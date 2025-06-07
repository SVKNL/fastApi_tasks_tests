from src.schemas.task import TaskCreateRequest, TaskDB, TaskUpdateRequest
from src.utils.unit_of_work import IUnitOfWork


class TasksService:
    async def add_task(self, uow: IUnitOfWork, task: TaskCreateRequest) -> TaskDB:
        tasks_dict = task.model_dump()
        async with uow:
            task_id = await uow.task.add_one(tasks_dict)
            await uow.commit()

            return task_id

    async def get_tasks(self, uow: IUnitOfWork):
        async with uow:
            tasks = await uow.task.find_all()
            return [task.to_schema() for task in tasks]

    async def get_task(self, uow: IUnitOfWork, task_id):
        async with uow:
            task = await uow.task.get_one(task_id)
            await uow.commit()

            return task.to_schema()

    async def edit_task(self, uow: IUnitOfWork, task_id: int, task: TaskUpdateRequest):
        tasks_dict = task.model_dump()
        async with uow:
            await uow.task.edit_one(task_id, tasks_dict)
            await uow.commit()

    async def delete_task(self, uow: IUnitOfWork, task_id: int):
        async with uow:
            await uow.task.delete_one(task_id)
            await uow.commit()