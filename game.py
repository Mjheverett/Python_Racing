# Python Project for Team Discovery Channel: Matthew Everett, Kevin Jeffers, Tait Loughridge, Katy Sage
#
# from drivers import Drivers
from karts import Kart
# from tracks import Tracks

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
    "standard_kart",
    "mushmellow_kart",
    "powerflower_kart",
    "drybomber_kart",
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

def game_menu():
    while True:
        choice = get_user_choice(game_menu)
        if choice == 1:
            driver_selection = get_user_choice(driver_menu)
        if choice == 2:
            kart_selection = get_user_choice(kart_menu)
        if choice == 3:
            track_selection = get_user_choice(track_menu)
        if choice == 4:
            print("""
            Your have selected:
            Driver: %s
            Kart: %s
            Track: %s""" % (driver_selection, kart_selection, track_selection))
        if choice == 5:
            game(driver_selection, kart_selection, track_selection)
        if choice == 6:
            exit_prompt = input("Are you sure you want to quit? All game data will be lost. (Y or N)").upper()
            if exit_prompt == "Y":
                break
            elif exit_prompt == "N":
                pass
            else:
                print("That was not a valid choice. Try again.")
                exit_prompt = input("Are you sure you want to quit? All game data will be lost. (Y or N)").upper()

def game(driver_selection, kart_selection, track_selection):
    pass

print(drybomber_kart.stats())

game_menu()