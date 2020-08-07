from players import Players

player1 = Players(1)

player1.rank=1
player_rank_change = 1

import random
#the following dictionaries are for each outcome
catastrophic = {
    1: "During your pass attempt, your back tire blows out, causing you to have to pit for repairs. You lose two spots.",
    2: "You move to pass the kart in front of you, but sudenly Guster jumps on to the track. You swerve to miss the cat, saving his life but causing you to lose two spots.",
    3: "Fario runs out from the pits and throws a turtle shell onto the track. You hit it and lose two spots.",
    4: "The Godfather makes you an offer you can't refuse. You refused...so he went to the mattresses. You lose two spots.",
    5: "Corbin Dallas asked for your multi-pass. You 'dropped' it and got held up in the pits. Lose two spots.", 
}

bad = {
    6: "You try to pass but there is debris from another car that you have to avoid. You hit it causing your car to spin out. You drop back one spot",
    7: "You attempt to pass the kart in front of you. As you make your move, the kart behind you makes his move. You swerve out of the way in the nick of time. Unfortunately, you also lost your spot",
    8: "You hit a wet patch on the track and almost lose control of the car. The driver behind you sees their opportunity and passes you. ",
    9: "Over your radio you hear 'Doh'...Homer forgot to fill the gas tank on the last pit. You have to go easy on the gas and lose one spot.",
    10: "Peter and the Giant Chicken start fighting on the track! You have to swerve to avoid wrecking your car in the carnage. You get passed and lose one spot.",
}

neutral = {
    11: "You attempt to pass, but the other driver is much more skillful than you. He flips you off out of the window and keeps his spot.",
    12: "You wanted to pass the kart in front of you, but thoughts of the work you needed to do at home distracted you. 'Did you leave the oven on?' You missed your chance to pass.",
    13: "As you race along the track, thoughts of programming in Python fill your mind. Now you're too 'mentally drained' to pass.",
    14: "In a test of your driving ability, you move to pass. Your kart starts to spin-out but you are able to get back control just in time not to lose your spot.",
    15: "Fath No More steps on stage at the winner's circle and starts playing 'Epic'. Everyone is distracted...including you. You stay in your spot.",
}

good = {
    16: "In a daring test of your driving ability, you move to pass. The driver in front of you picks a bad line, and you slide past to gain one spot",
    17: "You pull alongside the kart next to you and wink at your opponent. He is so distracted by your dashing good looks and charm that you can pass him easily.",
    18: "You rub the genie lamp you've been saving for this occasion. He grants you one wish, and you wish to advance a place. That's it? Out of anything in the world? Uh, okay. You move up a spot.",
    19: "Thanos snapped his fingers and the driver in front of you fades into dust. You shed a single, glistening tear and gain one spot.",
    20: "A giant eagle mistakes you for a hobbit and picks up your kart! Luckily, he realizes his mistake and drops you back onto the track a spot ahead of where you were. Sweet!",
}
catastrophic_first = {
    1: "During your time in first, your back tire blows out... causing you to have to pit for repairs. You lose two spots. Bummer!",
    2: "You speed forward to keep your spot in first, but sudenly Beans jumps on to the track. She isn't in your way, but she's so cute that you stop to pet her. You've lost two spots by the time you get back into your kart.",
    3: "A blue shell hits your kart, sending you into the sky. This isn't even Mario Kart! Where did that come from?! You lose two spots.",
    4: "Odin lopes onto the course and wags his tail in your direction. You have to stop and tell him that he's a good boy. He must know. Lose two spots.",
    5: "Off in the distance you hear a familiar melody. You cock your head to listen... It's the ice cream truck! You speed off the track and grab one of those weird popsicles that look like Spongebob. It's delicious, but you lose two spots by the time you make it back.", 
}

bad_first = {
    6: "You are in first! Everything is awesome! You're the best! As with classic heroes of old, your hubris is your fatal flaw. Turns out doing a handstand on top of your kart during the race was a bad idea. Lose one spot.",
    7: "While all those energy drinks you consumed before the race have helped you attain first place, they also have filled up your bladder. You stop for a potty break and lose one spot.",
    8: "Happy to be in first, you look around you. What's that blur? It's a bird! It's a plane! No, it's your opponent passing you. Lose one spot.",
    9: "You're cruising along when a haunting melody enters your head. 'First is the worst, second is the best...' You can't get the song out of your brain and you slow enough to lose one spot.",
    10: "Another kart enters the race ahead of you! It's Sean's moving truck! A Power Rangers figurine falls off, and you swerve to avoid it. Lose your first place spot.",
}

neutral_first = {
    11: "You zoom past a witch and splash her with water. She curses you, but you already have a counterspell placed on you by your team warlock. The curse rebounds and hits her! Ha! Take that! You keep your first place spot. ",
    12: "You look at your kart and notice that it has turned into a blue Toyota Yaris! How could this be? Luckily, The Blueberry is a winner. You maintain your spot.",
    13: "The guys from Pimp My Ride sprint onto the track and jump into your kart. They hook you up with some sick speakers and a minibar. Cool? This has no effect on your driving ability. You keep your first place spot.",
    14: "You're in first! The sun is shining! The birds are singing! Everything is right with the world. Except the pandemic and stuff. Shoot... Bob Marley appears and tell you not to worry. You don't. You manage to keep your spot.",
    15: "Your stomach grumbles. You've forgotten to eat lunch! You must have been coding so much that you skipped it! Sean warned you about this! Thankfully, you packed enough fruit by the foot in your fanny pack to stave off the hunger. You maintain your place in first.",
}
# these are the functions for each outcome
def good_outcomes(dict, x):
    print(dict[x])
    player_rank_change = -1
    return player_rank_change 
def bad_outcomes(dict, x):
    print(dict[x])
    player_rank_change = 1
    return player_rank_change
def neutral_outcomes(dict, x):
    print(dict[x])
    player_rank_change = 0
    return player_rank_change
def catastrophic_outcomes(dict, x):
    print(dict[x])
    player_rank_change = 2
    return player_rank_change
#this is the main function for each lap
def go_around_track():   
    if player1.rank == 1:
        probability_first = random.randint(1,15)
        x = probability_first
        if probability_first >= 1 and probability_first <= 5:
            print("Oh no! It's a catastrophe!")
            catastrophic_outcomes(catastrophic_first, x)
        elif probability_first >= 6 and probability_first <= 10:
            bad_outcomes(bad_first, x)
        elif probability_first >= 11 and probability_first <=15:
            neutral_outcomes(neutral_first, x)
    else:
        probability = random.randint(1,20)
        x = probability
        if probability >= 1 and probability <= 5:
            print("Oh no! It's a catastrophe!")
            catastrophic_outcomes(catastrophic, x)
        elif probability >= 6 and probability <= 10:
            print("Oh, no! It's not good news!")
            bad_outcomes(bad, x)
        elif probability >= 11 and probability <= 15:
            neutral_outcomes(neutral, x)
        elif probability >= 16 and probability <= 20:
            good_outcomes(good, x)

go_around_track()