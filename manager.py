from coach import Coach

class Manager(Coach):
    def __init__(self, player, position, age, team, expir):
        super().__init__(player, position, age, team)
        self.__expir = expir




    def get_printMan(self):
        if self.__expir > 9:
            print(f'Manager {self.player} come with {self.__expir} years experience')
        else:
            print(f'Manager {self.player} come with {self.__expir} year experience')

    def set_printMan(self, newExp):
        self.__expir = newExp


