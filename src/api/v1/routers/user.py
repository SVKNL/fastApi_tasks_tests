from fastapi import APIRouter

from src.api.v1.routers.dependencies import UOWDep
from src.schemas.user import CreateUserRequest
from src.api.v1.services.user import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(
    user: CreateUserRequest,
    uow: UOWDep,
):
    user_id = await UsersService(uow).add_user(user)
    return {"user_id": user_id}


@router.get("")
async def get_users(
    uow: UOWDep,
):
    users = await UsersService(uow).get_users()
    return users
