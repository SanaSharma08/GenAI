# Best Practices to build models in pydantic.

# Model Organization
# 1. Define leaf models first - Models with no dependencies
# 2. Build upward - Gradually compose more complex models
# 3. Use clear naming - Make relationships obvious
# 4. Group related models - Keep models in logical modules

from typing import List, Optional, Union
from pydantic import BaseModel, Field, field_validator

# --- 1. LEAF MODELS (Smallest Units) ---
class Product(BaseModel):
    id: int
    name: str
    price: float

class Address(BaseModel):
    city: str
    zip_code: str

# --- 2. COMPOSITE MODELS (Building Upward) ---
class User(BaseModel):
    username: str
    email: str
    shipping_address: Optional[Address] = None # Clear naming

# --- 3. ROOT MODEL (The Core Business Logic) ---
class Order(BaseModel):
    order_id: int
    customer: User
    items: List[Product]
    
    @field_validator('items')
    def must_have_items(cls, v):
        if len(v) == 0:
            raise ValueError("An order must have at least one product")
        return v

# ----------------------------------------------

# Performance Considerations
# 1. Deep nesting impacts performance - Keep reasonable depth
# 2. Large lists of nested models - Consider pagination
# 3. Circular references - Use carefully, can cause memory issues
# 4. Lazy loading - Consider for expensive nested computations

# -----------------------------------------------

# Data Modeling Tips 
# A common mistake is trying to make models fit your database table exactly. Instead, model your domain. If an article can contain either text or a video, use a Union.
# 1 . Model real-world relationships - Mirror your domain structure
# 2. Use Optional appropriately - Not all relationships are required
# 3. Consider Union types - For polymorphic relationships
# 4. Validate business rules - Use model validators for cross-model logic

class TextBlock(BaseModel):
    content: str

class VideoBlock(BaseModel):
    url: str
    duration_seconds: int

class Article(BaseModel):
    title: str
    # Polymorphic relationship: The list can contain either type
    blocks: List[Union[TextBlock, VideoBlock]]

#--------------------------------------------------