class CookieNotFound(Exception):
    def __init__(self):
        super().__init__("Cookie not found in the environment variable")


class userNotFound(Exception):
    def __init__(self):
        super().__init__("User not found")
