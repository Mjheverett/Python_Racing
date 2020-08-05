class Tracks:
    def __init__(self, name, difficulty, weather, speed, handeling):
        self.name = name
        self.difficulty = difficulty
        self.weather = weather
        self.speed = speed
        self.handeling = handeling

class Track_1(Tracks):
    def __init__(self, name = "Suzuka", difficulty = 3, weather = 0, speed = 8, handeling = 8):
        super().__init__(name, difficulty, weather, speed, handeling)


class Track_2(Tracks):
    def __init__(self, name = "Fuji", difficulty = 5, weather = 8, speed = 4, handeling = 3):
        super().__init__(name, difficulty, weather, speed, handeling)


class Track_3(Tracks):
    def __init__(self, name = "Inagawa", difficulty = 8, weather = 5, speed = 3, handeling = 5):
        super().__init__(name, difficulty, weather, speed, handeling)


class Track_4(Tracks):
    def __init__(self, name = "Tsukuba", difficulty = 9, weather = 0, speed = 7, handeling = 4):
        super().__init__(name, difficulty, weather, speed, handeling)
        
#hi
