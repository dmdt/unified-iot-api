from utils.app_exceptions import AppExceptionType


class ServiceResult:
    def __init__(self, arg):
        if isinstance(arg, AppExceptionType):
            self.success = False
            self.exception_type = arg.exception_type
            self.status_code = arg.status_code
        else:
            self.success = True
            self.exception_type = None
            self.status_code = None
        self.value = arg

    def __repr__(self):
        if self.success:
            return "<ServiceResult Success>"
        return f"<ServiceResult AppException {self.exception_type}>"

    def __enter__(self):
        return self.value

    def __exit__(self, *kwargs):
        pass


def handle_result(result: ServiceResult):
    if not result.success:
        with result as exception:
            raise exception
    with result as result:
        return result
