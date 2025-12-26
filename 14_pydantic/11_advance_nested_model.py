# Advance Nested Models
# You are now handling scenarios typical of large-scale enterprise APIs, CMS platforms, and complex database relationships.

# ---------------------------------------------
# 1. Optional Nested Model : Handles missing data gracefully without KeyErrors.
# Best For: Profile settings, optional metadata.
from pydantic import BaseModel
from typing import Optional, List, Union


# In your Company and Employee classes, the use of Optional (or | None in Python 3.10+) allows for data that is missing or incomplete without crashing the program.
class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    # If you provide an address, Pydantic validates it against the Address model. If you leave it out, it simply becomes None.
    address: Optional[Address]=None
    
class Employee(BaseModel):
    name:str
    company:Optional[Company]=None
    
# ---------------------------------------------


# 2. Mixed Data Types: Allows a single list to hold completely different shapes of data.
# Best For: News feeds, Page builders, polymorphic API responses.
class TextContent(BaseModel):
    type: str='text'
    content: str
    
class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str
    
# This is extremely common in content management systems (CMS) where a page is made up of different "blocks" (text, images, videos).
class Article(BaseModel):
    title: str
    sections: List[Union[TextContent,ImageContent]]
    
    
# --------------------------------------------------   
    
# 3. Deeply Nested Structure: Keeps logic organized; "Small" models can be reused elsewhere.
# Best For: Geography, Inventory, Financial systems.
class Country(BaseModel):
    name: str
    code: str
class State(BaseModel):
    name: str
    country: Country
class City(BaseModel):
    name: str
    state: State
class Address(BaseModel):
    name: str
    city: City
class Organization(BaseModel):
    name: str
    headquater: Address
    branches: List[Address]=[]
    
# The Validation Chain: When you create an Organization, Pydantic starts a chain reaction of validation:

# Organization checks Address.
# Address checks City.
# City checks State.
# State checks Country.