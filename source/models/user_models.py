from config import user_database
from sqlalchemy import Column, Integer, String, Boolean


class User(user_database.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    login = Column(String)
    devices = Column(Integer)
    is_admin = Column(Boolean)

    def __repr__(self):
        return f'<User(id={self.id},' \
               f'password={self.password},' \
               f'login={self.login},' \
               f'devices={self.devices},' \
               f'is_admin={self.is_admin}'
