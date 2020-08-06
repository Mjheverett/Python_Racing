class Players:
    def __init__(self, rank, driver, kart):
        self.rank = rank
        self.driver = driver
        self.kart = kart

class Human_player(Players):
    def __init__(self, rank, driver, kart):
        super().__init__(rank, driver, kart)

class CPU_player(Players):
    def __init__(self, rank, driver, kart):
        super().__init__(rank, driver, kart)