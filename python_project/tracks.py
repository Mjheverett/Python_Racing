class Tracks:
    def __init__(self, name, difficulty, weather, speed, handeling):
        self.name = name
        self.difficulty = difficulty
        self.weather = weather
        self.speed = speed
        self.handeling = handeling

class Track_1(Tracks):
    def __init__(self, name, difficulty, weather, speed, handeling):
        super().__init__(name, difficulty, weather, speed, handeling)


class Track_2(Tracks):
    def __init__(self, name, difficulty, weather, speed, handeling):
        super().__init__(name, difficulty, weather, speed, handeling)


class Track_3(Tracks):
    def __init__(self, name, difficulty, weather, speed, handeling):
        super().__init__(name, difficulty, weather, speed, handeling)


class Track_4(Tracks):
    def __init__(self, name, difficulty, weather, speed, handeling):
        super().__init__(name, difficulty, weather, speed, handeling)

suzuka = Track_1(Suzuka, 3, 2, 8, 8)
fuji = Track_2(Fuji, 5, 8, 4, 3)
Inagawa = Track_3(Inagawa, 8, 5, 3, 5)
tsukuba = Track_4(Tsukuba, 9, 5, 7, 4)