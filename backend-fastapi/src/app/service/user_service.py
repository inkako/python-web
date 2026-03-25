from app.core.crud import CrudBase
from app.models import User
from app.schema.user_schemas import UserCreate, UserUpdate
from app.util.pwd_utils import get_pwd_hash


class UserService(CrudBase[User, UserCreate, UserUpdate]):
    def __init__(self):
        super().__init__(model=User)

    async def get_by_username(self, username: str) -> User | None:
        return await self.model.get_or_none(username=username)

    async def create_user(self, user_in: UserCreate) -> User:
        user_in.password = get_pwd_hash(user_in.password)
        user = await self.create(user_in)
        return user


user_service = UserService()
