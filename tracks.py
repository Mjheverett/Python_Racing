class Tracks:
    def __init__(self, name, difficulty, weather, speed, handling):
        self.name = name
        self.difficulty = difficulty
        self.weather = weather
        self.speed = speed
        self.handling = handling
    def stats(self):
        return """
        %s:
        Difficulty: %.1f
        Weather: %.1f
        Speed: %.1f
        Handling: %.1f
        """ % (self.name, self.difficulty, self.weather, self.speed, self.handling)

class Track_1(Tracks):
    def __init__(self, name = "Suzuka", difficulty = 6, weather = 0, speed = 8, handling = 8):
        super().__init__(name, difficulty, weather, speed, handling)


class Track_2(Tracks):
    def __init__(self, name = "Fuji", difficulty = 9, weather = 8, speed = 4, handling = 3):
        super().__init__(name, difficulty, weather, speed, handling)


class Track_3(Tracks):
    def __init__(self, name = "Inagawa", difficulty = 12, weather = 5, speed = 3, handling = 5):
        super().__init__(name, difficulty, weather, speed, handling)


class Track_4(Tracks):
    def __init__(self, name = "Tsukuba", difficulty = 15, weather = 0, speed = 7, handling = 4):
        super().__init__(name, difficulty, weather, speed, handling)

track_1 = Track_1()
track_2 = Track_2()
track_3 = Track_3()
track_4 = Track_4()

#print(track_1.stats())
#print(track_2.stats())
#print(track_3.stats())
#print(track_3.stats())


##Track 1##---------------------------------------------------------------

def track_1_turn():
    probability = randint.range(20)
#Catastrophic_event
if probability == 1:
    print("During your pass attempt on the curve, your back tire blows out....causing you to have to pit for repairs. You lose 2 spots")
elif probability == 2:
    print("losing two spots as a result")
#Bad_event
elif probability == 3:
    print("lost one spot")
elif probability == 4:
    print("lost one spot")
#Nutral_event
elif probability == 5:
    print("You attempt to pass in the curve but the other driver out maneuvers you and keeps their spot - stade in current spot")
elif probability == 6:
    print("stade in current spot")
#Positive_Event
elif probability == 7:
    print("In a test of your driving ability, you move to pass on the turn. The driver in front of you picks a bad line and you slide past to gain one spot")
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


def track_1_straight():
    probability = randint.range(20)
#Catastrophic_event
if probability == 1:
    print("You move to pass the kart in front of you on the straight away. A cat jumps on to the track, you sweve to avoid it! losing two spots as a result")
elif probability == 2:
    print("You move to pass the kart in front of you on the straight away. right when you think all went well you see a road hazard and spenout trying to avoid it, losing two spots as a result")
#Bad_event
elif probability == 3:
    print("You move to pass the kart in front of you on the straight away. right when you think all is going well you realize the kart behind you is now in your way. trying to avoid it you lose one spots as a result")
elif probability == 4:
    print("lost one spot")
#Nutral_event
elif probability == 5:
    print("stade in current spot")
elif probability == 6:
    print("stade in current spot")
#Positive_Event
elif probability == 7:
    print("you advanced one spot")
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


##Track 2##---------------------------------------------------------------

def track_2_turn():
    probability = randint.range(20)
#Catastrophic_event
if probability == 1:
    print("During your pass attempt on the curve, your back tire blows out....causing you to have to pit for repairs. You lose 2 spots")
elif probability == 2:
    print("losing two spots")
elif probability == 3:
    print("losing two spots")
#Bad_event
elif probability == 4:
    print("lost one spot")
elif probability == 5:
    print("lost one spot")
elif probability == 6:
    print("lost one spot")
#Nutral_event
elif probability == 7:
    print("You attempt to pass in the curve but the other driver out maneuvers you and keeps their spot - stade in current spot")
elif probability == 8:
    print("stade in current spot")
elif probability == 9:
    print("stade in current spot")
#Positive_Event
elif probability == 10:
    print("In a test of your driving ability, you move to pass on the turn. The driver in front of you picks a bad line and you slide past to gain one spot")
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

def track_2_straight():
    probability = randint.range(20)
#Catastrophic_event
if probability == 1:
    print("losing two spots")
elif probability == 2:
    print("losing two spots")
elif probability == 3:
    print("losing two spots")
#Bad_event
elif probability == 4:
    print("lost one spot")
elif probability == 5:
    print("lost one spot")
elif probability == 6:
    print("lost one spot")
#Nutral_event
elif probability == 7:
    print("stade in current spot")
elif probability == 8:
    print("stade in current spot")
elif probability == 9:
    print("stade in current spot")
#Positive_Event
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


##Track 3##---------------------------------------------------------------

def track_3_turn():
    probability = randint.range(20)
#Catastrophic_event
if probability == 1:
    print("During your pass attempt on the curve, your back tire blows out....causing you to have to pit for repairs. You lose 2 spots")
elif probability == 2:
    print("losing two spots")
elif probability == 3:
    print("losing two spots")
elif probability == 4:
    print("losing two spots")
#Bad_event
elif probability == 5:
    print("lost one spot")
elif probability == 6:
    print("lost one spot")
elif probability == 7:
    print("lost one spot")
elif probability == 8:
    print("lost one spot")
#Nutral_event
elif probability == 9:
    print("You attempt to pass in the curve but the other driver out maneuvers you and keeps their spot - stade in current spot")
elif probability == 10:
    print("stade in current spot")
elif probability == 11:
    print("stade in current spot")
elif probability == 12:
    print("stade in current spot")
#Positive_Event
elif probability == 13:
    print("In a test of your driving ability, you move to pass on the turn. The driver in front of you picks a bad line and you slide past to gain one spot")
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

def track_3_straight():
    probability = randint.range(20)
#Catastrophic_event
if probability == 1:
    print("losing two spots")
elif probability == 2:
    print("losing two spots")
elif probability == 3:
    print("losing two spots")
elif probability == 4:
    print("losing two spots")
#Bad_event
elif probability == 5:
    print("lost one spot")
elif probability == 6:
    print("lost one spot")
elif probability == 7:
    print("lost one spot")
elif probability == 8:
    print("lost one spot")
#Nutral_event
elif probability == 9:
    print("stade in current spot")
elif probability == 10:
    print("stade in current spot")
elif probability == 11:
    print("stade in current spot")
elif probability == 12:
    print("stade in current spot")
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


##Track 4##---------------------------------------------------------------

def track_4_turn():
    probability = randint.range(20)
#Catastrophic_event
if probability == 1:
    print("During your pass attempt on the curve, your back tire blows out....causing you to have to pit for repairs. You lose 2 spots")
elif probability == 2:
    print("losing two spots")
elif probability == 3:
    print("losing two spots")
elif probability == 4:
    print("losing two spots")
elif probability == 5:
    print("losing two spots")
#Bad_event
elif probability == 6:
    print("You try pass on a curve but there is debris from another car you have to avoid. You hit it causing your car to spin out. You drop back one spot")
elif probability == 7:
    print("lost one spot")
elif probability == 8:
    print("lost one spot")
elif probability == 9:
    print("lost one spot")
elif probability == 10:
    print("lost one spot")
#Nutral_event
elif probability == 11:
    print("You attempt to pass in the curve but the other driver out maneuvers you and keeps their spot - stade in current spot")
elif probability == 12:
    print("stade in current spot")
elif probability == 13:
    print("stade in current spot")
elif probability == 14:
    print("stade in current spot")
elif probability == 15:
    print("stade in current spot")
#Positive_Event
elif probability == 16:
    print("In a test of your driving ability, you move to pass on the turn. The driver in front of you picks a bad line and you slide past to gain one spot")
elif probability == 17:
    print("you advanced one spot")
elif probability == 18:
    print("you advanced one spot")
elif probability == 19:
    print("you advanced one spot")
elif probability == 20:
    print("you advanced one spot") 

def track_4_straight():
    probability = randint.range(20)
#Catastrophic_event
if probability == 1:
    print("losing two spots")
elif probability == 2:
    print("losing two spots")
elif probability == 3:
    print("losing two spots")
elif probability == 4:
    print("losing two spots")
elif probability == 5:
    print("losing two spots")
#Bad_event
elif probability == 6:
    print("lost one spot")
elif probability == 7:
    print("lost one spot")
elif probability == 8:
    print("lost one spot")
elif probability == 9:
    print("lost one spot")
elif probability == 10:
    print("lost one spot")
#Nutral_event
elif probability == 11:
    print("stade in current spot")
elif probability == 12:
    print("stade in current spot")
elif probability == 13:
    print("stade in current spot")
elif probability == 14:
    print("stade in current spot")
elif probability == 15:
    print("stade in current spot")
#Positive_Event
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