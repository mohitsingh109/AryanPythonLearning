from game_score.utils.helpers import sort_players, validation

class ScoreBoard:
    def __init__(self):
        self.__players = []

    def add_player(self, new_player):
        if validation(new_player.get_score()):
            self.__players.append(new_player)
        else:
            print("Invalid!")

    def remove_player(self, username):
        to_be_removed = self.search_username(username)
        self.__players.remove(to_be_removed)

    def update_score(self, username, new_score):
        if validation(new_score):
            player_to_update = self.search_username(username)
            player_to_update.set_score(new_score)
        else:
            print("Invalid!")

    def search_username(self, username):
        for player in self.__players:
            if player.get_username() == username:
                return player
        return None

    def show_top_10(self):
        self.show_top_inputted_players(10)

    def show_top_inputted_players(self, num):
        if validation(num):
            sorted_players = sort_players(self.__players)
            for i in range(min(num, len(sorted_players))):
                print(sorted_players[i])
        else:
            print("Invalid scoreboard num.")

    def get_players(self):
        return self.__players