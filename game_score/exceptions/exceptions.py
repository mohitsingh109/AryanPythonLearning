class UsernameNotFoundError(Exception):
    def __init__(self, username):
        super().__init__(f"Username {username} not exist")

class UsernameAlreadyExistError(Exception):
    def __init__(self, username):
        super().__init__(f"Username {username} already taken")