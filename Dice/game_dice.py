"""
RPG Game Dice
"""
import random


def dice(rolls: int, sides: int) -> int:
    return sum(random.randint(1, sides) for _ in range(rolls))
