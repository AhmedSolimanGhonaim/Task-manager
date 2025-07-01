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
        title_in= title_in.strip()
        if not title_in:
            raise ValueError("title can not be empty")
        return title_in

    @field_validator("due_date", mode="before")
    def parse_due_date(cls, value: Optional[str]):
        if value is None:
            return None
        try:
            value = value.strip()
            return datetime.strptime(value, "%Y-%m-%d:%H")
        except ValueError:
            raise ValueError("due_date must be in format 'YYYY-MM-DD:HH'")

    # Validate that the due date is in the future
    @field_validator("due_date", mode="after")
    def validate_due_date(cls, date_in: Optional[datetime]):
        if date_in and date_in <= datetime.now():
            raise ValueError("Due date must be in the future")
        return date_in
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus]
    priority: Optional[TaskPriority]
    due_date: Optional[datetime]
    assigned_to: Optional[str] = Field(None, max_length=100)

    @field_validator("title")
    def validate_title(cls, title):
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Title cannot be empty or whitespace")
        return title

    @field_validator("due_date", mode="before")
    def parse_due_date(cls, value: Optional[str]):
        if value is None:
            return None
        try:
            value = value.strip()
            return datetime.strptime(value, "%Y-%m-%d:%H")
        except ValueError:
            raise ValueError("due_date must be in format 'YYYY-MM-DD:HH'")

    # Validate that the due date is in the future
    @field_validator("due_date", mode="after")
    def validate_due_date(cls, date_in: Optional[datetime]):
        if date_in and date_in <= datetime.now():
            raise ValueError("Due date must be in the future")
        return date_in
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

    model_config = {
        "from_attributes": True
    }
