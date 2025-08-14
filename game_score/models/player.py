class Player:

    def __init__(self, username, score):
        self.__username = username
        self.__score = score

    def get_username(self):
        return self.__username

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        self.__score = new_score

    def __str__(self):
        return f"Score: {self.get_score()} | Username: {self.get_username()}"


