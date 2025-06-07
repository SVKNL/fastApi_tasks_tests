from fastapi import APIRouter, Depends

from src.api.v1.routers.dependencies import UOWDep
from src.schemas.task import (TaskCreateRequest,
                              TaskUpdateRequest,
                              TaskListResponse,
                              TaskResponse,
                              TaskFilterSchema)
from src.api.v1.services.task import TasksService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("/")
async def get_tasks(
    filter: TaskFilterSchema = Depends(),
    service: TasksService = Depends(),
):
    tasks = await service.get_tasks(filter)
    return TaskListResponse(payload=tasks)


@router.get("/{id}")
async def get_task(
    id: int,
    uow: UOWDep
):
    task = await TasksService(uow).get_task(id)
    return TaskResponse(payload=task)


@router.post("")
async def add_task(
    task: TaskCreateRequest,
    uow: UOWDep,
):
    task_id = await TasksService(uow).add_task(task)
    return {"task_id": task_id}


@router.patch("/{id}")
async def edit_task(
    id: int,
    task: TaskUpdateRequest,
    uow: UOWDep,
):
    await TasksService(uow).edit_task(id, task)
    return {"ok": True}

@router.delete("/{id}")
async def delete_task(
        id: int,
        uow: UOWDep,
):
    await TasksService(uow).delete_task(id)
    return {"ok": True}