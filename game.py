# Python Project for Team Discovery Channel: Matthew Everett, Kevin Jeffers, Tait Loughridge, Katy Sage
#
from drivers import Driver_1, Driver_2, Driver_3, Driver_4
from karts import Standard_kart, Mushmellow_kart, Powerflower_kart, Drybomber_kart, Kart
from tracks import Track_1, Track_2, Track_3, Track_4, Tracks
import track_events
import attributes

print("""
Welcome to Definitely NOT Mario Kart

  ___
    _-_-  _/\______\\__
 _-_-__  / ,-. -|-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'

A text based racing game.

Choose your driver and get racing!""")

game_menu = """
    1: Pick a Driver
    2: Pick a Kart
    3: Pick a Track
    4: View your selections
    5: RACE!!!
    6: Exit
    """

# GAME MENU AND FUNCTIONS--------------------------------------------------------------------------

kart_menu = ("""
    1: Standard:      
            Speed: 6.5, Handling: 4
    2: Mushmellow:    
            Speed: 4.3, Handling: 6.9
    3: Powerflower:   
            Speed: 6.7, Handling: 4.3
    4: Dry Bomber:    
            Speed: 3.4, Handling: 9.8""")

driver_menu = ("""
    1: Veteran:   
            Speed:  5,  Knowledge: 10,  Alertness:  5,  Mech. Skill: 10
    2: Crafty:    
            Speed:  0,  Knowledge: 10,  Alertness: 10,  Mech. Skill:  5
    3: Cavalier:  
            Speed: 10,  Knowledge:  0,  Alertness:  5,  Mech. Skill: 10
    4: Joe:       
            Speed:  5,  Knowledge:  5,  Alertness:  5,  Mech. Skill:  5""")

track_menu = ("""
    1: Suzuka:    
            Difficulty: 3, Weather: 0, Speed: 8, Handling: 8
    2: Fuji:      
            Difficulty: 5, Weather: 8, Speed: 4, Handling: 3
    3: Inagawa:   
            Difficulty: 8, Weather: 5, Speed: 3, Handling: 5
    4: Tsukuba:   
            Difficulty: 9, Weather: 0, Speed: 7, Handling: 4""")

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")

def game_startmenu():
    while True:
        print(game_menu)
        menu_choice = int(input("Please choose an option: "))
        if menu_choice == 1:
            print(driver_menu)
            driver_choice = int(input("Please choose an option: "))
            if driver_choice == 1:
                players_driver = Driver_1("Veteran", 5, 10, 5, 5, 10)
            if driver_choice == 2:
                players_driver = Driver_2("Crafty", 0, 10, 10, 10, 5)
            if driver_choice == 3:
                players_driver = Driver_3("Cavalier", 10, 0, 5, 5, 5)
            if driver_choice == 4:
                players_driver = Driver_4("Joe", 5, 5, 5, 5, 5)
        if menu_choice == 2:
            print(kart_menu)
            kart_choice = int(input("Please choose an option: "))
            if kart_choice == 1:
                players_kart = Standard_kart("Standard", 6.5, 4, 9, 6.5)
            if kart_choice == 2:
                players_kart = Mushmellow_kart("Mushmellow", 4.3, 6.9, 6.9, 8.7)
            if kart_choice == 3:
                players_kart = Powerflower_kart("Powerflower", 6.7, 4.3, 9, 8.7)
            if kart_choice == 4:
                players_kart = Drybomber_kart("Dry Bomber", 3.4, 9.8, 3.9, 9.5)
        if menu_choice == 3:
            print(track_menu)
            track_choice = int(input("Please choose an option: "))
            if track_choice == 1:
                players_track = Track_1("Suzuka", 3, 0, 8, 8)
            if track_choice == 2:
                players_track = Track_2("Fuji", 5, 8, 4, 3)
            if track_choice == 3:
                players_track = Track_3("Inagawa", 8, 5, 3, 5)
            if track_choice == 4:
                players_track = Track_4("Tsukuba", 9, 0, 7, 4)
        if menu_choice == 4:
            print(players_driver.stats())
            print(players_kart.stats())
            print(players_track.stats())
        if menu_choice == 5:
            game(players_driver, players_kart, players_track)
        if menu_choice == 6:
            exit_prompt = input("Are you sure you want to quit? All game data will be lost. (Y or N): ").upper()
            if exit_prompt == "Y":
                break
            elif exit_prompt == "N":
                pass
            else:
                print("That was not a valid choice. Try again. ")
                exit_prompt = input("Are you sure you want to quit? All game data will be lost. (Y or N): ").upper()

# GAME AND GAME FUNCTIONS BELOW HERE---------------------------------------------------------------

def print_player_ranks(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    return choice_string

def set_starting_line(players_driver, players_kart, players_track):

    #assign attributes to variables so the rest of this runs 
    players_driver_name = players_driver.name
    players_kart_name = players_kart.name
    players_track = players_track.name

    #lists all drivers and karts
    all_drivers = ["Veteran","Crafty","Cavalier","Joe"]
    all_karts = ["Standard","Mushmellow","Powerflower","Dry Bomber"]

    # these two functions create lists of the computer-controlled drivers and karts
    def create_new_driver_list(x):
        remaining_drivers = []
        for i in range(len(x)):
            if x[i] != players_driver_name:
                remaining_drivers.append(x[i])
        return(remaining_drivers)
    def create_new_karts_list(x):
        remaining_karts = []
        for i in range(len(x)):
            if x[i] != players_kart_name:
                remaining_karts.append(x[i])
        return(remaining_karts)
    remaining_drivers = create_new_driver_list(all_drivers)
    remaining_karts = create_new_karts_list(all_karts)

    #groups the player and computers 1-3 into dictionaries
    players = {
        "player": {
            players_kart_name: players_driver_name
        },
        "computer_1": {
            remaining_karts[0]: remaining_drivers[0]
        }, 
        "computer_2": {
            remaining_karts[1]: remaining_drivers[1]
        },
        "computer_3": {
            remaining_karts[2]: remaining_drivers[2]
        }}
    
    print("Starting Order:")
    starting_order = ["","","",""]
    for i in players:
        for j in players[i]:
            if j == "Dry Bomber":
                starting_order[0] = players[i][j]
            if j == "Mushmellow":
                starting_order[1] = players[i][j]
            if j == "Powerflower":
                starting_order[2] = players[i][j]
            if j == "Standard":
                starting_order[3] = players[i][j]
    print(print_player_ranks(starting_order))

    #prints the players dictionary nicely 
    def print_nested(val, nesting = -5): 
        if type(val) == dict: 
            print('') 
            nesting += 5 
            for k in val: 
                print(nesting * ' ', end='') 
                print(k, end=': ') 
                print_nested(val[k],nesting) 
        else: 
            print(val) 
    return players

def lap_events(laps): # add back players to pass in
    print("Lap %d!!" % laps)

def finish_line():
    print("""
    FINISH!!
    """)

def game(players_driver, players_kart, players_track):
    print("""
    Welcome to %s!! 
    """ % (players_track.name))
    set_starting_line(players_driver, players_kart, players_track)
    for laps in range(1, 4):
        if laps == 3:
            print("Final Lap!!!")
            lap_events(laps)
        else:
            lap_events(laps)
    finish_line()

game_startmenu()