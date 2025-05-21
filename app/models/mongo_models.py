
from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    author: str
    text: str
    timestamp: Optional[str]

class History(BaseModel):
    status: str
    timestamp: Optional[str]

class TaskDetails(BaseModel):
    task_id: int
    comments: List[Comment] = []
    history: List[History] = []
    attachments: List[str] = []
