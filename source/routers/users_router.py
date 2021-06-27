from fastapi import APIRouter
from utils.app_exceptions import AppException

router = APIRouter(prefix='/users')


@router.get('/record/{record_id}')
async def get_record(record_id: int):
    raise AppException.UserAlreadyExistException()
