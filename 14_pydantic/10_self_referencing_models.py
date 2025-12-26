# Self referencing models in pydantic
#This concept is known as a Recursive Model or a Self-Referencing Model.
# It is used whenever you have data that has a "tree-like" or "parent-child" structure, where an item can contain other items of the exact same type.

#Common real-world examples include comment threads, folder/file structures, or organizational charts (managers who manage employees who are also managers).

from typing import List,Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    #In Python, you usually cannot refer to a class inside itself because the class isn't "finished" being defined yet.
    #If you wrote replies: List[Comment], Python would throw an error saying Comment is not defined.
    #The Solution: By putting the name in quotes—'Comment'—you are creating a Forward Reference. You are telling Pydantic: "Trust me, there will be a class named Comment soon; look for it once you're done reading the file."
    replies: Optional[List['Comment']] = None
    
Comment.model_rebuild()
# Calling Comment.model_rebuild() performs the following:

# It scans the model for any string-based type hints.
# It replaces those strings with the actual class references now that the class is fully defined.
# It prepares the internal validation logic so it can handle deep nesting.

comment=Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(id=2,content="Reply1",replies=[
            Comment(id=21,content="Reply21"),
            Comment(id=22,content="Reply22")
            ]),
        Comment(id=3,content="Reply2"),
        Comment(id=4,content="Reply3"),
        Comment(id=5,content="Reply4"),
        Comment(id=6,content="Reply5"),
        Comment(id=7,content="Reply6")
    ]
)