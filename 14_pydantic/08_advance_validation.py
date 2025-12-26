# Advance Validation in pydantic
# Validation usecases
#This code demonstrates the four most common "real-world" validation patterns in Pydantic.
from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


#Multi-Field Validation
#Goal: Apply the exact same rule to multiple fields at once.
class Person(BaseModel):
    first_name:str
    last_name:str
    #How it works: By passing multiple strings to @field_validator('first_name', 'last_name'), Pydantic runs the names_be_capatalized function twice—once for each field.
    @field_validator('first_name','last_name')
    def names_be_capatalize(cls,v):
        #It uses .istitle() to ensure names start with a capital letter (e.g., "John" passes, but "john" fails).
        if not v.istitle():
            raise ValueError('Names must be capatalized')
        return v
    
    
# Data Normalization (Cleaning)
# Not just to validate, but to "fix" the data into a standard format.
class User(BaseModel):
    #The validator intercepts the email and returns a modified version.
    email:str
    @field_validator('email')
    def normalize_email(cls,v):
        #It removes accidental spaces with .strip() and forces the email to lowercase with .lower().
        return v.lower().strip()
    
#   Pre-Parsing with mode='before'
# Clean up "dirty" input before Pydantic's internal type-checker sees it.
class Product(BaseModel):
    price:str # $4.44
    #By setting mode='before', this validator runs before Pydantic tries to convert the data.
    @field_validator('price',mode='before')
    #Without mode='before', Pydantic might throw an error saying "$4.44" is not a valid number. This "clears the path" for the data.
    def parse_price(cls,v):
        if isinstance(v,str):
            return float(v.replace('$',''))
        return v
   
#  Cross-Field Logic
# Validate a relationship between two different fields.
class DateRange(BaseModel):
    start_date:datetime
    end_date: datetime
    #It uses @model_validator(mode="after"). In Pydantic V2, this validator has access to the whole object (usually called self rather than values).
    @model_validator(mode="after")
    def validate_date_range(cls,values):
        # It ensures that the start_date is mathematically "less than" (earlier than) the end_date.
        if values.start_date >= values.end_date:
            raise ValueError('end_date must come after start_date')
        return values
    

            