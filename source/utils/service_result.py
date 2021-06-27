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