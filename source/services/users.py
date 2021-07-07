from models.users import UserModel
from repositories.users import UserRepository
from schemas.users import UserSignUpSchema
from repositories.users import UserRepository
from utils.service_result import ServiceResult
from utils.app_exceptions import AppException


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def signup(self, user_schema: UserSignUpSchema) -> ServiceResult:
        user_record = self.repository.create_user_record(data=user_schema)
        if user_record:
            return ServiceResult(user_record)
        else:
            return ServiceResult(AppException.UserAlreadyExistException())
