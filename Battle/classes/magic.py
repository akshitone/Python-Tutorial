from random import randrange


class Spell:
    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type

    def generate_spell_damage(self):
        magic_low = self.damage - 5
        magic_high = self.damage + 5
        return randrange(magic_low, magic_high)
