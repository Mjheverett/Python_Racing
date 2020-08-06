from drivers import Driver_1, Driver_2, Driver_3, Driver_4
from karts import Standard_kart, Mushmellow_kart, Powerflower_kart, Drybomber_kart, Kart
from tracks import Track_1, Track_2, Track_3, Track_4, Tracks
from game import players_driver_name, players_kart_name, players, players_track


##Track 1##---------------------------------------------------------------

def track_1_turn_agg(probability):
    if 1 <= probability <= 4:
        change_in_places = -1
    if 5 <= probability <= 12:
        change_in_places = 0
    if 13 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places

def track_1_turn_pass(probability):
    if 1 <= probability <= 4:
        change_in_places = -1
    if 5 <= probability <= 14:
        change_in_places = 0
    if 15 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print(".")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places

def track_1_straight_agg(probability):
    if 1 <= probability <= 4:
        change_in_places = -1
    if 5 <= probability <= 12:
        change_in_places = 0
    if 13 <= probability <= 20:
        change_in_places = +1

#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    #Bad_event
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
    #Nutral_event
    elif probability == 5:
        print("stayed in current spot")
    elif probability == 6:
        print("stayed in current spot")
    #Positive_Event
    elif probability == 7:
        print("")
    elif probability == 8:
        print("you advanced one spot")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot")
    return change_in_places

def track_1_straight_pass(probability):
    if 1 <= probability <= 4:
        change_in_places = -1
    if 5 <= probability <= 14:
        change_in_places = 0
    if 15 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
#Nutral_event
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places


def track_1_in_first(probability):
    if 1 <= probability <= 4:
        change_in_places = -1
    if 5 <= probability <= 20:
        change_in_places = 0
#Bad_event
    if probability == 1:
        print("lost two spots")
    elif probability == 2:
        print("lost two spots")
#Nutral_event
    elif probability == 3:
        print("lost one spot")
    elif probability == 4:
        print("lost one spot")
    elif probability == 5:
        print("stayed in current spot")
    elif probability == 6:
        print("stayed in current spot")
    elif probability == 7:
        print("stayed in current spot")
    elif probability == 8:
        print("stayed in current spot")
    elif probability == 9:
        print("stayed in current spot")
    elif probability == 10:
        print("stayed in current spot")
    elif probability == 11:
        print("stayed in current spot")
    elif probability == 12:
        print("stayed in current spot")
    elif probability == 13:
        print("stayed in current spot")
    elif probability == 14:
        print("stayed in current spot")
    elif probability == 15:
        print("stayed in current spot")
    elif probability == 16:
        print("stayed in current spot")
    elif probability == 17:
        print("stayed in current spot")
    elif probability == 18:
        print("stayed in current spot")
    elif probability == 19:
        print("stayed in current spot")
    elif probability == 20:
        print("stayed in current spot")
    return change_in_places


##Track 2##---------------------------------------------------------------

def track_2_turn_agg(probability):
    if 1 <= probability <= 6:
        change_in_places = -1
    if 7 <= probability <= 12:
        change_in_places = 0
    if 13 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("Y")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places

def track_2_turn_pass(probability):
    if 1 <= probability <= 6:
        change_in_places = -1
    if 7 <= probability <= 14:
        change_in_places = 0
    if 15 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print(".")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places

def track_2_straight_agg(probability):
    if 1 <= probability <= 6:
        change_in_places = -1
    if 7 <= probability <= 12:
        change_in_places = 0
    if 13 <= probability <= 20:
        change_in_places = +1

#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    #Bad_event
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
    #Nutral_event
    elif probability == 5:
        print("stayed in current spot")
    elif probability == 6:
        print("stayed in current spot")
    #Positive_Event
    elif probability == 7:
        print("")
    elif probability == 8:
        print("you advanced one spot")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot")
    return change_in_places

def track_2_straight_pass(probability):
    if 1 <= probability <= 6:
        change_in_places = -1
    if 7 <= probability <= 14:
        change_in_places = 0
    if 15 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places


def track_2_in_first(probability):
    if 1 <= probability <= 6:
        change_in_places = -1
    if 7 <= probability <= 20:
        change_in_places = +0
#Bad_event
    if probability == 1:
        print("lost two spots")
    elif probability == 2:
        print("lost two spots")
    #Bad_event
    elif probability == 3:
        print("lost one spot")
    elif probability == 4:
        print("lost one spot")
    #Nutral_event
    elif probability == 5:
        print("stayed in current spot")
    elif probability == 6:
        print("stayed in current spot")
    elif probability == 7:
        print("stayed in current spot")
    elif probability == 8:
        print("stayed in current spot")
    elif probability == 9:
        print("stayed in current spot")
    elif probability == 10:
        print("stayed in current spot")
    elif probability == 11:
        print("stayed in current spot")
    elif probability == 12:
        print("stayed in current spot")
    elif probability == 13:
        print("stayed in current spot")
    elif probability == 14:
        print("stayed in current spot")
    elif probability == 15:
        print("stayed in current spot")
    elif probability == 16:
        print("stayed in current spot")
    elif probability == 17:
        print("stayed in current spot")
    elif probability == 18:
        print("stayed in current spot")
    elif probability == 19:
        print("stayed in current spot")
    elif probability == 20:
        print("stayed in current spot")
    return change_in_places


##Track 3##---------------------------------------------------------------

def track_3_turn_agg(probability):
    if 1 <= probability <= 3:
        change_in_places = -2
    if 4 <= probability <= 8:
        change_in_places = -1
    if 9 <= probability <= 14:
        change_in_places = 0
    if 15 <= probability <= 20:
        change_in_places = +1
#Catastrophic_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places

def track_3_turn_pass(probability):
    if 1 <= probability <= 3:
        change_in_places = -2
    if 4 <= probability <= 6:
        change_in_places = -1
    if 7 <= probability <= 14:
        change_in_places = 0
    if 15 <= probability <= 20:
        change_in_places = +1
#Catastrophic_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print(".")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places

def track_3_straight_agg(probability):
    if 1 <= probability <= 3:
        change_in_places = -2
    if 4 <= probability <= 8:
        change_in_places = -1
    if 9 <= probability <= 14:
        change_in_places = 0
    if 15 <= probability <= 20:
        change_in_places = +1

#Catastrophic_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    #Bad_event
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
    #Nutral_event
    elif probability == 5:
        print("stayed in current spot")
    elif probability == 6:
        print("stayed in current spot")
    #Positive_Event
    elif probability == 7:
        print("")
    elif probability == 8:
        print("you advanced one spot")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot")
    return change_in_places

def track_3_straight_pass(probability):
    if 1 <= probability <= 3:
        change_in_places = -2
    if 4 <= probability <= 6:
        change_in_places = -1
    if 7 <= probability <= 14:
        change_in_places = 0
    if 15 <= probability <= 20:
        change_in_places = +1

#Catastrophic_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places


def track_3_in_first(probability):
    if 1 <= probability <= 3:
        change_in_places = -2
    if 4 <= probability <= 6:
        change_in_places = -1
    if 7 <= probability <= 20:
        change_in_places = 0

#Catastrophic_event
    if probability == 1:
        print("lost two spots")
    elif probability == 2:
        print("lost two spots")
    #Bad_event
    elif probability == 3:
        print("lost one spot")
    elif probability == 4:
        print("lost one spot")
    #Nutral_event
    elif probability == 5:
        print("stayed in current spot")
    elif probability == 6:
        print("stayed in current spot")
    elif probability == 7:
        print("stayed in current spot")
    elif probability == 8:
        print("stayed in current spot")
    elif probability == 9:
        print("stayed in current spot")
    elif probability == 10:
        print("stayed in current spot")
    elif probability == 11:
        print("stayed in current spot")
    elif probability == 12:
        print("stayed in current spot")
    elif probability == 13:
        print("stayed in current spot")
    elif probability == 14:
        print("stayed in current spot")
    elif probability == 15:
        print("stayed in current spot")
    elif probability == 16:
        print("stayed in current spot")
    elif probability == 17:
        print("stayed in current spot")
    elif probability == 18:
        print("stayed in current spot")
    elif probability == 19:
        print("stayed in current spot")
    elif probability == 20:
        print("stayed in current spot")
    return change_in_places


##Track 4##---------------------------------------------------------------

def track_4_turn_agg(probability):
    if 1 <= probability <= 5:
        change_in_places = -2
    if 6 <= probability <= 11:
        change_in_places = -1
    if 12 <= probability <= 17:
        change_in_places = 0
    if 18 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places

def track_4_turn_pass(probability):
    if 1 <= probability <= 4:
        change_in_places = -2
    if 5 <= probability <= 8:
        change_in_places = -1
    if 9 <= probability <= 17:
        change_in_places = 0
    if 18 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places

def track_4_straight_agg(probability):
    if 1 <= probability <= 5:
        change_in_places = -2
    if 6 <= probability <= 11:
        change_in_places = -1
    if 12 <= probability <= 17:
        change_in_places = 0
    if 18 <= probability <= 20:
        change_in_places = +1

    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    #Bad_event
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
    #Nutral_event
    elif probability == 5:
        print("stayed in current spot")
    elif probability == 6:
        print("stayed in current spot")
    #Positive_Event
    elif probability == 7:
        print("")
    elif probability == 8:
        print("you advanced one spot")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot")
    return change_in_places

def track_4_straight_pass(probability):
    if 1 <= probability <= 4:
        change_in_places = -2
    if 5 <= probability <= 8:
        change_in_places = -1
    if 9 <= probability <= 17:
        change_in_places = 0
    if 18 <= probability <= 20:
        change_in_places = +1
#Bad_event
    if probability == 1:
        print("")
    elif probability == 2:
        print("")
    elif probability == 3:
        print("")
    elif probability == 4:
        print("")
#Nutral_event
    elif probability == 5:
        print("")
    elif probability == 6:
        print("")
    elif probability == 7:
        print("")
    elif probability == 8:
        print("")
    elif probability == 9:
        print("you advanced one spot")
    elif probability == 10:
        print("you advanced one spot")
    elif probability == 11:
        print("you advanced one spot")
    elif probability == 12:
        print("you advanced one spot")
#Positive_Event
    elif probability == 13:
        print("you advanced one spot")
    elif probability == 14:
        print("you advanced one spot")
    elif probability == 15:
        print("you advanced one spot")
    elif probability == 16:
        print("you advanced one spot")
    elif probability == 17:
        print("you advanced one spot")
    elif probability == 18:
        print("you advanced one spot")
    elif probability == 19:
        print("you advanced one spot")
    elif probability == 20:
        print("you advanced one spot") 
    return change_in_places


def track_4_in_first(probability):
    if 1 <= probability <= 5:
        change_in_places = -2
    if 6 <= probability <= 11:
        change_in_places = -1
    if 11 <= probability <= 20:
        change_in_places = 0
#Catastrophic_event
    if probability == 1:
        print("lost two spots")
    elif probability == 2:
        print("lost two spots")
    #Bad_event
    elif probability == 3:
        print("lost one spot")
    elif probability == 4:
        print("lost one spot")
    #Nutral_event
    elif probability == 5:
        print("stayed in current spot")
    elif probability == 6:
        print("stayed in current spot")
    elif probability == 7:
        print("stayed in current spot")
    elif probability == 8:
        print("stayed in current spot")
    elif probability == 9:
        print("stayed in current spot")
    elif probability == 10:
        print("stayed in current spot")
    elif probability == 11:
        print("stayed in current spot")
    elif probability == 12:
        print("stayed in current spot")
    elif probability == 13:
        print("stayed in current spot")
    elif probability == 14:
        print("stayed in current spot")
    elif probability == 15:
        print("stayed in current spot")
    elif probability == 16:
        print("stayed in current spot")
    elif probability == 17:
        print("stayed in current spot")
    elif probability == 18:
        print("stayed in current spot")
    elif probability == 19:
        print("stayed in current spot")
    elif probability == 20:
        print("stayed in current spot")
    return change_in_places

def track_1_turn_player(): 
    print("As you round the turn, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
    #ask for user input if they want to be aggressive or passive
    user_input = input()
    #if they choose aggressive
    if user_input == "1":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_turn + track_1_handling_bonus + player_kart_all
        change_in_places_player = track_1_turn_agg(probability)
    #if they choose passive
    elif user_input == "2":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_turn + track_1_handling_bonus + player_kart_all 
        change_in_places_player = track_1_turn_pass(probability)
    else:
        #if they press something other than 1 or 2
        print("Please only enter the number one (1) or the number two (2).")
    #run computers through the event
def track_1_turn_computer():
    #decide whether they are aggressive (1) or passive (2)
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_1_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_1_handling_bonus
    return change_in_places_comp1
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_1_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_1_handling_bonus
    return change_in_places_comp2
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_1_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_1_handling_bonus
    return change_in_places_comp3
def track_1_straight_player(): 
    print("As you near the straight section of the track, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
    #ask for user input if they want to be aggressive or passive
    user_input = input()
    #if they choose aggressive
    if user_input == "1":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_straight + track_1_speed_bonus + player_kart_all
        change_in_places_player = track_1_straight_agg(probability)
    #if they choose passive
    elif user_input == "2":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_straight + track_1_speed_bonus + player_kart_all
        change_in_places_player = track_1_straight_pass(probability)
    else:
        #if they press something other than 1 or 2
        print("Please only enter the number one (1) or the number two (2).")
    #run computers through the event
def track_1_straight_computer():
    #decide whether they are aggressive (1) or passive (2)
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_straight + comp1_all + track_1_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_straight + comp1_all + track_1_speed_bonus
    return change_in_places_comp1
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_straight + comp2_all + track_1_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_straight + comp2_all + track_1_speed_bonus
    return change_in_places_comp2
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_straight + comp3_all + track_1_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_straight + comp3_all + track_1_speed_bonus
    return change_in_places_comp3
def track_2_turn_player():
    print("As you round the turn, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
    #ask for user input if they want to be aggressive or passive
    user_input = input()
    #if they choose aggressive
    if user_input == "1":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_turn + track_2_handling_bonus + player_kart_all
        change_in_places_player = track_2_turn_agg(probability)
    #if they choose passive
    elif user_input == "2":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_turn + track_2_handling_bonus + player_kart_all 
        change_in_places_player = track_2_turn_pass(probability)
    else:
        #if they press something other than 1 or 2
        print("Please only enter the number one (1) or the number two (2).")
    #run computers through the event
def track_2_turn_computer():
    #decide whether they are aggressive (1) or passive (2)
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_2_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_2_handling_bonus
    return change_in_places_comp1
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_2_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_2_handling_bonus
    return change_in_places_comp2
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_2_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_2_handling_bonus
    return change_in_places_comp3
def track_2_straight_player():
    print("As you near the straight section of the track, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
    #ask for user input if they want to be aggressive or passive
    user_input = input()
    #if they choose aggressive
    if user_input == "1":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_straight + track_2_speed_bonus + player_kart_all
        change_in_places_player = track_2_straight_agg(probability)
    #if they choose passive
    elif user_input == "2":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_straight + track_2_speed_bonus + player_kart_all
        change_in_places_player = track_2_straight_pass(probability)
    else:
        #if they press something other than 1 or 2
        print("Please only enter the number one (1) or the number two (2).")
    #run computers through the event
def track_2_straight_computer():
    #decide whether they are aggressive (1) or passive (2)
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_2_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_2_speed_bonus
    return change_in_places_comp1
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_2_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_2_speed_bonus
    return change_in_places_comp2
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_2_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_2_speed_bonus
    return change_in_places_comp3
def track_3_turn_player():
    print("As you round the turn, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
    #ask for user input if they want to be aggressive or passive
    user_input = input()
    #if they choose aggressive
    if user_input == "1":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_turn + track_3_handling_bonus + player_kart_all
        change_in_places_player = track_3_turn_agg(probability)
    #if they choose passive
    elif user_input == "2":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_turn + track_3_handling_bonus + player_kart_all 
        change_in_places_player = track_3_turn_pass(probability)
    else:
        #if they press something other than 1 or 2
        print("Please only enter the number one (1) or the number two (2).")
def track_3_turn_computer():
    #decide whether they are aggressive (1) or passive (2)
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_3_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_3_handling_bonus
    return change_in_places_comp1
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_3_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_3_handling_bonus
    return change_in_places_comp2
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_3_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_3_handling_bonus
    return change_in_places_comp3
def track_3_straight_player():
    print("As you near the straight section of the track, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
    #ask for user input if they want to be aggressive or passive
    user_input = input()
    #if they choose aggressive
    if user_input == "1":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_straight + track_3_speed_bonus + player_kart_all
        change_in_places_player = track_1_straight_agg(probability)
    #if they choose passive
    elif user_input == "2":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_straight + track_3_speed_bonus + player_kart_all
        change_in_places_player = track_1_straight_pass(probability)
    else:
        #if they press something other than 1 or 2
        print("Please only enter the number one (1) or the number two (2).")
    #run computers through the event
def track_3_straight_computer():
    #decide whether they are aggressive (1) or passive (2)
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_3_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_3_speed_bonus
    return change_in_places_comp1
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_3_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_3_speed_bonus
    return change_in_places_comp2
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_3_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_3_speed_bonus
    return change_in_places_comp3
def track_4_turn_player():
    print("As you round the turn, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
    #ask for user input if they want to be aggressive or passive
    user_input = input()
    #if they choose aggressive
    if user_input == "1":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_turn + track_4_handling_bonus + player_kart_all
        change_in_places_player = track_4_turn_agg(probability)
    #if they choose passive
    elif user_input == "2":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_turn + track_4_handling_bonus + player_kart_all 
        change_in_places_player = track_4_turn_pass(probability)
    else:
        #if they press something other than 1 or 2
        print("Please only enter the number one (1) or the number two (2).")
    #run computers through the event
def track_4_turn_computer():
    #decide whether they are aggressive (1) or passive (2)
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_4_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_turn + comp1_all + track_4_handling_bonus
    return change_in_places_comp1
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_4_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_turn + comp2_all + track_4_handling_bonus
    return change_in_places_comp2
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_4_handling_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_turn + comp3_all + track_4_handling_bonus
    return change_in_places_comp3
def track_4_straight_player():
    print("As you near the straight section of the track, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
    #ask for user input if they want to be aggressive or passive
    user_input = input()
    #if they choose aggressive
    if user_input == "1":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_straight + track_1_speed_bonus + player_kart_all
        change_in_places_player = track_1_straight_agg(probability)
    #if they choose passive
    elif user_input == "2":
        base_probability = randint.range(1, 20)
        probability = base_probability + player_kart_straight + track_1_speed_bonus + player_kart_all
        change_in_places_player = track_1_straight_pass(probability)
    else:
        #if they press something other than 1 or 2
        print("Please only enter the number one (1) or the number two (2).")
    #run computers through the event
def track_4_straight_computer():
    #decide whether they are aggressive (1) or passive (2)
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_straight + comp1_all + track_1_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp1_kart_straight + comp1_all + track_1_speed_bonus
    return change_in_places_comp1
    agg_pass = randint.range(1,3)
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_straight + comp2_all + track_1_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp2_kart_straight + comp2_all + track_1_speed_bonus
    return change_in_places_comp2
    if agg_pass == 1:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_straight + comp3_all + track_1_speed_bonus
    if agg_pass == 2:
        base_probability = randint.range(1, 20)
        probability = base_probability + comp3_kart_straight + comp3_all + track_1_speed_bonus
    return change_in_places_comp3