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


def track_1_turn():
    probability = randint.range(20)
def track_1_straight():
    probability = randint.range(20)

    
probability = randint.range(20)
if probability in range(1,3):
    print("blah blah")
elif probability in range(4, 6):
    print("blah blah")
elif probability == 5:
    print("blah blah")
elif probability == 6:
    print("blah blah")
elif probability == 7:
    print("blah blah")
elif probability == 8:
    print("blah blah")
elif probability == 9:
    print("blah blah")
elif probability == 10:
    print("blah blah")
elif probability == 11:
    print("blah blah")
elif probability == 12:
    print("blah blah")
elif probability == 13:
    print("blah blah")
elif probability == 14:
    print("blah blah")
elif probability == 15:
    print("blah blah")
elif probability == 16:
    print("blah blah")
elif probability == 17:
    print("blah blah")
elif probability == 18:
    print("blah blah")
elif probability == 19:
    print("blah blah")
elif probability == 20:
    print("blah blah")