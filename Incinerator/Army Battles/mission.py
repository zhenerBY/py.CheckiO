# Taken from mission The Warriors

class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return True if self.health > 0 else False


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
        else:
            return True
    return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, warrior: Warrior, amount):
        for i in range(amount):
            self.units.append(warrior())

    def kill_unit(self):
        self.units.pop(0)


class Battle:
    def __init__(self):
        self.army1 = None
        self.army2 = None

    def fight(self, army1: Army, army2: Army):
        self.army1 = army1
        self.army2 = army2
        while True:
            if fight(self.army1.units[0], self.army2.units[0]):
                self.army2.kill_unit()
            else:
                self.army1.kill_unit()
            if len(self.army1.units) == 0:
                return False
            if len(self.army2.units) == 0:
                return True



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
