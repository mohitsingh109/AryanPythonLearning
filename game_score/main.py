from models.player import Player
from models.scoreboard import ScoreBoard

scoreboard = ScoreBoard()
scoreboard.add_player(Player("Aryan", 89))
scoreboard.add_player(Player("Arya", 8))
scoreboard.add_player(Player("Ary", 9))
scoreboard.add_player(Player("Ar", 7))
scoreboard.add_player(Player("Aryn", 76))
scoreboard.add_player(Player("Arjun", 74))
scoreboard.add_player(Player("Mohit", 87))
scoreboard.add_player(Player("Arian", 81))
scoreboard.add_player(Player("Ry", 1))
scoreboard.add_player(Player("Max", 13))
scoreboard.add_player(Player("Theo", 82))

def player_creation():
    username = input("What is the username of the player? ")
    score = int(input("What is the score of the player? "))
    player = Player(username, score)
    scoreboard.add_player(player)

def player_removal():
    username = input("Who do you wnt to remove? ")
    scoreboard.remove_player(username)

def update_score():
    username = input("Who do you want to update? ")
    score = int(input("What is their new score? "))
    scoreboard.update_score(username, score)

def show_all_players():
    players = scoreboard.get_players()
    for player in players:
        print(player)

def top_inputted_players():
    num = input("How many people do you want on the scoreboard? ")
    scoreboard.show_top_inputted_players(num)

def search_player():
    username = input("Who are you searching for? ")
    print(scoreboard.search_username(username))

def cli_menu():
    while True:
        print("What would you like to do? Enter the number corresponding with the action you want in the CLI menu below.\n"
               "1. Add Player\n"
               "2. Remove Player\n"
               "3. Update Score\n"
               "4. Show All Players\n"
               "5. Show Top 10 Players\n"
               "6. Show Top Inputted Player"
               "7. Search Player\n"
               "8. Exit")
        choice = input()
        if choice == "1":
            player_creation()
        elif choice == "2":
            player_removal()
        elif choice == "3":
            update_score()
        elif choice == "4":
            show_all_players()
        elif choice == "5":
            scoreboard.show_top_10()
        elif choice == "6":
            top_inputted_players()
        elif choice == "7":
            search_player()
        elif choice == "8":
            print("Thanks for using the program!")
            break
        else:
            print("That's invalid. Try again using the options below!")

cli_menu()