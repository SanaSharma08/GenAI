# . Adding validations with Field

from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id:int
    items: List[str]
    quantities: Dict[str,int] # a dictionary with str keys and int values.

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str]=None # a field thatcan be string or None
    
# Adding Validation with Field-------------------
class Employee(BaseModel): # Employee inherits BaseModel
    id: int
    name: str = Field(
        ..., # ... means required field
        min_length=3,
        max_length=50,
        decription="Employee Name",
        examples = "Hitech Choudhary"
    )
    department: Optional[str]= 'General'
    salary: float = Field(
        ...,
        ge=10000 # ge means >=
        le = 100000000
        description="Employee salary in INR"
    )
    
class User(BaseModel):
    #When you use pattern (formerly regex in V1) in a Pydantic Field, Pydantic checks if the input string matches your pattern. If it doesn't, it throws a ValidationError.
    email: str = Field(
        ...,
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )
    phone: str = Field(..., regex=r"^\d{3}-?\d{3}-?\d{4}$")
    age: int = Field(..., ge=0,le=150,description="Age in years")
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description = "Discount percentage"
    )
    #If you are using the latest version of Pydantic, always use pattern. If you use the old regex keyword, Pydantic will usually give you a warning or an error.
# ------------------------------------------------ 
  
cart_data = {
    "user_id":123,
    "items": ["Laptop", "Mouse" ,"Keyboard"],
    "quantities": {
        "Laptop": "1",  # String "1": becomes int 1
        "Mouse": 2, 
        "Keyboard": True, # Boolean True: becomes int 1
        "Monitor": "5"   # String "5" : becomes int 5
    }
}

cart = Cart(**cart_data)
print(cart)