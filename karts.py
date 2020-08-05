class Kart:
    def __init__(self, name, speed, handling, drift, acceleration):
        self.name = name
        self.speed = speed
        self.handling = handling
        self.drift = drift
        self.acceleration = acceleration
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

# print(drybomber_kart.stats())

