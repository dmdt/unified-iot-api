from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

SQL_USERS_DATABASE_URL = 'sqlite:///E:/unified-iot-api/source/config/user_test.db'

user_db_engine = create_engine(
    SQL_USERS_DATABASE_URL,
    connect_args={'check_same_thread': False}  # FIXME: special parameter for SQLITE
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=user_db_engine
)

Base = declarative_base()


def get_db_session() -> Session:
    db_session = SessionLocal()
    return db_session


def create_tables():
    Base.metadata.create_all(bind=user_db_engine)
