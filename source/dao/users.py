from config.users import get_db_session
from sqlalchemy.orm import Session
from models.users import UserModel


class UserDAO:
    def __init__(self, db: Session = get_db_session()):
        self.db = db

    def add_user(self, record: UserModel) -> UserModel:
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

    def get_user_by_login(self, user_login) -> UserModel:
        print(type(self.db))
        return self.db.query(UserModel).filter(UserModel.login == user_login).first()
