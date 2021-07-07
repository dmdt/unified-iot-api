from dao.users import UserDAO
from repositories.users import UserRepository
from services.users import UserService

from dependency_injector import containers, providers


class ApplicationServiceContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_dao = providers.Factory(
        UserDAO,
        # db=get_db_session()
    )

    user_repository = providers.Factory(
        UserRepository,
        dao=user_dao
    )

    user_service = providers.Factory(
        UserService,
        repository=user_repository
    )
