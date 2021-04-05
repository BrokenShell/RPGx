"""
RPG Characters

"""
import random

from Dice.game_dice import dice
from Units.CombatUnits import CombatUnit


class Character(CombatUnit):
    class_name = "NPC"
    primary_stat = None
    specialties = ("Blacksmith", "Farmer", "Merchant", "Villager")
    char_level = 0
    health_dice = 2
    damage_dice = 2
    offence = 0
    defense = 0

    def init_speciality(self):
        if self.specialties and self.level > 4:
            return f"{self.class_name}: {random.choice(self.specialties)}"
        else:
            return self.class_name

    def init_health(self):
        return max(self.health_dice, dice(self.level, self.health_dice))

    def __init__(self, level=1):
        self.level = level
        self.specialty = self.init_speciality()
        self.health = self.max_health = self.init_health()

    def __str__(self):
        output = (
            f"{self.specialty}",
            f"  Level: {self.level}",
            f"  Current/Max Health: {self.health}/{self.max_health}",
            f"  Damage Roll: {self.level}d{self.damage_dice}",
            f"  Attack Roll: 1d20+{self.offence}",
            f"  Defend Roll: 1d20+{self.defense}",
            "",
        )
        return '\n'.join(output)


class Mage(Character):
    class_name = "Mage"
    primary_stat = "Intellect"
    specialties = ("Wizard", "Warlock", "Alchemist")
    health_dice = 6
    damage_dice = 12
    offence = 5
    defense = 1


class Acolyte(Character):
    class_name = "Acolyte"
    primary_stat = "Wisdom"
    specialties = ("Priest", "Cleric", "Templar")
    health_dice = 8
    damage_dice = 8
    offence = 2
    defense = 4


class Sorcerer(Character):
    class_name = "Sorcerer"
    primary_stat = "Charisma"
    specialties = ("Witch", "Shaman", "Druid")
    health_dice = 6
    damage_dice = 12
    offence = 4
    defense = 2


class Rogue(Character):
    class_name = "Rogue"
    primary_stat = "Dexterity"
    specialties = ("Ninja", "Pirate", "Hunter")
    health_dice = 10
    damage_dice = 10
    offence = 3
    defense = 3


class Warrior(Character):
    class_name = "Warrior"
    primary_stat = "Strength"
    specialties = ("knight", "Gladiator", "Barbarian")
    health_dice = 12
    damage_dice = 6
    offence = 1
    defense = 5


if __name__ == '__main__':
    print(f"\nRandom Party of 5 adventurers:\n")
    random_level = lambda: 8 + dice(1, 3)
    m = Mage(random_level())
    print(m)
    a = Acolyte(random_level())
    print(a)
    s = Sorcerer(random_level())
    print(s)
    r = Rogue(random_level())
    print(r)
    w = Warrior(random_level())
    print(w)
    print("Random NPCs:\n")
    for _ in range(5):
        c = Character(random_level())
        print(c)
