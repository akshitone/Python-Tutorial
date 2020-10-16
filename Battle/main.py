from random import choice
from classes.game import Gamer, BackgroundColors
from classes.magic import Spell

# BLACK MAGIC
fire = Spell("Fire", 12, 120, "Black")
thunder = Spell("Thunder", 20, 200, "Black")
blizzard = Spell("Blizzard", 17, 170, "Black")
meteor = Spell("Meteor", 15, 150, "Black")
quake = Spell("Quake", 14, 140, "Black")

# WHITE MAGIC
cure = Spell("Cure", 12, 120, "White")
bura = Spell("Bura", 15, 150, "White")
heloy = Spell("Heloy", 17, 170, "White")

# INSTANTIATE PLAYERS
player_one = Gamer(460, 65, 60, 34, [
                   fire, thunder,
                   blizzard, meteor,
                   quake, cure,
                   bura, heloy
                   ])
enemy_one = Gamer(1200, 65, 45, 25, [])

running = True
print(BackgroundColors.FAIL + BackgroundColors.BOLD +
      "AN ENEMY ATTACK!" + BackgroundColors.ENDC)
while running:
    print("".center(50, "="))
    player_one.choose_action()

    player_choice = int(input("Choose player action: ")) - 1

    if player_choice == 0:

        player_damage = player_one.generate_damage()
        enemy_one.take_damage(player_damage)
        print(BackgroundColors.OKGREEN + "Player attack for " +
              str(player_damage) + " points of damages." + BackgroundColors.ENDC)

    elif player_choice == 1:

        player_one.choose_magic()
        magic_choice = int(input("Choose player magic: ")) - 1

        # magic_damage = player_one.generate_spell_magic(magic_choice)
        # magic_spell = player_one.get_spell_name(magic_choice)
        # magic_cost = player_one.get_spell_magic_cost(magic_choice)

        spell = player_one.magic[magic_choice]
        magic_damage = spell.generate_spell_damage()

        current_magic_point = player_one.get_magic_point()

        if spell.cost > current_magic_point:
            print(BackgroundColors.FAIL +
                  "Not enough magic points!".center(50, " ") + BackgroundColors.ENDC)
            continue

        player_one.reduce_magic_point(spell.cost)

        if spell.type == "White":

            player_one.heal(magic_damage)
            print(BackgroundColors.OKBLUE + spell.name + " heals for " +
                  str(magic_damage) + " points." + BackgroundColors.ENDC)

        elif spell.type == "Black":

            enemy_one.take_damage(magic_damage)
            print(BackgroundColors.OKBLUE + spell.name + " deals " +
                  str(magic_damage) + " points of damage." + BackgroundColors.ENDC)

    enemy_choice = 1
    enemy_damage = enemy_one.generate_damage()
    player_one.take_damage(enemy_damage)
    print(BackgroundColors.FAIL + "Enemy attack for " +
          str(enemy_damage) + " points of damages." + BackgroundColors.ENDC)

    print()
    print("HEALTH POINT".center(50, "-"))
    print(BackgroundColors.FAIL + "Enemy: " +
          str(enemy_one.get_health_point()) + "/" + str(enemy_one.get_max_health_point()) + BackgroundColors.ENDC)
    print(BackgroundColors.OKGREEN + "Player: " +
          str(player_one.get_health_point()) + "/" + str(player_one.get_max_health_point()) + BackgroundColors.ENDC)
    print(BackgroundColors.OKBLUE + "Player magic: " +
          str(player_one.get_magic_point()) + "/" + str(player_one.get_max_magic_point()) + BackgroundColors.ENDC)

    if enemy_one.get_health_point() == 0:

        print(BackgroundColors.OKBLUE + BackgroundColors.BOLD +
              "YOU WIN!".center(50, " ") + BackgroundColors.ENDC)
        running = False

    elif player_one.get_health_point() == 0:

        print(BackgroundColors.FAIL + BackgroundColors.BOLD +
              "YOUR ENEMY HAS DEFEATED YOU!".center(50, " ") + BackgroundColors.ENDC)
        running = False
