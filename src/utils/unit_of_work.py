from abc import ABC, abstractmethod
from typing import Type

from src.database import async_session_maker

from src.repositories.task import TaskRepository
from src.repositories.user import UserRepository


class IUnitOfWork(ABC):
    user: Type[UserRepository]
    task: Type[TaskRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session = async_session_maker()

    async def __aenter__(self):
        self.user = UserRepository(self.session)
        self.task = TaskRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
