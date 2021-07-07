from pydantic import BaseModel


class UserSignInSchema(BaseModel):
    login: str
    password: str


class UserSignUpSchema(UserSignInSchema):
    ...


class UserSchema(UserSignInSchema):
    id: int
