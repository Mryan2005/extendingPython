class NotFoundProject(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AccessTokenNotExist(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
