from fastapi import APIRouter
from app_containers.main import ApplicationServiceContainer
from schemas.users import UserSignUpSchema, UserSchema
from services.users import UserService
from utils.service_result import handle_result

router = APIRouter(prefix='/users')

user_service = ApplicationServiceContainer()


@router.get('/signup/{login}/{password}', response_model=UserSchema)
async def signup(
        login: str,
        password: str,


):
    service: UserService = user_service.user_service()
    return handle_result(service.signup(
        UserSignUpSchema(
            login=login,
            password=password
        )
    ))
