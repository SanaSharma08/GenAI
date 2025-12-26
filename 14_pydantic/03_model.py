# simple user validation
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

# 1. Define your model with strict types
class UserProfile(BaseModel):
    id: int
    username: str
    is_premium: bool
    signup_date: datetime
    scores: List[int]

# 2. Raw data (Imagine this came from a JSON API or a Form)
# Notice that almost everything is a string, even the numbers and booleans!
raw_data = {
    "id": "101",                      # String to Int
    "username": "coder_99",           # Standard String
    "is_premium": "yes",              # "yes" to True
    "signup_date": "2023-12-25 14:30", # String to Datetime object
    "scores": ["85", 90, "95"]        # List of mixed strings/ints to List[int]
}
# "id": "apple" : Validation Error: 1 validation error for UserProfile

# 3. Parse the data
try:
    user = UserProfile(**raw_data)
    
    print("--- Successfully Parsed Model ---")
    print(f"ID: {user.id} ({type(user.id)})")
    print(f"Premium Status: {user.is_premium} ({type(user.is_premium)})")
    print(f"Signup: {user.signup_date} ({type(user.signup_date)})")
    print(f"Scores: {user.scores} (List of {type(user.scores[0])})")
    
    # Exporting back to a clean dictionary
    print("\n--- Clean JSON Output ---")
    print(user.model_dump_json(indent=2))

except Exception as e:
    print(f"Validation Error: {e}")