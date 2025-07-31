from models.player import Player
from models.scoreboard import ScoreBoard

scoreboard = ScoreBoard()

def cli_menu():
    print("What would you like to do? Enter the number corresponding with the action you want in the CLI menu below.\n"
          "1. Add Player\n"
          "2. Remove Player\n"
          "3. Update Score\n"
          "4. Show All Players\n"
          "5. Show Top 10 Players\n"
          "6. Search Player\n"
          "7. Exit\n")

cli_menu()