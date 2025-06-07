from src.models.task import User
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
    model.related_field_1 = 'watched_tasks'
    model.related_field_2 = 'executed_tasks'

