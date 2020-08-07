from track_events import catastrophic, bad, neutral, good, catastrophic_first, bad_first, neutral_first, good_outcomes, bad_outcomes, neutral_outcomes, catastrophic_outcomes, go_around_track
import random

# player1 = Players(1)
# Computer1 = Players(2)
# Computer2 = Players(3)
# Computer3 = Players(4)
# Computers = [Computer1, Computer2, Computer1]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")

# GAME AND GAME FUNCTIONS BELOW HERE---------------------------------------------------------------

def print_player_ranks(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    return choice_string

def set_starting_line(players_driver, players_kart):
    #assign attributes to variables so the rest of this runs 
    players_driver_name = players_driver.name
    players_kart_name = players_kart.name
    # players_track = players_track.name

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

def set_finish_order():
    pass

# def change_ranks(player_rank_change, player1):
#     if player_rank_change == 1 and player1.rank <= 3:
#         player1.rank += 1
#     elif player_rank_change == 2 and player1.rank <=2:
#         player1.rank += 2
#     elif player_rank_change == -1 and player1.rank >= 2:
#         player1.rank -= 1
#     elif player_rank_change == -1 and player1.rank == 1:
#         player1.rank = 1
#     else:
#         pass
#     return player1.rank
#     print("You are now in rank: %d! Keep the pedal to the metal!" % player1.rank)

# def lap_events(laps, lap_count, player1): # add back players to pass in
#     if laps == lap_count:
#         print("Final Lap!!!")
#         go_around_track(player1)
#     else:
#         print("Lap %d!!" % laps)
#         go_around_track(player1)
        

# def finish_line():
#     print("\nFINISH!!\n")
#     print(finish_order)
#     if player1.rank == 1:
#         print("Congrats! You WON!!")
#     elif player1.rank == 2:
#         print("Second: Not great, not horrible")
#     elif player1.rank == 3:
#         print("Third: try harder")
#     elif player1.rank == 4:
#         print("Fourth ... oof.")
#     set_finish_order()