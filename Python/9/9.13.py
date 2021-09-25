from random import randint
class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1,self.sides)
        print(number)

die_0 = Die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
print()

die_0 = Die(10)
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
print()

die_0 = Die(20)
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
print()