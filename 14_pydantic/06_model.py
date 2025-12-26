#Field and model validators in python
#In Pydantic, validators are the "brains" of your data model. While type hints (like str or int) handle the type, validators handle the logic.
from pydantic import BaseModel, Field, field_validator, model_validator

# Field Validator
#A @field_validator focuses on one specific field in isolation. It doesn't care about the rest of the model; it only cares if the value assigned to its target field is valid.
class User(BaseModel):
    username: str
    
    @field_validator('username') # decorator : applies to a field
    # It receives v (the value of that specific field).
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v # Always return the value!
    
# Model Validator
#A @model_validator looks at the entire object. It is used when the validity of one field depends on the value of another field.
class SignupData(BaseModel):
    password:str
    confirm_password: str
    @model_validator(mode='after')
    def password_match(cls,values):
        if(values.password != values.confirm_password):
            raise ValueError("Passwords do not match")
        return values
    