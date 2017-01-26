import random

class Creature:

    def __init__(self,name,level):
        self.name = name
        self.level = level
    
    def __repr__(self):
        return "Creature {} of level {}".format(self.name,self.level)

    def roll(self):
        return random.randint(1,12) * self.level


class Wizard(Creature):

    def attack(self,creature):
        print('{} attacks {}'.format(self.name,creature.name))

        my_roll = self.roll()
        creature_roll = creature.roll()

        print('{} Rolls {}'.format(self.name,my_roll))
        print('{} Rolls {}'.format(creature.name,creature_roll))

        if my_roll >= creature_roll:
            print('You fabulously triumphed over {}'.format(creature.name))
            return True
        else:
            print('The hero has been DEFEATED!')
            return False


class SmallAnimal(Creature):
    def roll(self):
        roll_result = super().roll() / 2
        return roll_result


class Dragon(Creature):
    def __init__(self, name, level, scallines, breath_fire):
        super().__init__(name,level)
        self.breath_fire = breath_fire
        self.scallines = scallines

    def roll(self):
        roll_result = super().roll()
        fire_modifier = 5 if self.breath_fire else 1
        scale_modifier = self.scallines / 10
        return roll_result * fire_modifier * scale_modifier
