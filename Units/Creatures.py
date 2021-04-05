"""
Creatures: Local beasts and furry critters.

Typically Creatures are not as scary as Monsters, much less Characters.
"""
from Units.CombatUnits import CombatUnit


class Creature(CombatUnit):
    terrains = [
        "Forest", "Swamp", "Mountain", "Cave", "Ocean", "Lake", "River",
        "Garden", "City", "Village", "Dungeon", "Beach", "Jungle", "Dessert",
    ]
    pass
