class Kart:
    def __init__(self, name, speed, handling, drift, acceleration, wear = 10):
        self.name = name
        self.speed = speed
        self.handling = handling
        self.drift = drift
        self.acceleration = acceleration
        self.wear = wear
    def stats(self):
        return """
        %s:
        Speed: %d
        Handling: %d
        Drift: %d
        Acceleration: %d
        """ % (self.name, self.speed, self.handling, self.drift, self.acceleration)
# speed is the maximum speed a given kart can go
# handling is the capacity of the kart to make small turns
    #the use of handling causes a speed loss, but this is lessened by a high handling score
#drift is the ability to slide around a corner without speed loss
    #drifting can lead to a spin-out in inclimate weather
#acceleration is how fast a kart achieves maximum speed
    #also indicates the rate of speed recovery after the kart is stopped or slowed


standard_kart = Kart("Standard", 6.5, 4, 9, 6.5)
mushmellow_kart = Kart("Mushmellow", 4.3, 6.9, 6.9, 8.7)
powerflower_kart = Kart("Powerflower", 6.7, 4.3, 9, 6.6)
drybomber_kart = Kart("Dry Bomber", 3.4, 9.8, 3.9, 9.5)

class Damage(Kart):
    def __init__(self, name, speed, handling, drift, acceleration, wear = 10):
        super().__init__(name, speed, handling, drift, acceleration)
        self.wear = wear
    def spin_out(self, wear):
        wear -= 1
        return ("You've spun-out. \n Your kart has suffered an additional 1 wear. \n Your kart is now at %d out of 10 wear." % (self.wear))
        if wear <= 0:
            return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
            #enter a loop to restart the game here
    def tire_wear(self, wear):
        wear -= 1.5
        return ("You've caused increased wear on your tires. \n Your kart has suffered an additional 1.5 wear. \n Your kart is now at %d out of 10 wear." % (self.wear))
        if wear <= 0:
            return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
            #enter a loop to restart the game here
    def crash_into_wall(self, wear):
        wear -= 8
        return ("You have crashed into a wall. \n Your kart has suffered an additional 8 damage. \n Your kart is now at %d out of 10 wear." % (self.wear))
        if wear <= 0:
            return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
            #enter a loop to restart the game here
    def bump_into_opponent(self, wear):
        wear -= 2.5 
        return ("You have bumped into an opponent's kart. \n Your kart has suffered an additional 2.5 damage. \n Your kart is now at %d out of 10 wear." % (self.wear))
        if wear <= 0:
            return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
            #enter a loop to restart the game here
    def blown_engine(self, wear):
        wear -= 10
        return("You have blown an engine! \n Your kart has suffered an additional 10 damage. \n Your kart is now at %d out of 10 wear." % (self.wear))
        if wear <= 0:
            return("Your kart is beat to hell. There is no way you can continue the race. Play again?")
            #enter a loop to restart the game here

print(drybomber_kart.stats())

