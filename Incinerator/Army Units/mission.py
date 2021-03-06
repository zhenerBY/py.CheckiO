from abc import ABC, abstractmethod


class Army(ABC):

    @abstractmethod
    def train_swordsman(self, name):
        pass

    @abstractmethod
    def train_lancer(self, name):
        pass

    @abstractmethod
    def train_archer(self, name):
        pass


class Swordsman:

    def __init__(self, unittype, army, name):
        self.type = unittype
        self.army = army
        self.name = name

    def introduce(self):
        return f'{self.type} {self.name}, {self.army} swordsman'


class Lancer:

    def __init__(self, unittype, army, name):
        self.type = unittype
        self.army = army
        self.name = name

    def introduce(self):
        return f'{self.type} {self.name}, {self.army} lancer'


class Archer:

    def __init__(self, unittype, army, name):
        self.type = unittype
        self.army = army
        self.name = name

    def introduce(self):
        return f'{self.type} {self.name}, {self.army} archer'


class AsianArmy(Army):

    def train_swordsman(self, name):
        return Swordsman(unittype='Samurai', army='Asian', name=name)

    def train_lancer(self, name):
        return Lancer(unittype='Ronin', army='Asian', name=name)

    def train_archer(self, name):
        return Archer(unittype='Shinobi', army='Asian', name=name)


class EuropeanArmy(Army):

    def train_swordsman(self, name):
        return Swordsman(unittype='Knight', army='European', name=name)

    def train_lancer(self, name):
        return Lancer(unittype='Raubritter', army='European', name=name)

    def train_archer(self, name):
        return Archer(unittype='Ranger', army='European', name=name)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
