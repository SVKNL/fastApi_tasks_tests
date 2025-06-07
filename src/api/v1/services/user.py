from src.schemas.user import CreateUserRequest
from src.api.v1.routers.dependencies import UOWDep


class UsersService:
    def __init__(self, unit_of_work: UOWDep):
        self.uow = unit_of_work

    async def add_user(self, user: CreateUserRequest):
        user_dict = user.model_dump()
        async with self.uow:
            user_id = await self.uow.user.add_one(user_dict)
            return user_id

    async def get_users(self):
        async with self.uow:
            users = await self.uow.user.find_all()
            return users

