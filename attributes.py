
from drivers import Driver_1, Driver_2, Driver_3, Driver_4
from karts import Standard_kart, Mushmellow_kart, Powerflower_kart, Drybomber_kart, Kart
from tracks import Track_1, Track_2, Track_3, Track_4, Tracks
import track_events
from game import players_driver_name, players_kart_name, players, players_track

#attributes:

mushmellow_kart_speed = 5 - mushmellow_kart.speed 
mushmellow_kart_speed_bonus = -(mushmellow_kart_speed) * .2
mushmellow_kart_handling = 5 - mushmellow_kart.handling
mushmellow_kart_handling_bonus = -(mushmellow_kart_handling) * .2
# mushmellow_kart_drift = 5 - mushmellow_kart.drift
# mushmellow_kart_drift_bonus = -abs(mushmellow_kart_drift) * .2
drybomber_kart_speed = 5 - drybomber_kart.speed 
drybomber_kart_speed_bonus = -(drybomber_kart_speed) * .2
drybomber_kart_handling = 5 - drybomber_kart.handling
drybomber_kart_handling_bonus = -(drybomber_kart_handling) * .2
# drybomber_kart_drift = 5 - drybomber_kart.drift
# drybomber_kart_drift_bonus = -abs(drybomber_kart_drift) * .2
powerflower_kart_speed = 5 - powerflower_kart.speed 
powerflower_kart_speed_bonus = -(powerflower_kart_speed) * .2
powerflower_kart_handling = 5 - powerflower_kart.handling
powerflower_kart_handling_bonus = -(powerflower_kart_handling) * .2
# powerflower_kart_drift = 5 - mushmellow_kart.drift
# powerflower_kart_drift_bonus = -abs(powerflower_kart_drift) * .2
standard_kart_speed = 5 - standard_kart.speed 
standard_kart_speed_bonus = -(standard_kart_speed) * .2
standard_kart_handling = 5 - standard_kart.handling
standard_kart_handling_bonus = -(standard_kart_handling) * .2
#standard_kart_drift = 5 - standard_kart.drift
#standard_kart_drift_bonus = -abs(standard_kart_drift) * .2

driver_1_straight = 0
driver_1_all = 1
driver_1_turn = 0


driver_2_straight = -1
driver_2_all = 1
driver_2_turn = 1


driver_3_straight = 1
driver_3_all = -1
driver_3_turn = 0


driver_4_straight = 0
driver_4_all = 0
driver_4_turn = 0


track_1_speed = 5 - track_1.speed 
track_1_speed_bonus = -(track_1_speed) * .2
track_1_handling = 5 - track_1.handling
track_1_handling_bonus = -(track_1_handling) * .2

track_2_speed = 5 - track_1.speed 
track_2_speed_bonus = -(track_2_speed) * .2
track_2_handling = 5 - track_2.handling
track_2_handling_bonus = -(track_2_handling) * .2

track_3_speed = 5 - track_3.speed 
track_3_speed_bonus = -(track_3_speed) * .2
track_3_handling = 5 - track_3.handling
track_3_handling_bonus = -(track_3_handling) * .2

track_4_speed = 5 - track_4.speed 
track_4_speed_bonus = -(track_4_speed) * .2
track_4_handling = 5 - track_4.handling
track_4_handling_bonus = -(track_4_handling) * .2

from functools import reduce
def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)

print (deep_get(players, "player"))

def get_bonus_player(players):
    global player_kart_straight
    global player_kart_all
    global player_kart_turn
    player_kart_turn = 0
    player_kart_straight = 0
    player_kart_all = 0
    if "Powerflower" in deep_get(players, "player"):
        player_chosen_driver = deep_get(players, "player.Powerflower")
        if "Crafty" == player_chosen_driver:
            player_kart_turn = powerflower_kart_handling_bonus + driver_2_turn
            player_kart_straight = powerflower_kart_speed_bonus + driver_2_straight
            player_kart_all = driver_2_all
        elif "Veteran" == player_chosen_driver:
            player_kart_turn = powerflower_kart_handling_bonus + driver_1_turn
            player_kart_straight = powerflower_kart_speed_bonus + driver_1_straight
            player_kart_all = driver_1_all
        elif "Cavalier" == player_chosen_driver:
            player_kart_turn = powerflower_kart_handling_bonus + driver_3_turn
            player_kart_straight = powerflower_kart_speed_bonus + driver_3_straight
            player_kart_all = driver_3_all
        elif "Joe" == player_chosen_driver:
            player_kart_turn = powerflower_kart_handling_bonus + driver_4_turn
            player_kart_straight = powerflower_kart_speed_bonus + driver_4_straight
            player_kart_all = driver_4_all
    if "Mushmellow" in deep_get(players, "player"):
        player_chosen_driver = deep_get(players, "player.Mushmellow")
        if "Crafty" == player_chosen_driver:
            player_kart_turn = mushmellow_kart_handling_bonus + driver_2_turn
            player_kart_straight = mushmellow_kart_speed_bonus + driver_2_straight
            player_kart_all = driver_2_all
        elif "Veteran" == player_chosen_driver:
            player_kart_turn = mushmellow_kart_handling_bonus + driver_1_turn
            player_kart_straight = mushmellow_kart_speed_bonus + driver_1_straight
            player_kart_all = driver_1_all
        elif "Cavalier" == player_chosen_driver:
            player_kart_turn = mushmellow_kart_handling_bonus + driver_3_turn
            player_kart_straight = mushmellow_kart_speed_bonus + driver_3_straight
            player_kart_all = driver_3_all
        elif "Joe" == player_chosen_driver:
            player_kart_turn = mushmellow_kart_handling_bonus + driver_4_turn
            player_kart_straight = mushmellow_kart_speed_bonus + driver_4_straight
            player_kart_all = driver_4_all
    if "Dry Bomber" in deep_get(players, "player"):
        player_chosen_driver = deep_get(players, "player.Dry Bomber")
        if "Crafty" == player_chosen_driver:
            player_kart_turn = drybomber_kart_handling_bonus + driver_2_turn
            player_kart_straight = drybomber_kart_speed_bonus + driver_2_straight
            player_kart_all = driver_2_all
        elif "Veteran" == player_chosen_driver:
            player_kart_turn = drybomber_kart_handling_bonus  + driver_1_turn
            player_kart_straight = drybomber_kart_speed_bonus  + driver_1_straight
            player_kart_all = driver_1_all
        elif "Cavalier" == player_chosen_driver:
            player_kart_turn = drybomber_kart_handling_bonus + driver_3_turn
            player_kart_straight = drybomber_kart_speed_bonus  + driver_3_straight
            player_kart_all = driver_3_all
        elif "Joe" == player_chosen_driver:
            player_kart_turn = drybomber_kart_handling_bonus + driver_4_turn
            player_kart_straight = drybomber_kart_speed_bonus  + driver_4_straight
            player_kart_all = driver_4_all
    if "Standard" in deep_get(players, "player"):
        player_chosen_driver = deep_get(players, "player.Standard")
        if "Crafty" == player_chosen_driver:
            player_kart_turn = standard_kart_handling_bonus + driver_2_turn
            player_kart_straight = standard_kart_speed_bonus + driver_2_straight
            player_kart_all = driver_2_all
        elif "Veteran" == player_chosen_driver:
            player_kart_turn = standard_kart_handling_bonus   + driver_1_turn
            player_kart_straight = standard_kart_speed_bonus  + driver_1_straight
            player_kart_all = driver_1_all
        elif "Cavalier" == player_chosen_driver:
            player_kart_turn = standard_kart_handling_bonus + driver_3_turn
            player_kart_straight = standard_kart_speed_bonus  + driver_3_straight
            player_kart_all = driver_3_all
        elif "Joe" == player_chosen_driver:
            player_kart_turn = standard_kart_handling_bonus + driver_4_turn
            player_kart_straight = standard_kart_speed_bonus  + driver_4_straight
            player_kart_all = driver_4_all
    return player_kart_straight, player_kart_all, player_kart_turn
get_bonus_player(players)
def get_bonus_computer_1(players):
    global comp1_kart_straight
    global comp1_kart_all
    global comp1_kart_turn
    comp1_kart_turn = 0
    comp1_kart_straight = 0
    comp1_kart_all = 0
    if "Powerflower" in deep_get(players, "computer_1"):
        comp1_chosen_driver = deep_get(players, "computer_1.Powerflower")
        if "Crafty" == computer_1_chosen_driver:
            comp1_kart_turn = powerflower_kart_handling_bonus + driver_2_turn
            comp1_kart_straight = powerflower_kart_speed_bonus + driver_2_straight
            comp1_kart_all = driver_2_all
        elif "Veteran" == comp1_chosen_driver:
            comp1_kart_turn = powerflower_kart_handling_bonus + driver_1_turn
            comp1_kart_straight = powerflower_kart_speed_bonus + driver_1_straight
            comp1_kart_all = driver_1_all
        elif "Cavalier" == comp1_chosen_driver:
            comp1_kart_turn = powerflower_kart_handling_bonus + driver_3_turn
            comp1_kart_straight = powerflower_kart_speed_bonus + driver_3_straight
            comp1_kart_all = driver_3_all
        elif "Joe" == comp1_chosen_driver:
            comp1_kart_turn = powerflower_kart_handling_bonus + driver_4_turn
            comp1_kart_straight = powerflower_kart_speed_bonus + driver_4_straight
            comp1_kart_all = driver_4_all
    if "Mushmellow" in deep_get(players, "computer_1"):
        comp1_chosen_driver = deep_get(players, "computer_1.Mushmellow")
        if "Crafty" == comp1_chosen_driver:
            comp1_kart_turn = mushmellow_kart_handling_bonus + driver_2_turn
            comp1_kart_straight = mushmellow_kart_speed_bonus + driver_2_straight
            comp1_kart_all = driver_2_all
        elif "Veteran" == comp1_chosen_driver:
            comp1_kart_turn = mushmellow_kart_handling_bonus + driver_1_turn
            comp1_kart_straight = mushmellow_kart_speed_bonus + driver_1_straight
            comp1_kart_all = driver_1_all
        elif "Cavalier" == comp1_chosen_driver:
            comp1_kart_turn = mushmellow_kart_handling_bonus + driver_3_turn
            comp1_kart_straight = mushmellow_kart_speed_bonus + driver_3_straight
            comp1_kart_all = driver_3_all
        elif "Joe" == comp1_chosen_driver:
            comp1_kart_turn = mushmellow_kart_handling_bonus + driver_4_turn
            comp1_kart_straight = mushmellow_kart_speed_bonus + driver_4_straight
            comp1_kart_all = driver_4_all
    if "Dry Bomber" in deep_get(players, "computer_1"):
        comp1_chosen_driver = deep_get(players, "computer_1.Dry Bomber")
        if "Crafty" == comp1_chosen_driver:
            comp1_kart_turn = drybomber_kart_handling_bonus + driver_2_turn
            comp1_kart_straight = drybomber_kart_speed_bonus + driver_2_straight
            comp1_kart_all = driver_2_all
        elif "Veteran" == comp1_chosen_driver:
            comp1_kart_turn = drybomber_kart_handling_bonus  + driver_1_turn
            comp1_kart_straight = drybomber_kart_speed_bonus  + driver_1_straight
            comp1_kart_all = driver_1_all
        elif "Cavalier" == comp1_chosen_driver:
            comp1_kart_turn = drybomber_kart_handling_bonus + driver_3_turn
            comp1_kart_straight = drybomber_kart_speed_bonus  + driver_3_straight
            comp1_kart_all = driver_3_all
        elif "Joe" == comp1_chosen_driver:
            comp1_kart_turn = drybomber_kart_handling_bonus + driver_4_turn
            comp1_kart_straight = drybomber_kart_speed_bonus  + driver_4_straight
            comp1_kart_all = driver_4_all
    if "Standard" in deep_get(players, "computer_1"):
        comp1_chosen_driver = deep_get(players, "computer_1.Standard")
        if "Crafty" == comp1_chosen_driver:
            comp1_kart_turn = standard_kart_handling_bonus + driver_2_turn
            comp1_kart_straight = standard_kart_speed_bonus + driver_2_straight
            comp1_kart_all = driver_2_all
        elif "Veteran" == comp1_chosen_driver:
            comp1_kart_turn = standard_kart_handling_bonus   + driver_1_turn
            comp1_kart_straight = standard_kart_speed_bonus  + driver_1_straight
            comp1_kart_all = driver_1_all
        elif "Cavalier" == comp1_chosen_driver:
            comp1_kart_turn = standard_kart_handling_bonus + driver_3_turn
            comp1_kart_straight = standard_kart_speed_bonus  + driver_3_straight
            comp1_kart_all = driver_3_all
        elif "Joe" == comp1_chosen_driver:
            comp1_kart_turn = standard_kart_handling_bonus + driver_4_turn
            comp1_kart_straight = standard_kart_speed_bonus  + driver_4_straight
            comp1_kart_all = driver_4_all
    return comp1_kart_straight, comp1_kart_all, comp1_kart_turn
get_bonus_computer_1(players)
def get_bonus_computer_2(players):
    global comp2_kart_straight
    global comp2_kart_all
    global comp2_kart_turn
    comp2_kart_turn = 0
    comp2_kart_straight = 0
    comp2_kart_all = 0
    if "Powerflower" in deep_get(players, "computer_2"):
        comp2_chosen_driver = deep_get(players, "computer_2.Powerflower")
        if "Crafty" == computer_2_chosen_driver:
            comp2_kart_turn = powerflower_kart_handling_bonus + driver_2_turn
            comp2_kart_straight = powerflower_kart_speed_bonus + driver_2_straight
            comp2_kart_all = driver_2_all
        elif "Veteran" == comp2_chosen_driver:
            comp2_kart_turn = powerflower_kart_handling_bonus + driver_1_turn
            comp2_kart_straight = powerflower_kart_speed_bonus + driver_1_straight
            comp2_kart_all = driver_1_all
        elif "Cavalier" == comp2_chosen_driver:
            comp2_kart_turn = powerflower_kart_handling_bonus + driver_3_turn
            comp2_kart_straight = powerflower_kart_speed_bonus + driver_3_straight
            comp2_kart_all = driver_3_all
        elif "Joe" == comp2_chosen_driver:
            comp2_kart_turn = powerflower_kart_handling_bonus + driver_4_turn
            comp2_kart_straight = powerflower_kart_speed_bonus + driver_4_straight
            comp2_kart_all = driver_4_all
    if "Mushmellow" in deep_get(players, "computer_2"):
        comp2_chosen_driver = deep_get(players, "computer_2.Mushmellow")
        if "Crafty" == comp2_chosen_driver:
            comp2_kart_turn = mushmellow_kart_handling_bonus + driver_2_turn
            comp2_kart_straight = mushmellow_kart_speed_bonus + driver_2_straight
            comp2_kart_all = driver_2_all
        elif "Veteran" == comp2_chosen_driver:
            comp2_kart_turn = mushmellow_kart_handling_bonus + driver_1_turn
            comp2_kart_straight = mushmellow_kart_speed_bonus + driver_1_straight
            comp2_kart_all = driver_1_all
        elif "Cavalier" == comp2_chosen_driver:
            comp2_kart_turn = mushmellow_kart_handling_bonus + driver_3_turn
            comp2_kart_straight = mushmellow_kart_speed_bonus + driver_3_straight
            comp2_kart_all = driver_3_all
        elif "Joe" == comp2_chosen_driver:
            comp2_kart_turn = mushmellow_kart_handling_bonus + driver_4_turn
            comp2_kart_straight = mushmellow_kart_speed_bonus + driver_4_straight
            comp2_kart_all = driver_4_all
    if "Dry Bomber" in deep_get(players, "computer_2"):
        comp2_chosen_driver = deep_get(players, "computer_2.Dry Bomber")
        if "Crafty" == comp2_chosen_driver:
            comp2_kart_turn = drybomber_kart_handling_bonus + driver_2_turn
            comp2_kart_straight = drybomber_kart_speed_bonus + driver_2_straight
            comp2_kart_all = driver_2_all
        elif "Veteran" == comp2_chosen_driver:
            comp2_kart_turn = drybomber_kart_handling_bonus  + driver_1_turn
            comp2_kart_straight = drybomber_kart_speed_bonus  + driver_1_straight
            comp2_kart_all = driver_1_all
        elif "Cavalier" == comp2_chosen_driver:
            comp2_kart_turn = drybomber_kart_handling_bonus + driver_3_turn
            comp2_kart_straight = drybomber_kart_speed_bonus  + driver_3_straight
            comp2_kart_all = driver_3_all
        elif "Joe" == comp2_chosen_driver:
            comp2_kart_turn = drybomber_kart_handling_bonus + driver_4_turn
            comp2_kart_straight = drybomber_kart_speed_bonus  + driver_4_straight
            comp2_kart_all = driver_4_all
    if "Standard" in deep_get(players, "computer_2"):
        comp2_chosen_driver = deep_get(players, "computer_2.Standard")
        if "Crafty" == comp2_chosen_driver:
            comp2_kart_turn = standard_kart_handling_bonus + driver_2_turn
            comp2_kart_straight = standard_kart_speed_bonus + driver_2_straight
            comp2_kart_all = driver_2_all
        elif "Veteran" == comp2_chosen_driver:
            comp2_kart_turn = standard_kart_handling_bonus   + driver_1_turn
            comp2_kart_straight = standard_kart_speed_bonus  + driver_1_straight
            comp2_kart_all = driver_1_all
        elif "Cavalier" == comp2_chosen_driver:
            comp2_kart_turn = standard_kart_handling_bonus + driver_3_turn
            comp2_kart_straight = standard_kart_speed_bonus  + driver_3_straight
            comp2_kart_all = driver_3_all
        elif "Joe" == comp2_chosen_driver:
            comp2_kart_turn = standard_kart_handling_bonus + driver_4_turn
            comp2_kart_straight = standard_kart_speed_bonus  + driver_4_straight
            comp2_kart_all = driver_4_all
    return comp2_kart_straight, comp2_kart_all, comp2_kart_turn
get_bonus_computer_2(players)
def get_bonus_computer_3(players):
    global comp3_kart_straight
    global comp3_kart_all
    global comp3_kart_turn
    comp3_kart_turn = 0
    comp3_kart_straight = 0
    comp3_kart_all = 0
    if "Powerflower" in deep_get(players, "computer_3"):
        comp3_chosen_driver = deep_get(players, "computer_3.Powerflower")
        if "Crafty" == computer_3_chosen_driver:
            comp3_kart_turn = powerflower_kart_handling_bonus + driver_2_turn
            comp3_kart_straight = powerflower_kart_speed_bonus + driver_2_straight
            comp3_kart_all = driver_2_all
        elif "Veteran" == comp3_chosen_driver:
            comp3_kart_turn = powerflower_kart_handling_bonus + driver_1_turn
            comp3_kart_straight = powerflower_kart_speed_bonus + driver_1_straight
            comp3_kart_all = driver_1_all
        elif "Cavalier" == comp3_chosen_driver:
            comp3_kart_turn = powerflower_kart_handling_bonus + driver_3_turn
            comp3_kart_straight = powerflower_kart_speed_bonus + driver_3_straight
            comp3_kart_all = driver_3_all
        elif "Joe" == comp3_chosen_driver:
            comp3_kart_turn = powerflower_kart_handling_bonus + driver_4_turn
            comp3_kart_straight = powerflower_kart_speed_bonus + driver_4_straight
            comp3_kart_all = driver_4_all
    if "Mushmellow" in deep_get(players, "computer_3"):
        comp3_chosen_driver = deep_get(players, "computer_3.Mushmellow")
        if "Crafty" == comp3_chosen_driver:
            comp3_kart_turn = mushmellow_kart_handling_bonus + driver_2_turn
            comp3_kart_straight = mushmellow_kart_speed_bonus + driver_2_straight
            comp3_kart_all = driver_2_all
        elif "Veteran" == comp3_chosen_driver:
            comp3_kart_turn = mushmellow_kart_handling_bonus + driver_1_turn
            comp3_kart_straight = mushmellow_kart_speed_bonus + driver_1_straight
            comp3_kart_all = driver_1_all
        elif "Cavalier" == comp3_chosen_driver:
            comp3_kart_turn = mushmellow_kart_handling_bonus + driver_3_turn
            comp3_kart_straight = mushmellow_kart_speed_bonus + driver_3_straight
            comp3_kart_all = driver_3_all
        elif "Joe" == comp3_chosen_driver:
            comp3_kart_turn = mushmellow_kart_handling_bonus + driver_4_turn
            comp3_kart_straight = mushmellow_kart_speed_bonus + driver_4_straight
            comp3_kart_all = driver_4_all
    if "Dry Bomber" in deep_get(players, "computer_3"):
        comp3_chosen_driver = deep_get(players, "computer_3.Dry Bomber")
        if "Crafty" == comp3_chosen_driver:
            comp3_kart_turn = drybomber_kart_handling_bonus + driver_2_turn
            comp3_kart_straight = drybomber_kart_speed_bonus + driver_2_straight
            comp3_kart_all = driver_2_all
        elif "Veteran" == comp3_chosen_driver:
            comp3_kart_turn = drybomber_kart_handling_bonus  + driver_1_turn
            comp3_kart_straight = drybomber_kart_speed_bonus  + driver_1_straight
            comp3_kart_all = driver_1_all
        elif "Cavalier" == comp3_chosen_driver:
            comp3_kart_turn = drybomber_kart_handling_bonus + driver_3_turn
            comp3_kart_straight = drybomber_kart_speed_bonus  + driver_3_straight
            comp3_kart_all = driver_3_all
        elif "Joe" == comp3_chosen_driver:
            comp3_kart_turn = drybomber_kart_handling_bonus + driver_4_turn
            comp3_kart_straight = drybomber_kart_speed_bonus  + driver_4_straight
            comp3_kart_all = driver_4_all
    if "Standard" in deep_get(players, "computer_3"):
        comp3_chosen_driver = deep_get(players, "computer_3.Standard")
        if "Crafty" == comp3_chosen_driver:
            comp3_kart_turn = standard_kart_handling_bonus + driver_2_turn
            comp3_kart_straight = standard_kart_speed_bonus + driver_2_straight
            comp3_kart_all = driver_2_all
        elif "Veteran" == comp3_chosen_driver:
            comp3_kart_turn = standard_kart_handling_bonus   + driver_1_turn
            comp3_kart_straight = standard_kart_speed_bonus  + driver_1_straight
            comp3_kart_all = driver_1_all
        elif "Cavalier" == comp3_chosen_driver:
            comp3_kart_turn = standard_kart_handling_bonus + driver_3_turn
            comp3_kart_straight = standard_kart_speed_bonus  + driver_3_straight
            comp3_kart_all = driver_3_all
        elif "Joe" == comp3_chosen_driver:
            comp3_kart_turn = standard_kart_handling_bonus + driver_4_turn
            comp3_kart_straight = standard_kart_speed_bonus  + driver_4_straight
            comp3_kart_all = driver_4_all
    return comp3_kart_straight, comp3_kart_all, comp3_kart_turn
get_bonus_computer_3(players)