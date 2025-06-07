from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum

from fastapi import Query


class TaskStatus(str, Enum):
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'


class TaskCreateRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    author_id: int
    assignee_id: int = None
    column_id: Optional[int] = None
    sprint_id: Optional[int] = None
    board_id: Optional[int] = None
    group_id: Optional[int] = None



class TaskUpdateRequest(TaskCreateRequest):
    pass





class TaskDB(TaskCreateRequest):
    id: int
    description: Optional[str]
    status: TaskStatus
    created_at: datetime
    sprint_id: Optional[int]
    group_id: Optional[int]
    title: str
    author_id: int
    assignee_id: int
    column_id: Optional[int]
    board_id: Optional[int]


class TaskResponse(BaseModel):
    payload: TaskDB


class TaskFilterSchema(BaseModel):
    status: Optional[TaskStatus] = Query(None)
    author_id: Optional[int] = Query(None)
    assignee_id: Optional[int] = Query(None)


class TaskListResponse(BaseModel):
    payload: List[TaskDB]




