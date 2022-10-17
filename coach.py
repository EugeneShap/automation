from lamo import Lamo

class Coach(Lamo):
    def __init__(self, player, position, age, team):
        super().__init__(player, position, age)
        self.team = team

    def coachInfo (self):
        print(f'Coach {self.player} training {self.team} team')
