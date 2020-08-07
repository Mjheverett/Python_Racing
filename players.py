class Players:
    def __init__(self, rank):
        self.rank = rank

# class Human_player(Players):
#     def __init__(self, rank, driver, kart):
#         super().__init__(rank, driver, kart)

# class CPU_player(Players):
#     def __init__(self, rank, driver, kart):
#         super().__init__(rank, driver, kart)
#
"""ToDo: refactor drivers and karts as part of player class using dictionaries to hold the attributes"""

karts = {
    "Standard": {
        "Speed": 6.5,
        "Handling": 4,
        "Drift": 9,
        "Acceleration": 6.5
    },
    "Mushmellow": {
        "Speed": 4.3,
        "Handling": 6.9,
        "Drift": 6.9,
        "Acceleration": 8.7
    },
    "Powerflower": {
        "Speed": 6.7,
        "Handling": 4.3,
        "Drift": 9,
        "Acceleration": 7.7
    },
    "Dry Bomber": {
        "Speed": 3.4,
        "Handling": 9.8,
        "Drift": 3.9,
        "Acceleration": 9.5
    }
}

drivers = {
    "Veteran": {},
    "Crafty": {},
    "Cavalier": {},
    "Joe": {},
}