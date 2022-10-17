class Lamo:
    color = "green"
    def __init__(self, player, position, age):
        self.player = player
        self.position = position
        self.age = age

    def printInfo (self):
        print(f'Player {self.player} prefer position {self.position} and playing at {self.age} Navy team')

