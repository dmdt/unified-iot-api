import uvicorn
from fastapi import FastAPI
from routers.users import router
from utils.app_exceptions import AppExceptionType, app_exception_handler
from config.users import create_tables

create_tables()

app = FastAPI()


@app.exception_handler(AppExceptionType)
async def custom_app_exception_handler(request, exp):
    return await app_exception_handler(request, exp)


if __name__ == "__main__":
    app.include_router(router)
    uvicorn.run(app, host="0.0.0.0", port=8000)
