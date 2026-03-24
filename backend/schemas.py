from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

# ---------------------------------------------------------
# ENUM: TaskStatus
# ---------------------------------------------------------
# Same idea as in models.py, but used for API validation
class TaskStatus(str, Enum):
    PENDING = "pending"
    DONE = "done"


# ---------------------------------------------------------
# BASE SCHEMA: TaskBase
# ---------------------------------------------------------
# Contains common fields shared across multiple schemas
class TaskBase(BaseModel):

    # Required field: task title
    title: str

    # Optional field: can be None
    description: Optional[str] = None

    # Required field: deadline (date + time)
    deadline: datetime

    # Default status = "pending"
    status: TaskStatus = TaskStatus.PENDING


# ---------------------------------------------------------
# SCHEMA: TaskCreate
# ---------------------------------------------------------
# Used when creating a new task
# Inherits all fields from TaskBase
class TaskCreate(TaskBase):
    pass


# ---------------------------------------------------------
# SCHEMA: TaskUpdate
# ---------------------------------------------------------
# Used when updating a task
# All fields are optional → allows partial updates
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    status: Optional[TaskStatus] = None


# ---------------------------------------------------------
# SCHEMA: Task (Response Model)
# ---------------------------------------------------------
# Used when returning data to the client (API response)
class Task(TaskBase):

    # Include ID (not provided during creation)
    id: int

    class Config:
        # Allows compatibility with SQLAlchemy objects
        # (so FastAPI can convert DB objects → JSON automatically)
        from_attributes = True