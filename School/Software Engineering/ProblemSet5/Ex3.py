from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name:str, hp: int, attack:int, move):
        self.__name = name
        if hp <= 10:
            self.__hp = hp
        else:
            self.__hp = 1

        if attack <= 5:
            self.__attack = attack
        else:
            self.__attack = 1

        self.__move = move

    @property
    def get_name(self):
        return self.__name

    @property
    def get_hp(self):
        return self.__hp

    @property
    def get_attack(self):
        return self.__attack

    @abstractmethod
    def movement(self):
        return f"The Unit moves {self.__move} squares"


class Warrior(ABC):
    def __init__(self, name_of_weapon):
        self.__name = name_of_weapon

    @property
    def special(self):
        return self.__name

class Flying(ABC):
    def __init__(self, flight_speed:int):
        self.__flight_speed = flight_speed

    @property
    def special(self):
        return self.__flight_speed

class Aquatic(ABC):
    def __init__(self, depth:int):
        self.__depth = depth

    @property
    def special(self):
        return self.__depth

class Summoner(ABC):
    def __init__(self, name_of_summon:str):
        self.__name = name_of_summon

    @property
    def special(self):
        return self.__name

class Arcane(ABC):
    def __init__(self, name_of_devil:str):
        self.__name = name_of_devil

    @property
    def special(self):
        return self.__name

class Magic(ABC):
    def __init__(self, number_of_spells:int):
        self.__number = number_of_spells

    @property
    def special(self):
        return self.__number


class Barbarian(Character, Warrior):
    def __init__(self, name, hp, attack, name_of_weapon):
        Character.__init__(self, name, hp, attack, move=1)
        Warrior.__init__(self, name_of_weapon)

    def movement(self):
        return Character.movement(self)

    @property
    def special(self):
        return f"Weapon Name: {Warrior.special.fget(self)}"

class Wizard(Character, Magic):
    def __init__(self, name, hp, attack, number_of_spells):
        Character.__init__(self, name, hp, attack, move=2)
        Magic.__init__(self, number_of_spells)

    def movement(self):
        return Character.movement(self)

    @property
    def special(self):
        return f"Number of Spells: {Magic.special.fget(self)}"

class SummonerWizard(Wizard, Summoner):
    def __init__(self, name, hp, attack, number_of_spells, name_of_summon):
        Wizard.__init__(self, name, hp, attack, number_of_spells,)
        Summoner.__init__(self, name_of_summon)

    def movement(self):
        return Character.movement(self)

    @property
    def special(self):
        return f"Summon Name: {Summoner.special.fget(self)}, Number of Spells: {Wizard.special.fget(self)}"

class DarkWizard(Wizard, Arcane):
    def __init__(self, name, hp, attack, number_of_spells, name_of_devil):
        Wizard.__init__(self, name, hp, attack, number_of_spells)
        Arcane.__init__(self, name_of_devil)

    def movement(self):
        return Character.movement(self)

    @property
    def special(self):
        return f"Devil Name: {Arcane.special.fget(self)}, Number of Spells: {Wizard.special.fget(self)}"

class Dragon(Character, Magic, Flying):
    def __init__(self, name, hp, attack, flight_speed, number_of_spells):
        Character.__init__(self, name, hp, attack, move=5)
        Magic.__init__(self, number_of_spells)
        Flying.__init__(self, flight_speed)

    def movement(self):
        return Character.movement(self)

    @property
    def special(self):
        return f"Flight Speed: {Flying.special.fget(self)}, Number of Spells: {Magic.special.fget(self)}"

class Kraken(Character, Aquatic, Magic):
    def __init__(self, name, hp, attack, depth, number_of_spells):
        Character.__init__(self, name, hp, attack, move=4)
        Magic.__init__(self, number_of_spells)
        Aquatic.__init__(self, depth)

    def movement(self):
        return Character.movement(self)

    @property
    def special(self):
        return f"Depth: {Aquatic.special.fget(self)}, Number of Spells: {Magic.special.fget(self)}"

if __name__ == "__main__":

    lista = []

    jimmy = Barbarian(name="Armandone il coccolone", hp=9, attack=10, name_of_weapon="Helm Slayer")
    print(f"Name: {jimmy.get_name}, HP: {jimmy.get_hp}, ATK: {jimmy.get_attack}")
    print(jimmy.movement())
    lista.append(jimmy)

    merlin = Wizard(name="Merlin", hp=5, attack=2, number_of_spells=15)
    print(f"Name: {merlin.get_name}, HP: {merlin.get_hp}, ATK: {merlin.get_attack}")
    print(merlin.movement())
    lista.append(merlin)


    yuna = SummonerWizard(name="Yuna", hp=6, attack=2, number_of_spells=10, name_of_summon="Bahamut")
    print(f"Name: {yuna.get_name}, HP: {yuna.get_hp}, ATK: {yuna.get_attack}")
    print(yuna.movement())
    lista.append(yuna)

    voldemort = DarkWizard(name="Voldemort", hp=7, attack=4, number_of_spells=3, name_of_devil="Mephistopheles")
    print(f"Name: {voldemort.get_name}, HP: {voldemort.get_hp}, ATK: {voldemort.get_attack}")
    print(voldemort.movement())
    lista.append(voldemort)

    smaug = Dragon(name="Smaug", hp=10, attack=5, flight_speed=120, number_of_spells=5)
    print(f"Name: {smaug.get_name}, HP: {smaug.get_hp}, ATK: {smaug.get_attack}")
    print(smaug.movement())
    lista.append(smaug)


    davy = Kraken(name="Davy Jones", hp=9, attack=4, depth=1000, number_of_spells=0)
    print(f"Name: {davy.get_name}, HP: {davy.get_hp}, ATK: {davy.get_attack}")
    print(davy.movement())
    lista.append(davy)

    print("---Polymorphism Test---")
    for i in lista:
        print(i.special)



