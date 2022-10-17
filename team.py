from lamo import Lamo
from coach import Coach
from manager import Manager

p2 = Lamo(player = "Makarii", position = "Mid", age=11)
p2.printInfo()
p1 = Lamo("Maxim", 'Def', 12)
p1.printInfo()
c1 = Coach("Dag", "def", 11, "Navy")
c1.coachInfo()
c1.printInfo()

m1 = Manager("Matt", "Manager", 35, "Navy", 8)
m1.set_printMan(2)
m1.get_printMan()
m1.printInfo()
