#Parent Driver class
class Driver:
    def __init__(self, name, speed, knowledge, alertness, patience, mechanical_skills):
        self.name = name
        self.speed = speed
        self.knowledge = knowledge
        self.alertness = alertness
        self.patience = patience
        self.mechanical_skills = mechanical_skills

    def stats(self):
        return """
        %s:
        Speed: %.1f
        Knowledge: %.1f
        Alertness: %.1f
        Mechanical: %.1f
        """ % (self.name.upper(), self.speed, self.knowledge, self.alertness, self.mechanical_skills)

#Driver subclasses
class Driver_1(Driver):
    def __init__(self, name = "Veteran", speed = 5, knowledge = 10, alertness = 5, patience = 5, mechanical_skills = 10):
        super().__init__(name, speed, knowledge, alertness, patience, mechanical_skills)

class Driver_2(Driver):
    def __init__(self, name = "Crafty", speed = 0, knowledge = 10, alertness = 10, patience = 10, mechanical_skills = 5):
        super().__init__(name, speed, knowledge, alertness, patience, mechanical_skills)

class Driver_3(Driver):
    def __init__(self, name = "Cavalier", speed = 10, knowledge = 0, alertness = 5, patience = 0, mechanical_skills = 10):
        super().__init__(name, speed, knowledge, alertness, patience, mechanical_skills)

class Driver_4(Driver):
    def __init__(self, name = "Joe", speed = 5, knowledge = 5, alertness = 5, patience = 5, mechanical_skills = 5):
        super().__init__(name, speed, knowledge, alertness, patience, mechanical_skills)