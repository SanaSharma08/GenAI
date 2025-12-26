# Pydantic Serialization 
# Serialization is the process of converting your complex Pydantic objects into a format that can be easily stored, printed, or sent over a network (like a Python dictionary or a JSON string).

# 1. model_dump(): The Python Dictionary
# Recursive: It automatically converts nested models (like Address) into nested dictionaries.
# Type Retention: It keeps native Python types. Notice in your output that createdAt is still a datetime.datetime object, and is_active is a Python bool.
# Use Case: Use this when you need to pass data to other Python libraries (like a database driver or a template engine like Jinja2).

# 2. model_dump_json(): The JSON String
# This method converts the model into a JSON-formatted string.
# String Conversion: Everything is turned into text.
# JSON Standards: Python True becomes JSON false, and None becomes null.
# Use Case: Use this when sending data to a Web Browser, a Mobile App, or saving it to a .json file.

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city:str
    zip_code:str
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags : List[str] =[]
    
    # Customizing JSON with json_encoders
    # JSON is a simple format that does not natively support "Date" objects. Usually, JSON dates look like 2024-03-15T14:30:20.
    model_config=ConfigDict(
        # Custom Encoder
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
        
    )
    
user=User(
    id=1,
    name="Ojas",
    email="ahsahjsbsjs@ai",
    createdAt=datetime(2024,3,15,14,30,20),
    address=Address(
        street="Something",
        city="Jaipur",
        zip_code="7685877"
    ),
    is_active=False,
    tags=["Premium","Subscriber"]
)

python_dict=user.model_dump() # converts to dictionary format
print('-'*20)
print(f"\nPython Dictionary : model_dump(): {python_dict}")
# {'id': 1, 'name': 'Ojas', 'email': 'ahsahjsbsjs@ai', 'is_active': False, 'createdAt': datetime.datetime(2024, 3, 15, 14, 30), 'address': {'street': 'Something', 'city': 'Jaipur', 'zip_code': '7685877'}, 'tags': ['Premium', 'Subscriber']}

json_str=user.model_dump_json()
print('-'*20)
print(f"\nJSON ENCODED STRING : model_dump_json(): {json_str}")
# {"id":1,"name":"Ojas","email":"ahsahjsbsjs@ai","is_active":false,"createdAt":"15-03-2024 14:30:20","address":{"street":"Something","city":"Jaipur","zip_code":"7685877"},"tags":["Premium","Subscriber"]}

# When serializing, you often want to hide certain fields (like a password or internal id). You can do this easily with the exclude parameter:
# This will hide the 'email' and 'is_active' fields in the output
limited_dict = user.model_dump(exclude={'email', 'is_active'})
print('-'*30)
print(limited_dict)
# {'id': 1, 'name': 'Ojas', 'createdAt': datetime.datetime(2024, 3, 15, 14, 30, 20), 'address': {'street': 'Something', 'city': 'Jaipur', 'zip_code': '7685877'}, 'tags': ['Premium', 'Subscriber']}