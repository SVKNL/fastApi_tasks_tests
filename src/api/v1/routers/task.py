from fastapi import APIRouter

from src.api.v1.routers.dependencies import UOWDep
from src.schemas.task import TaskCreateRequest, TaskUpdateRequest, TaskDB, TaskListResponse, TaskResponse
from src.api.v1.services.task import TasksService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("/")
async def get_tasks(
    uow: UOWDep,
):
    tasks = await TasksService().get_tasks(uow)
    return TaskListResponse(payload=tasks)


@router.get("/{id}")
async def get_task(
    id: int,
    uow: UOWDep
):
    task = await TasksService().get_task(uow, id)
    return TaskResponse(payload=task)


@router.post("")
async def add_task(
    task: TaskCreateRequest,
    uow: UOWDep,
):
    task_id = await TasksService().add_task(uow, task)
    return {"task_id": task_id}


@router.patch("/{id}")
async def edit_task(
    id: int,
    task: TaskUpdateRequest,
    uow: UOWDep,
):
    await TasksService().edit_task(uow, id, task)
    return {"ok": True}

@router.delete("/{id}")
async def delete_task(
        id: int,
        uow: UOWDep,
):
    await TasksService().delete_task(uow, id)
    return {"ok": True}