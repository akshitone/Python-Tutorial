from random import randrange


class BackgroundColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Gamer:
    def __init__(self, health_point, magic_point, attack, defence, magic):
        self.max_health_point = health_point
        self.health_point = health_point
        self.max_magic_point = magic_point
        self.magic_point = magic_point
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defence = defence
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return randrange(self.attack_low, self.attack_high)

    def generate_spell_magic(self, i):
        magic_low = self.magic[i]["damage"] - 5
        magic_high = self.magic[i]["damage"] + 5
        return randrange(magic_low, magic_high)

    def take_damage(self, damage):
        self.health_point -= damage
        if self.health_point < 0:
            self.health_point = 0
        return self.health_point

    def heal(self, damage):
        self.health_point += damage
        if self.health_point > self.max_health_point:
            self.health_point = self.max_health_point
        return self.health_point

    def get_health_point(self):
        return self.health_point

    def get_max_health_point(self):
        return self.max_health_point

    def get_magic_point(self):
        return self.magic_point

    def get_max_magic_point(self):
        return self.max_magic_point

    def reduce_magic_point(self, cost):
        self.magic_point -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_magic_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(BackgroundColors.OKBLUE + BackgroundColors.BOLD +
              "ACTIONS".center(30, " ") + BackgroundColors.ENDC)
        for action in self.actions:
            print(str(i) + ":" + action)
            i += 1

    def choose_magic(self):
        i = 1
        print(BackgroundColors.OKBLUE + BackgroundColors.BOLD +
              "MAGICS".center(30, " ") + BackgroundColors.ENDC)
        for spell in self.magic:
            print(str(i) + ": " + spell["name"] +
                  "(cost: " + str(spell["cost"]) + ")")
            i += 1
