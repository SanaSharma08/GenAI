# Mixing pydantic and typing in python

from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Union, Literal, Annotated

# 1. Complex Containers (List, Dict)
class Ingredient(BaseModel):
    name: str
    quantity: float

class Recipe(BaseModel):
    # Mixing: Pydantic ensures 'ingredients' is a list AND every item is an Ingredient object
    ingredients: List[Ingredient] 
    tags: Dict[str, str]
class Cart(BaseModel):
    user_id:int
    items: List[str]
    # Pydantic will ensure keys are strings and values are integers
    quantities: Dict[str,int] # a dictionary with str keys and int values.
    
    
# 2. Optional and Nullable Fields (Optional / | None)
#In modern Python (3.10+), we use | None, but Pydantic handles both. It tells Pydantic that a field can be missing or null.
class User(BaseModel):
    username: str
    bio: Optional[str] = None  # If not provided, it defaults to None

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str]=None # a field thatcan be string or None
    
# 3. Multiple Choices (Union and Literal)
# Union: The data can be one of several types.
# Literal: The data must be an exact specific value.

class Payment(BaseModel):
    # Can be an integer ID OR a string username
    identifier: Union[int, str] 
    
    # Must be exactly one of these three strings
    currency: Literal["USD", "EUR", "GBP"]
    
    
# 4 : The "Modern Way": Annotated
# The most powerful way to mix these two is using Annotated. This allows you to keep the type hint clean while adding Pydantic-specific "metadata" (like range limits).

class Product(BaseModel):
    # 'int' is for the IDE, 'Field' is for Pydantic's runtime check
    price: Annotated[int, Field(gt=0, le=1000)] 
    description: Annotated[str, Field(max_length=50)]

    