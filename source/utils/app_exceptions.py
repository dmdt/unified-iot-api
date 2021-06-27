from fastapi import Request
from starlette.responses import JSONResponse


class AppExceptionType(Exception):
    def __init__(self, status_code: int, description: str):
        self.exception_type = self.__class__.__name__
        self.status_code = status_code
        self.description = description

    def __str__(self):
        return f'Exception: code - {self.status_code}, description - {self.description}'


async def app_exception_handler(request: Request, exc: AppExceptionType):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "app_exception": exc.exception_type,
            "descriptions": exc.description,
        },
    )


class AppException:
    class UserAlreadyExistException(AppExceptionType):
        def __init__(self, description: str = 'This user already exists.'):
            status_code = 400
            super().__init__(status_code, description)

    class UserPasswordException(AppExceptionType):
        def __init__(self, description: str = 'Entered password is incorrect.'):
            status_code = 400
            super().__init__(status_code, description)
