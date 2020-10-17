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
    def __init__(self, name, health_point, magic_point, attack, defence, magic, items):
        self.name = name
        self.max_health_point = health_point
        self.health_point = health_point
        self.max_magic_point = magic_point
        self.magic_point = magic_point
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defence = defence
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return randrange(self.attack_low, self.attack_high)

    def take_damage(self, damage):
        self.health_point -= damage
        if self.health_point < 0:
            self.health_point = 0
        return self.health_point

    def heal(self, points):
        self.health_point += points
        print(self.health_point)
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

    def choose_action(self):
        i = 1
        print(BackgroundColors.OKBLUE + BackgroundColors.BOLD +
              ("ACTIONS OF " + str(self.name)).center(100, " ") + BackgroundColors.ENDC)
        for action in self.actions:
            print("    " + str(i) + ":" + action)
            i += 1

    def choose_target(self, enemies):
        i = 1
        print(BackgroundColors.OKBLUE + BackgroundColors.BOLD +
              ("ENEMIES OF " + str(self.name)).center(100, " ") + BackgroundColors.ENDC)
        for enemy in enemies:
            print("    " + str(i) + ":" + enemy.name)
            i += 1

        choice_of_enemy = int(input("Choose player enemy: ")) - 1
        return choice_of_enemy

    def choose_magic(self):
        i = 1
        print(BackgroundColors.OKBLUE + BackgroundColors.BOLD +
              ("MAGICS OF " + str(self.name)).center(100, " ") + BackgroundColors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ": " + spell.name +
                  "(cost: " + str(spell.cost) + ")")
            i += 1

    def choose_items(self):
        i = 1
        print(BackgroundColors.OKBLUE + BackgroundColors.BOLD +
              ("ITEMS OF " + str(self.name)).center(100, " ") + BackgroundColors.ENDC)
        for item in self.items:
            print("    " + str(i) + ": " + item["item"].name +
                  " : " + str(item["item"].description) + " (x" + str(item["qty"]) + ")")
            i += 1

    def get_stats(self):

        health_point_bar = ""
        health_bar_ticks = int(
            (self.health_point/self.max_health_point) * 100 / 4)
        health_point_bar = "█" * health_bar_ticks + \
            " " * (25 - health_bar_ticks)

        magic_point_bar = ""
        magic_bar_ticks = int(
            (self.magic_point/self.max_magic_point) * 100 / 10)
        magic_point_bar = "█" * magic_bar_ticks + " " * (10 - magic_bar_ticks)

        char_hp = str(self.health_point)
        ln = len(str(self.health_point))
        if ln < 4:
            char_hp = " " * (4 - ln) + str(self.health_point)

        char_mp = str(self.magic_point)
        ln = len(str(self.magic_point))
        if ln < 3:
            char_mp = " " * (3 - ln) + str(self.magic_point)

        print(BackgroundColors.OKGREEN +
              "                               _________________________               " + BackgroundColors.OKBLUE + "__________" + BackgroundColors.ENDC)
        print(BackgroundColors.OKGREEN + BackgroundColors.BOLD + self.name + "              " + char_hp + "/" + str(self.max_health_point) +
              " |" + health_point_bar + "|     " + BackgroundColors.OKBLUE + char_mp + "/" + str(self.max_magic_point) + " |" + magic_point_bar + "|" + BackgroundColors.ENDC)

    def get_enemy_stats(self):
        health_point_bar = ""
        health_bar_ticks = int(
            (self.health_point/self.max_health_point) * 100 / 2)
        health_point_bar = "█" * health_bar_ticks + \
            " " * (50 - health_bar_ticks)

        char_hp = str(self.health_point) + "/" + str(self.max_health_point)
        ln = len(char_hp)
        if ln < 11:
            char_hp = " " * (11 - ln) + str(self.health_point) + \
                "/" + str(self.max_health_point)

        print(BackgroundColors.FAIL +
              "                               __________________________________________________" + BackgroundColors.ENDC)
        print(BackgroundColors.FAIL + BackgroundColors.BOLD + self.name + "            " + char_hp +
              " |" + health_point_bar + "|" + BackgroundColors.ENDC)

    def choose_enemy_spell(self):
        magic_choice = randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_damage = spell.generate_spell_damage()

        perc = int(self.health_point / self.max_health_point * 100)

        if self.magic_point < spell.cost or spell.type == "white" and perc > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_damage
