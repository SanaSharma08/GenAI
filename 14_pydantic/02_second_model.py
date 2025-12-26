from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
input_data = {'id':101,'name':"Chaicode",'is_active': 25}

user=User(**input_data) # ** unpacks dictionary

print(user) #1 validation error for User 

# Input should be a valid boolean, unable to interpret input [type=bool_parsing, input_value=25, input_type=int]