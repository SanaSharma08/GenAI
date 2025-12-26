#Computed property in pydantic
# a Computed Property is a field that is not part of the input data but is calculated "on the fly" using other fields in the model.
#While standard Python has the @property decorator, Pydantic’s @computed_field takes it a step further by allowing these calculated values to be serialized (included in your JSON or dictionary output).
#Normally, if you just use a standard Python @property, it works fine for code logic, but it disappears when you convert your model to a dictionary or JSON.

#By adding @computed_field, you tell Pydantic: "Treat this method like a real piece of data. When I export this model, I want this value to be there."

#COMMON USECASE: Instead of making a user provide first_name, last_name, AND full_name, you just ask for the first two and compute the third

from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: float
    quantity: int
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
    
class Booking(BaseModel):
    user_id:int
    room_id: int
    nights: int=Field(..., ge=1)
    rate_per_night:float
    
    @computed_field # <--- Tells Pydantic to include this in model_dump()
    @property # <--- Standard Python property logic
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
booking = Booking(
    user_id = 123,
    room_id=456,
    nights=3,
    rate_per_night=100.0
)

print(booking.total_amount) #Output: 300.0. (This works like a normal attribute).
print(booking.model_dump())
'''{
    "user_id": 123,
    "room_id": 456,
    "nights": 3,
    "rate_per_night": 100.0,
    "total_amount": 300.0  # <--- Included because of @computed_field!
}'''

# Order of Decorators: You must put @computed_field above @property.

# Read-Only: By default, these are read-only. You cannot do booking.total_amount = 500.

# Performance: The calculation happens every time you access the property or serialize the model. If the calculation is extremely heavy (like a complex database query), be careful about using it frequently.