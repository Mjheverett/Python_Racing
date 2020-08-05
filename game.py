# Python Project for Team Discovery Channel: Matthew Everett, Kevin Jeffers, Tait Loughridge, Katy Sage
#
from drivers import Driver_1, Driver_2, Driver_3, Driver_4
from karts import Standard_kart, Mushmellow_kart, Powerflower_kart, Drybomber_kart
from tracks import Track_1, Track_2, Track_3, Track_4

print("""
Welcome to Definitely NOT Mario Kart

A text based racing game.

Choose your driver and get racing!
""")

game_menu = [
    "Pick a Driver",
    "Pick a Kart",
    "Pick a Track",
    "View your selections",
    "RACE!!!",
    "Exit"
]

kart_menu = [
    "Standard",
    "Mushmellow",
    "Powerflower",
    "Dry Bomber"
]

driver_menu = [
    "Veteran",
    "Crafty",
    "Cavalier",
    "Joe"
]

track_menu = [
    "Suzuka",
    "Fuji",
    "Inagawa",
    "Tsukuba"
]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "Please choose an option: "
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

def game_startmenu():
    while True:
        choice = get_user_choice(game_menu)
        if choice == 1:
            choice = get_user_choice(driver_menu)
            if choice == 1:
                players_driver = Driver_1("Veteran", 5, 10, 5, 5, 10)
            if choice == 2:
                players_driver = Driver_2("Crafty", 0, 10, 10, 10, 5)
            if choice == 3:
                players_driver = Driver_3("Cavalier", 10, 0, 5, 5, 5)
            if choice == 4:
                players_driver = Driver_4("Joe", 5, 5, 5, 5, 5)
        if choice == 2:
            choice = get_user_choice(kart_menu)
            if choice == 1:
                players_kart = Standard_kart("Standard", 6.5, 4, 9, 6.5)
            if choice == 2:
                players_kart = Mushmellow_kart("Mushmellow", 4.3, 6.9, 6.9, 8.7)
            if choice == 3:
                players_kart = Powerflower_kart("Powerflower", 6.7, 4.3, 9, 8.7)
            if choice == 4:
                players_kart = Drybomber_kart("Dry Bomber", 3.4, 9.8, 3.9, 9.5)
        if choice == 3:
            choice = get_user_choice(track_menu)
            if choice == 1:
                players_track = Track_1("Suzuka", 3, 0, 8, 8)
            if choice == 2:
                players_track = Track_2("Fuji", 5, 8, 4, 3)
            if choice == 3:
                players_track = Track_3("Inagawa", 8, 5, 3, 5)
            if choice == 4:
                players_track = Track_4("Tsukuba", 9, 0, 7, 4)
        if choice == 4:
            print(players_driver.stats())
            print(players_kart.stats())
            print(players_track.stats())
        if choice == 5:
            game(players_driver, players_kart, players_track)
        if choice == 6:
            exit_prompt = input("Are you sure you want to quit? All game data will be lost. (Y or N): ").upper()
            if exit_prompt == "Y":
                break
            elif exit_prompt == "N":
                pass
            else:
                print("That was not a valid choice. Try again. ")
                exit_prompt = input("Are you sure you want to quit? All game data will be lost. (Y or N): ").upper()

def game(players_driver, players_kart, players_track):
    pass

