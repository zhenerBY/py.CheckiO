# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

# Taken from mission The Warriors

class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0
        self.secondattack = 0

    @property
    def is_alive(self):
        return True if self.health > 0 else False


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 6
        self.secondattack = 3


def fight(unit_1, unit_2, unit_1_2=Warrior(), unit_2_2=Warrior()):
    while unit_1.is_alive and unit_2.is_alive:
        damage = (unit_1.attack - unit_2.defense) if (unit_1.attack - unit_2.defense) > 0 else 0
        seconddamage = (unit_1.secondattack - unit_2_2.defense) if (unit_1.secondattack - unit_2_2.defense) > 0 else 0
        unit_2.health -= damage
        unit_2_2.health -= seconddamage
        unit_1.health += damage * unit_1.vampirism / 100
        if unit_2.is_alive:
            damage = (unit_2.attack - unit_1.defense) if (unit_2.attack - unit_1.defense) > 0 else 0
            seconddamage = (unit_2.secondattack - unit_1_2.defense) if (
                                                                                   unit_2.secondattack - unit_1_2.defense) > 0 else 0
            unit_1.health -= damage
            unit_1_2.health -= seconddamage
            unit_2.health += damage * unit_2.vampirism / 100
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
            if len(self.army1.units) > 1:
                second_1 = self.army1.units[1]
            else:
                second_1 = Warrior()
            if len(self.army2.units) > 1:
                second_2 = self.army2.units[1]
            else:
                second_2 = Warrior()
            if fight(self.army1.units[0], self.army2.units[0], second_1, second_2):
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

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
