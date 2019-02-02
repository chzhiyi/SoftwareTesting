class const(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setter__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError
        if not name.isupper():
            raise self.ConstCaseError
        self.__dict__[name] = value
