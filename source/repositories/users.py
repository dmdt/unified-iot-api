from dao.users import UserDAO
from models.users import UserModel
from schemas.users import UserSignUpSchema, UserSchema

from typing import Optional


class UserRepository:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create_user_record(self, data: UserSignUpSchema) -> Optional[UserSchema]:
        if self.dao.get_user_by_login(data.login) is not None:
            return None
        else:
            user_record = UserModel(
                password=data.password,
                login=data.login,
            )
            user_record = self.dao.add_user(record=user_record)
            return UserSchema(
                id=user_record.id,
                login=user_record.login,
                password=user_record.password
            )
