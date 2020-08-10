class Kart:
    def __init__(self, name, speed, handling, drift, acceleration, wear = 0):
        self.name = name
        self.speed = speed
        self.handling = handling
        self.drift = drift
        self.acceleration = acceleration
        self.wear = wear
    def stats(self):
        return """
        %s:
        Speed: %.1f
        Handling: %.1f
        Drift: %.1f
        Acceleration: %.1f
        """ % (self.name.upper(), self.speed, self.handling, self.drift, self.acceleration)
# speed is the maximum speed a given kart can go
# handling is the capacity of the kart to make small turns
    #the use of handling causes a speed loss, but this is lessened by a high handling score
#drift is the ability to slide around a corner without speed loss
    #drifting can lead to a spin-out in inclimate weather
#acceleration is how fast a kart achieves maximum speed
    #also indicates the rate of speed recovery after the kart is stopped or slowed
#below this line is commented-out damage methods 
    # """ def spin_out(self, wear):
    #     wear += 1
    #     return ("You've spun-out. \n Your kart has suffered an additional 1 wear. \n Your kart is now at %.1f out of 10 wear." % (self.wear))
    #     if wear >= 10:
    #         return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
    #         #enter a loop to restart the game here
    # def tire_wear(self, wear):
    #     wear += 1.5
    #     return ("You've caused increased wear on your tires. \n Your kart has suffered an additional 1.5 wear. \n Your kart is now at %.1f out of 10 wear." % (self.wear))
    #     if wear >= 10:
    #         return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
    #         #enter a loop to restart the game here
    # def crash_into_wall(self, wear):
    #     wear += 8
    #     return ("You have crashed into a wall. \n Your kart has suffered an additional 8 damage. \n Your kart is now at %.1f out of 10 wear." % (self.wear))
    #     if wear >= 10:
    #         return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
    #         #enter a loop to restart the game here
    # def bump_into_opponent(self, wear):
    #     wear += 2.5 
    #     return ("You have bumped into an opponent's kart. \n Your kart has suffered an additional 2.5 damage. \n Your kart is now at %.1f out of 10 wear." % (self.wear))
    #     if wear >= 10:
    #         return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
    #         #enter a loop to restart the game here
    # def blown_engine(self, wear):
    #     wear += 10
    #     return("You have blown an engine! \n Your kart has suffered an additional 10 damage. \n Your kart is now at %.1f out of 10 wear." % (self.wear))
    #     if wear >= 10:
    #         return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
    #         #enter a loop to restart the game here """

#these are the karts as subclasses
class Standard_kart(Kart):
    def __init__(self, name = "Standard", speed = 6.5, handling = 4, drift = 9, acceleration = 6.5):
        super().__init__(name, speed, handling, drift, acceleration)
class Mushmellow_kart(Kart):
    def __init__(self, name = "Mushmellow", speed = 4.3, handling = 6.9, drift = 6.9, acceleration = 8.7):
        super().__init__(name, speed, handling, drift, acceleration)
class Powerflower_kart(Kart):
    def __init__(self, name = "Powerflower", speed = 6.7, handling = 4.3, drift = 9, acceleration = 7.7):
        super().__init__(name, speed, handling, drift, acceleration)
class Drybomber_kart(Kart):
    def __init__(self, name = "Dry Bomber", speed = 3.4, handling = 9.8, drift = 3.9, acceleration = 9.5):
        super().__init__(name, speed, handling, drift, acceleration)