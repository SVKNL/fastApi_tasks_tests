from src.schemas.user import CreateUserRequest
from src.utils.unit_of_work import IUnitOfWork


class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: CreateUserRequest):
        user_dict = user.model_dump()
        async with uow:
            user_id = await uow.user.add_one(user_dict)
            await uow.commit()
            return user_id

    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.user.find_all()
            return users

