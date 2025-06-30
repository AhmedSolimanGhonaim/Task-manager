from  app.models.taskmodel import  TaskStatus ,TaskPriority

from pydantic import BaseModel,Field , field_validator
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str = Field(..., max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: Optional[TaskStatus] = TaskStatus.pending
    priority: Optional[TaskPriority] = TaskPriority.medium
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(default=None , max_length=100)
    
    @field_validator("title")
    def validate_title(cls,title_in):
        title_in= title_in.stripe()
        if not title_in:
            raise ValueError("title can not be empty")
        return title_in

    @field_validator("due_date")
    def due_date_validator(cls,date_in):
        if date_in and date_in <= datetime.now():
            raise ValueError ("date must be in future")

        return date_in


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus]
    priority: Optional[TaskPriority]
    due_date: Optional[datetime]
    assigned_to: Optional[str] = Field(None, max_length=100)

    @field_validator("title")
    def validate_title(cls, v):
        if v is not None:
            v = v.strip()
            if not v:
                raise ValueError("Title cannot be empty or whitespace")
        return v

    @field_validator("due_date")
    def validate_due_date(cls, v):
        if v and v <= datetime.utcnow():
            raise ValueError("Due date must be in the future")
        return v
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: Optional[datetime]
    due_date: Optional[datetime]
    assigned_to: Optional[str]

    class Config:
        orm_mode = True
