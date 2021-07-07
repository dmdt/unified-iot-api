from config import users
from sqlalchemy import Column, Integer, String, Boolean


class UserModel(users.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    login = Column(String)

    def __repr__(self):
        return f'<User(id={self.id},' \
               f'password={self.password},' \
               f'login={self.login},' \
