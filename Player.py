class Player:
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    def is_offensive(self):
        return ((self.position == "QB") | (self.position == "RB") |
                (self.position == "WR") | (self.position == "TE"))

    def is_defensive(self):
        return not self.is_offensive()

    def __repr__(self):
        return self.position + " " + self.name + "(" + str(self.age) + ")"
