def set_starting_line():

    #assign attributes to variables so the rest of this runs 
    players_driver_name = "Veteran" #players_driver.name
    players_kart_name = "Mushmellow" #players_kart.name
    players_track = "Fuji" #players_track.name

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
    print(starting_order)

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
    #return print_nested(players),players

set_starting_line()