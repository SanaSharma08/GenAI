# Nested models in pydantic
# Allows u to compose complex data structure by embedding one pydantic model into another.

# Instead of having a flat, messy model with fields like address_street and address_city, you’ve created a hierarchy.

# Address is a standalone "Child" model.
# User is the "Parent" model that contains the Child.

from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
class User(BaseModel):
    id: int
    name: str
    address: Address # reference of Address Model
    
address=Address(
    street="123",
    city="Delhi",
    postal_code="100001"
)

user= User(
    id=1,
    name="Ojas",
    address=address
)

# or

user_data={
    "id":1,
    "name":"Ojas",
    "address":{
        "street":"321 ...",
        "city":"Delhi",
        "postal_code":"200209"
    }
}

user2=User(**user_data) # unpacking
print(user2)
print(user)
    
