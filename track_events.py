# from drivers import Driver_1, Driver_2, Driver_3, Driver_4
# from karts import Standard_kart, Mushmellow_kart, Powerflower_kart, Drybomber_kart, Kart
# from tracks import Track_1, Track_2, Track_3, Track_4, Tracks
# from game import players_driver_name, players_kart_name, players, players_track


##Track 1##---------------------------------------------------------------

import random

def change_ranks(player_rank_change, player1):
    if player_rank_change == 1 and player1.rank <= 3:
        player1.rank += 1
    elif player_rank_change == 2 and player1.rank <=2:
        player1.rank += 2
    elif player_rank_change == -1 and player1.rank >= 2:
        player1.rank -= 1
    elif player_rank_change == -1 and player1.rank == 1:
        player1.rank = 1
    else:
        pass
    print("\nYou are now in rank: %d! Keep the pedal to the metal!" % player1.rank)

#the following dictionaries are for each outcome
catastrophic = {
    1: "During your pass attempt, your back tire blows out, causing you to have to pit for repairs. You lose two spots.",
    2: "You move to pass the kart in front of you, but suddenly the fearsome cat Guster jumps on the track. You swerve to miss the cat, saving his life but causing you to lose two spots.",
    3: "Fario runs out from the pits and throws a turtle shell onto the track. You hit it and lose two spots.",
    4: "The Godfather makes you an offer you can't refuse. You refused ... so he went to the mattresses. You lose two spots.",
    5: "Corbin Dallas asked for your MultiPass. You 'dropped' it and got held up in the pits. Lose two spots.", 
}

bad = {
    6: "You try to pass but there is a lot of debris from another car you have to avoid. You hit it, causing your car to spin out. You drop back one spot.",
    7: "You attempt to pass the kart in front of you. As you make your move, the kart behind you makes his move. You swerve out of the way in the nick of time. Unfortunately, you also lost your spot.",
    8: "You hit a wet patch on the track and almost lose control of the car. The driver behind you sees their opportunity and passes you. ",
    9: "Over your radio you hear, 'Doh!' ... Homer forgot to fill the gas tank on the last pit. You have to go easy on the gas and lose one spot.",
    10: "Peter and the Giant Chicken start fighting on the track! You have to swerve to avoid wrecking your car in the carnage. A driver passes you and you lose one spot.",
}

neutral = {
    11: "You attempt to pass, but the other driver is much more skillful than you. He flips you off out of the window and keeps his spot.",
    12: "You wanted to pass the kart in front of you, but thoughts of the work you needed to do at home distracted you. 'Did you leave the oven on?' You missed your chance to pass.",
    13: "As you race along the track, thoughts of programming in Python fill your mind. Now you're too 'mentally drained' to pass.",
    14: "In a test of your driving ability, you move to pass. Your kart starts to spin-out but you are able to get back control just in time to not lose your spot.",
    15: "Faith No More steps on stage at the winner's circle and starts playing 'Epic'. Everyone is distracted ... including you. You stay in your spot.",
}

good = {
    16: "In a daring test of your driving ability, you move to pass. The driver in front of you picks a bad line, and you slide past to gain one spot.",
    17: "You pull alongside the kart next to you and wink at your opponent. He is so distracted by your dashing good looks and charm that you can pass him easily.",
    18: "You rub the genie lamp you've been saving for this occasion. He grants you one wish, and you wish to advance a place. That's it? Out of anything in the world? Uh, okay. You move up a spot.",
    19: "Thanos snapped his fingers and the driver in front of you fades into dust. You shed a single, glistening tear and gain one spot.",
    20: "A giant eagle mistakes you for a hobbit and picks up your kart! Luckily, he realizes his mistake and drops you back onto the track a spot ahead of where you were. Sweet!",
}

catastrophic_first = {
    1: "During your time in first, your back tire blows out ... causing you to have to pit for repairs. You lose two spots. Bummer!",
    2: "You speed forward to keep your spot in first, but sudenly Beans the cat jumps on to the track. She isn't in your way, but she's so cute that you stop to pet her. You've lost two spots by the time you get back into your kart.",
    3: "A blue shell hits your kart, sending you into the sky. This isn't even Mario Kart! Where did that come from?! You lose two spots.",
    4: "Odin lopes onto the course and wags his tail in your direction. You have to stop and tell him that he's a good boy. He must know. Lose two spots.",
    5: "Off in the distance you hear a familiar melody. You cock your head to listen ... it's the ice cream truck! You speed off the track and grab one of those weird popsicles that look like Spongebob. It's delicious, but you lose two spots by the time you make it back.", 
}

bad_first = {
    6: "You are in first! Everything is awesome! You're the best! As with classic heroes of old, your hubris is your fatal flaw. Turns out doing a handstand on top of your kart during the race was a bad idea. Lose one spot.",
    7: "While all those energy drinks you consumed before the race have helped you attain first place, they also have filled up your bladder. You stop for a potty break and lose one spot.",
    8: "Happy to be in first, you look around you. What's that blur? It's a bird! It's a plane! No, it's your opponent passing you. Lose one spot.",
    9: "You're cruising along when a haunting melody enters your head. 'First is the worst, second is the best ...'. You can't get the song out of your brain and you slow enough to lose one spot.",
    10: "Another kart enters the race ahead of you! It's Sean's moving truck! A Power Rangers figurine falls off, and you swerve to avoid it. Lose your first place spot.",
}

neutral_first = {
    11: "You zoom past a witch and splash her with water. She curses you, but you already have a counterspell placed on you by your team warlock. The curse rebounds and hits her! Ha! Take that! You keep your first-place spot. ",
    12: "You look at your kart and notice that it has turned into a blue Toyota Yaris! How could this be? Luckily, The Blueberry is a winner. You maintain your spot.",
    13: "The guys from Pimp My Ride sprint onto the track and jump into your kart. They hook you up with some sick speakers and a minibar. Cool? This has no effect on your driving ability. You keep your first-place spot.",
    14: "You're in first! The sun is shining! The birds are singing! Everything is right with the world. Except the pandemic and stuff. Shoot ... Bob Marley appears and tell you not to worry. You don't. You manage to keep your spot.",
    15: "Your stomach grumbles. You've forgotten to eat lunch! You must have been coding so much that you skipped it! Sean warned you about this! Thankfully, you packed enough fruit by the foot in your fanny pack to stave off the hunger. You maintain your place in first.",
}
# these are the functions for each outcome
def good_outcomes(dict, x):
    print(dict[x])
    rank_change = -1
    return rank_change 
def bad_outcomes(dict, x):
    print(dict[x])
    rank_change = 1
    return rank_change
def neutral_outcomes(dict, x):
    print(dict[x])
    rank_change = 0
    return rank_change
def catastrophic_outcomes(dict, x):
    print(dict[x])
    rank_change = 2
    return rank_change
#this is the main function for each lap
def go_around_track(player1):   
    if player1.rank == 1:
        probability_first = random.randint(1,15)
        x = probability_first
        if probability_first >= 1 and probability_first <= 5:
            print("Oh no! It's a catastrophe!\n")
            player_rank_change = catastrophic_outcomes(catastrophic_first, x)
        elif probability_first >= 6 and probability_first <= 10:
            print("Oh, no! It's not good news!\n")
            player_rank_change = bad_outcomes(bad_first, x)
        elif probability_first >= 11 and probability_first <=15:
            print("Meh. It's pretty neutral.\n")
            player_rank_change = neutral_outcomes(neutral_first, x)
    else:
        probability = random.randint(1,20)
        x = probability
        if probability >= 1 and probability <= 5:
            print("Oh no! It's a catastrophe!\n")
            player_rank_change = catastrophic_outcomes(catastrophic, x)
        elif probability >= 6 and probability <= 10:
            print("Oh, no! It's not good news!\n")
            player_rank_change = bad_outcomes(bad, x)
        elif probability >= 11 and probability <= 15:
            print("Meh. It's pretty neutral.\n")
            player_rank_change = neutral_outcomes(neutral, x)
        elif probability >= 16 and probability <= 20:
            print("Hey! Something went right!\n")
            player_rank_change = good_outcomes(good, x)
    if player_rank_change == 1 and player1.rank <= 3:
        player1.rank += 1
    elif player_rank_change == 2 and player1.rank <=2:
        player1.rank += 2
    elif player_rank_change ==2 and player1.rank ==3:
        player1.rank += 1
    elif player_rank_change == -1 and player1.rank >= 2:
        player1.rank -= 1
    elif player_rank_change == -1 and player1.rank == 1:
        player1.rank == 1
    else:
        pass
    print("\nYou are now in rank %d! Keep the pedal to the metal!\n" % player1.rank)
    return player1

# def game():
    while True:
        pass

# def track_1_turn_agg(probability):
#     if 1 <= probability <= 4:
#         change_in_places = -1
#     if 5 <= probability <= 12:
#         change_in_places = 0
#     if 13 <= probability <= 20:
#         change_in_places = +1
# #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
# #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places

# def track_1_turn_pass(probability):
#     if 1 <= probability <= 4:
#         change_in_places = -1
#     if 5 <= probability <= 14:
#         change_in_places = 0
#     if 15 <= probability <= 20:
#         change_in_places = +1
# #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
# #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print(".")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places

# def track_1_straight_agg(probability):
#     if 1 <= probability <= 4:
#         change_in_places = -1
#     if 5 <= probability <= 12:
#         change_in_places = 0
#     if 13 <= probability <= 20:
#         change_in_places = +1

# #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     #Bad_event
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
#     #Neutral_event
#     elif probability == 5:
#         print("stayed in current spot")
#     elif probability == 6:
#         print("stayed in current spot")
#     #Positive_Event
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("you advanced one spot")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot")
#     return change_in_places

# def track_1_straight_pass(probability):
#     if 1 <= probability <= 4:
#         change_in_places = -1
#     if 5 <= probability <= 14:
#         change_in_places = 0
#     if 15 <= probability <= 20:
#         change_in_places = +1
# #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
# #Neutral_event
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places


# def track_1_in_first(probability):
#     if 1 <= probability <= 4:
#         change_in_places = -1
#     if 5 <= probability <= 20:
#         change_in_places = 0
# #Bad_event
#     if probability == 1:
#         print("lost two spots")
#     elif probability == 2:
#         print("lost two spots")
# #Neutral_event
#     elif probability == 3:
#         print("lost one spot")
#     elif probability == 4:
#         print("lost one spot")
#     elif probability == 5:
#         print("stayed in current spot")
#     elif probability == 6:
#         print("stayed in current spot")
#     elif probability == 7:
#         print("stayed in current spot")
#     elif probability == 8:
#         print("stayed in current spot")
#     elif probability == 9:
#         print("stayed in current spot")
#     elif probability == 10:
#         print("stayed in current spot")
#     elif probability == 11:
#         print("stayed in current spot")
#     elif probability == 12:
#         print("stayed in current spot")
#     elif probability == 13:
#         print("stayed in current spot")
#     elif probability == 14:
#         print("stayed in current spot")
#     elif probability == 15:
#         print("stayed in current spot")
#     elif probability == 16:
#         print("stayed in current spot")
#     elif probability == 17:
#         print("stayed in current spot")
#     elif probability == 18:
#         print("stayed in current spot")
#     elif probability == 19:
#         print("stayed in current spot")
#     elif probability == 20:
#         print("stayed in current spot")
#     return change_in_places


# ##Track 2##---------------------------------------------------------------

# def track_2_turn_agg(probability):
#     if 1 <= probability <= 6:
#         change_in_places = -1
#     if 7 <= probability <= 12:
#         change_in_places = 0
#     if 13 <= probability <= 20:
#         change_in_places = +1
# #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
# #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("Y")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places

# def track_2_turn_pass(probability):
#     if 1 <= probability <= 6:
#         change_in_places = -1
#     if 7 <= probability <= 14:
#         change_in_places = 0
#     if 15 <= probability <= 20:
#         change_in_places = +1
# #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print(".")
# #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places

# def track_2_straight_agg(probability):
#     if 1 <= probability <= 6:
#         change_in_places = -1
#     if 7 <= probability <= 12:
#         change_in_places = 0
#     if 13 <= probability <= 20:
#         change_in_places = +1

# #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     #Bad_event
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
#     #Nutral_event
#     elif probability == 5:
#         print("stayed in current spot")
#     elif probability == 6:
#         print("stayed in current spot")
#     #Positive_Event
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("you advanced one spot")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot")
#     return change_in_places

# def track_2_straight_pass(probability):
#     if 1 <= probability <= 6:
#         change_in_places = -1
#     if 7 <= probability <= 14:
#         change_in_places = 0
#     if 15 <= probability <= 20:
#         change_in_places = +1
# #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
# #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places


# def track_2_in_first(probability):
#     if 1 <= probability <= 6:
#         change_in_places = -1
#     if 7 <= probability <= 20:
#         change_in_places = +0
# #Bad_event
#     if probability == 1:
#         print("lost two spots")
#     elif probability == 2:
#         print("lost two spots")
#     #Bad_event
#     elif probability == 3:
#         print("lost one spot")
#     elif probability == 4:
#         print("lost one spot")
#     #Neutral_event
#     elif probability == 5:
#         print("stayed in current spot")
#     elif probability == 6:
#         print("stayed in current spot")
#     elif probability == 7:
#         print("stayed in current spot")
#     elif probability == 8:
#         print("stayed in current spot")
#     elif probability == 9:
#         print("stayed in current spot")
#     elif probability == 10:
#         print("stayed in current spot")
#     elif probability == 11:
#         print("stayed in current spot")
#     elif probability == 12:
#         print("stayed in current spot")
#     elif probability == 13:
#         print("stayed in current spot")
#     elif probability == 14:
#         print("stayed in current spot")
#     elif probability == 15:
#         print("stayed in current spot")
#     elif probability == 16:
#         print("stayed in current spot")
#     elif probability == 17:
#         print("stayed in current spot")
#     elif probability == 18:
#         print("stayed in current spot")
#     elif probability == 19:
#         print("stayed in current spot")
#     elif probability == 20:
#         print("stayed in current spot")
#     return change_in_places


# ##Track 3##---------------------------------------------------------------

# def track_3_turn_agg(probability):
#     if 1 <= probability <= 3:
#         change_in_places = -2
#     if 4 <= probability <= 8:
#         change_in_places = -1
#     if 9 <= probability <= 14:
#         change_in_places = 0
#     if 15 <= probability <= 20:
#         change_in_places = +1
# #Catastrophic_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
# #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places

# def track_3_turn_pass(probability):
#     if 1 <= probability <= 3:
#         change_in_places = -2
#     if 4 <= probability <= 6:
#         change_in_places = -1
#     if 7 <= probability <= 14:
#         change_in_places = 0
#     if 15 <= probability <= 20:
#         change_in_places = +1
# #Catastrophic_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print(".")
# #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places

# def track_3_straight_agg(probability):
#     if 1 <= probability <= 3:
#         change_in_places = -2
#     if 4 <= probability <= 8:
#         change_in_places = -1
#     if 9 <= probability <= 14:
#         change_in_places = 0
#     if 15 <= probability <= 20:
#         change_in_places = +1

# #Catastrophic_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     #Bad_event
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
#     #Neutral_event
#     elif probability == 5:
#         print("stayed in current spot")
#     elif probability == 6:
#         print("stayed in current spot")
#     #Positive_Event
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("you advanced one spot")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot")
#     return change_in_places

# def track_3_straight_pass(probability):
#     if 1 <= probability <= 3:
#         change_in_places = -2
#     if 4 <= probability <= 6:
#         change_in_places = -1
#     if 7 <= probability <= 14:
#         change_in_places = 0
#     if 15 <= probability <= 20:
#         change_in_places = +1

# #Catastrophic_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
# #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
# #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places


# def track_3_in_first(probability):
#     if 1 <= probability <= 3:
#         change_in_places = -2
#     if 4 <= probability <= 6:
#         change_in_places = -1
#     if 7 <= probability <= 20:
#         change_in_places = 0
#     #Catastrophic_event
#     if probability == 1:
#         print("lost two spots")
#     elif probability == 2:
#         print("lost two spots")
#     #Bad_event
#     elif probability == 3:
#         print("lost one spot")
#     elif probability == 4:
#         print("lost one spot")
#     #Neutral_event
#     elif probability == 5:
#         print("stayed in current spot")
#     elif probability == 6:
#         print("stayed in current spot")
#     elif probability == 7:
#         print("stayed in current spot")
#     elif probability == 8:
#         print("stayed in current spot")
#     elif probability == 9:
#         print("stayed in current spot")
#     elif probability == 10:
#         print("stayed in current spot")
#     elif probability == 11:
#         print("stayed in current spot")
#     elif probability == 12:
#         print("stayed in current spot")
#     elif probability == 13:
#         print("stayed in current spot")
#     elif probability == 14:
#         print("stayed in current spot")
#     elif probability == 15:
#         print("stayed in current spot")
#     elif probability == 16:
#         print("stayed in current spot")
#     elif probability == 17:
#         print("stayed in current spot")
#     elif probability == 18:
#         print("stayed in current spot")
#     elif probability == 19:
#         print("stayed in current spot")
#     elif probability == 20:
#         print("stayed in current spot")
#     return change_in_places


# ##Track 4##---------------------------------------------------------------

# def track_4_turn_agg(probability):
#     if 1 <= probability <= 5:
#         change_in_places = -2
#     if 6 <= probability <= 11:
#         change_in_places = -1
#     if 12 <= probability <= 17:
#         change_in_places = 0
#     if 18 <= probability <= 20:
#         change_in_places = +1
#     #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
#     #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
#     #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places

# def track_4_turn_pass(probability):
#     if 1 <= probability <= 4:
#         change_in_places = -2
#     if 5 <= probability <= 8:
#         change_in_places = -1
#     if 9 <= probability <= 17:
#         change_in_places = 0
#     if 18 <= probability <= 20:
#         change_in_places = +1
#     #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
#     #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
#     #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places

# def track_4_straight_agg(probability):
#     if 1 <= probability <= 5:
#         change_in_places = -2
#     if 6 <= probability <= 11:
#         change_in_places = -1
#     if 12 <= probability <= 17:
#         change_in_places = 0
#     if 18 <= probability <= 20:
#         change_in_places = +1

#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     #Bad_event
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
#     #Neutral_event
#     elif probability == 5:
#         print("stayed in current spot")
#     elif probability == 6:
#         print("stayed in current spot")
#     #Positive_Event
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("you advanced one spot")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot")
#     return change_in_places

# def track_4_straight_pass(probability):
#     if 1 <= probability <= 4:
#         change_in_places = -2
#     if 5 <= probability <= 8:
#         change_in_places = -1
#     if 9 <= probability <= 17:
#         change_in_places = 0
#     if 18 <= probability <= 20:
#         change_in_places = +1
#     #Bad_event
#     if probability == 1:
#         print("")
#     elif probability == 2:
#         print("")
#     elif probability == 3:
#         print("")
#     elif probability == 4:
#         print("")
#     #Neutral_event
#     elif probability == 5:
#         print("")
#     elif probability == 6:
#         print("")
#     elif probability == 7:
#         print("")
#     elif probability == 8:
#         print("")
#     elif probability == 9:
#         print("you advanced one spot")
#     elif probability == 10:
#         print("you advanced one spot")
#     elif probability == 11:
#         print("you advanced one spot")
#     elif probability == 12:
#         print("you advanced one spot")
#     #Positive_Event
#     elif probability == 13:
#         print("you advanced one spot")
#     elif probability == 14:
#         print("you advanced one spot")
#     elif probability == 15:
#         print("you advanced one spot")
#     elif probability == 16:
#         print("you advanced one spot")
#     elif probability == 17:
#         print("you advanced one spot")
#     elif probability == 18:
#         print("you advanced one spot")
#     elif probability == 19:
#         print("you advanced one spot")
#     elif probability == 20:
#         print("you advanced one spot") 
#     return change_in_places


# def track_4_in_first(probability):
#     if 1 <= probability <= 5:
#         change_in_places = -2
#     if 6 <= probability <= 11:
#         change_in_places = -1
#     if 11 <= probability <= 20:
#         change_in_places = 0
#     #Catastrophic_event
#     if probability == 1:
#         print("lost two spots")
#     elif probability == 2:
#         print("lost two spots")
#     #Bad_event
#     elif probability == 3:
#         print("lost one spot")
#     elif probability == 4:
#         print("lost one spot")
#     #Neutral_event
#     elif probability == 5:
#         print("stayed in current spot")
#     elif probability == 6:
#         print("stayed in current spot")
#     elif probability == 7:
#         print("stayed in current spot")
#     elif probability == 8:
#         print("stayed in current spot")
#     elif probability == 9:
#         print("stayed in current spot")
#     elif probability == 10:
#         print("stayed in current spot")
#     elif probability == 11:
#         print("stayed in current spot")
#     elif probability == 12:
#         print("stayed in current spot")
#     elif probability == 13:
#         print("stayed in current spot")
#     elif probability == 14:
#         print("stayed in current spot")
#     elif probability == 15:
#         print("stayed in current spot")
#     elif probability == 16:
#         print("stayed in current spot")
#     elif probability == 17:
#         print("stayed in current spot")
#     elif probability == 18:
#         print("stayed in current spot")
#     elif probability == 19:
#         print("stayed in current spot")
#     elif probability == 20:
#         print("stayed in current spot")
#     return change_in_places

# def track_1_turn_player(): 
#     print("As you round the turn, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
#     #ask for user input if they want to be aggressive or passive
#     user_input = input()
#     #if they choose aggressive
#     if user_input == "1":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_turn + track_1_handling_bonus + player_kart_all
#         change_in_places_player = track_1_turn_agg(probability)
#     #if they choose passive
#     elif user_input == "2":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_turn + track_1_handling_bonus + player_kart_all 
#         change_in_places_player = track_1_turn_pass(probability)
#     else:
#         #if they press something other than 1 or 2
#         print("Please only enter the number one (1) or the number two (2).")
#     #run computers through the event
# def track_1_turn_computer():
#     #decide whether they are aggressive (1) or passive (2)
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_1_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_1_handling_bonus
#     return change_in_places_comp1
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_1_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_1_handling_bonus
#     return change_in_places_comp2
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_1_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_1_handling_bonus
#     return change_in_places_comp3
# def track_1_straight_player(): 
#     print("As you near the straight section of the track, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
#     #ask for user input if they want to be aggressive or passive
#     user_input = input()
#     #if they choose aggressive
#     if user_input == "1":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_straight + track_1_speed_bonus + player_kart_all
#         change_in_places_player = track_1_straight_agg(probability)
#     #if they choose passive
#     elif user_input == "2":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_straight + track_1_speed_bonus + player_kart_all
#         change_in_places_player = track_1_straight_pass(probability)
#     else:
#         #if they press something other than 1 or 2
#         print("Please only enter the number one (1) or the number two (2).")
#     #run computers through the event
# def track_1_straight_computer():
#     #decide whether they are aggressive (1) or passive (2)
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_straight + comp1_all + track_1_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_straight + comp1_all + track_1_speed_bonus
#     return change_in_places_comp1
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_straight + comp2_all + track_1_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_straight + comp2_all + track_1_speed_bonus
#     return change_in_places_comp2
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_straight + comp3_all + track_1_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_straight + comp3_all + track_1_speed_bonus
#     return change_in_places_comp3
# def track_2_turn_player():
#     print("As you round the turn, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
#     #ask for user input if they want to be aggressive or passive
#     user_input = input()
#     #if they choose aggressive
#     if user_input == "1":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_turn + track_2_handling_bonus + player_kart_all
#         change_in_places_player = track_2_turn_agg(probability)
#     #if they choose passive
#     elif user_input == "2":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_turn + track_2_handling_bonus + player_kart_all 
#         change_in_places_player = track_2_turn_pass(probability)
#     else:
#         #if they press something other than 1 or 2
#         print("Please only enter the number one (1) or the number two (2).")
#     #run computers through the event
# def track_2_turn_computer():
#     #decide whether they are aggressive (1) or passive (2)
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_2_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_2_handling_bonus
#     return change_in_places_comp1
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_2_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_2_handling_bonus
#     return change_in_places_comp2
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_2_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_2_handling_bonus
#     return change_in_places_comp3
# def track_2_straight_player():
#     print("As you near the straight section of the track, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
#     #ask for user input if they want to be aggressive or passive
#     user_input = input()
#     #if they choose aggressive
#     if user_input == "1":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_straight + track_2_speed_bonus + player_kart_all
#         change_in_places_player = track_2_straight_agg(probability)
#     #if they choose passive
#     elif user_input == "2":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_straight + track_2_speed_bonus + player_kart_all
#         change_in_places_player = track_2_straight_pass(probability)
#     else:
#         #if they press something other than 1 or 2
#         print("Please only enter the number one (1) or the number two (2).")
#     #run computers through the event
# def track_2_straight_computer():
#     #decide whether they are aggressive (1) or passive (2)
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_2_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_2_speed_bonus
#     return change_in_places_comp1
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_2_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_2_speed_bonus
#     return change_in_places_comp2
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_2_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_2_speed_bonus
#     return change_in_places_comp3
# def track_3_turn_player():
#     print("As you round the turn, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
#     #ask for user input if they want to be aggressive or passive
#     user_input = input()
#     #if they choose aggressive
#     if user_input == "1":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_turn + track_3_handling_bonus + player_kart_all
#         change_in_places_player = track_3_turn_agg(probability)
#     #if they choose passive
#     elif user_input == "2":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_turn + track_3_handling_bonus + player_kart_all 
#         change_in_places_player = track_3_turn_pass(probability)
#     else:
#         #if they press something other than 1 or 2
#         print("Please only enter the number one (1) or the number two (2).")
# def track_3_turn_computer():
#     #decide whether they are aggressive (1) or passive (2)
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_3_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_3_handling_bonus
#     return change_in_places_comp1
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_3_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_3_handling_bonus
#     return change_in_places_comp2
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_3_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_3_handling_bonus
#     return change_in_places_comp3
# def track_3_straight_player():
#     print("As you near the straight section of the track, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
#     #ask for user input if they want to be aggressive or passive
#     user_input = input()
#     #if they choose aggressive
#     if user_input == "1":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_straight + track_3_speed_bonus + player_kart_all
#         change_in_places_player = track_1_straight_agg(probability)
#     #if they choose passive
#     elif user_input == "2":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_straight + track_3_speed_bonus + player_kart_all
#         change_in_places_player = track_1_straight_pass(probability)
#     else:
#         #if they press something other than 1 or 2
#         print("Please only enter the number one (1) or the number two (2).")
#     #run computers through the event
# def track_3_straight_computer():
#     #decide whether they are aggressive (1) or passive (2)
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_3_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_3_speed_bonus
#     return change_in_places_comp1
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_3_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_3_speed_bonus
#     return change_in_places_comp2
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_3_speed_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_3_speed_bonus
#     return change_in_places_comp3
# def track_4_turn_player():
#     print("As you round the turn, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
#     #ask for user input if they want to be aggressive or passive
#     user_input = input()
#     #if they choose aggressive
#     if user_input == "1":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_turn + track_4_handling_bonus + player_kart_all
#         change_in_places_player = track_4_turn_agg(probability)
#     #if they choose passive
#     elif user_input == "2":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_turn + track_4_handling_bonus + player_kart_all 
#         change_in_places_player = track_4_turn_pass(probability)
#     else:
#         #if they press something other than 1 or 2
#         print("Please only enter the number one (1) or the number two (2).")
#     #run computers through the event
# def track_4_turn_computer():
#     #decide whether they are aggressive (1) or passive (2)
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_4_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp1_kart_turn + comp1_all + track_4_handling_bonus
#     return change_in_places_comp1
#     agg_pass = randint.range(1,3)
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_4_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp2_kart_turn + comp2_all + track_4_handling_bonus
#     return change_in_places_comp2
#     if agg_pass == 1:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_4_handling_bonus
#     if agg_pass == 2:
#         base_probability = randint.range(1, 20)
#         probability = base_probability + comp3_kart_turn + comp3_all + track_4_handling_bonus
#     return change_in_places_comp3
# def track_4_straight_player():
#     print("As you near the straight section of the track, you have a choice. Should you be aggressive or passive in your approach? If you want to be aggressive, press 1. If you want to be passive, press 2.")
#     #ask for user input if they want to be aggressive or passive
#     user_input = input()
#     #if they choose aggressive
#     if user_input == "1":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_straight + track_1_speed_bonus + player_kart_all
#         change_in_places_player = track_1_straight_agg(probability)
#     #if they choose passive
#     elif user_input == "2":
#         base_probability = randint.range(1, 20)
#         probability = base_probability + player_kart_straight + track_1_speed_bonus + player_kart_all
#         change_in_places_player = track_1_straight_pass(probability)
#     else:
#         #if they press something other than 1 or 2
#         print("Please only enter the number one (1) or the number two (2).")
#     #run computers through the event
# def track_4_straight_computer():
    #decide whether they are aggressive (1) or passive (2)
    # agg_pass = randint.range(1,3)
    # if agg_pass == 1:
    #     base_probability = randint.range(1, 20)
    #     probability = base_probability + comp1_kart_straight + comp1_all + track_1_speed_bonus
    # if agg_pass == 2:
    #     base_probability = randint.range(1, 20)
    #     probability = base_probability + comp1_kart_straight + comp1_all + track_1_speed_bonus
    # return change_in_places_comp1
    # agg_pass = randint.range(1,3)
    # if agg_pass == 1:
    #     base_probability = randint.range(1, 20)
    #     probability = base_probability + comp2_kart_straight + comp2_all + track_1_speed_bonus
    # if agg_pass == 2:
    #     base_probability = randint.range(1, 20)
    #     probability = base_probability + comp2_kart_straight + comp2_all + track_1_speed_bonus
    # return change_in_places_comp2
    # if agg_pass == 1:
    #     base_probability = randint.range(1, 20)
    #     probability = base_probability + comp3_kart_straight + comp3_all + track_1_speed_bonus
    # if agg_pass == 2:
    #     base_probability = randint.range(1, 20)
    #     probability = base_probability + comp3_kart_straight + comp3_all + track_1_speed_bonus
    # return change_in_places_comp3