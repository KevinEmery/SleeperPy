class Player:
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    def isOffensive(self):
        return ((self.position == "QB") | (self.position == "RB") |
                (self.position == "WR") | (self.position == "TE"))

    def isDefensive(self):
        return not self.isOffensive()

    def __repr__(self):
        return self.position + " " + self.name + "(" + str(self.age) + ")"
