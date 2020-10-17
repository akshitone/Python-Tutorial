from random import randrange
from classes.game import Gamer, BackgroundColors
from classes.magic import Spell
from classes.inventory import Item

# BLACK MAGIC
fire = Spell("Fire", 32, 520, "Black")
thunder = Spell("Thunder", 50, 600, "Black")
blizzard = Spell("Blizzard", 47, 570, "Black")
meteor = Spell("Meteor", 45, 550, "Black")
quake = Spell("Quake", 35, 540, "Black")

# WHITE MAGIC
cure = Spell("Cure", 45, 520, "White")
bura = Spell("Bura", 55, 550, "White")
heloy = Spell("Heloy", 59, 570, "White")

# CREATE SOME ITEMS
potion = Item("Potion", "potion", "Heals 50 health points", 700)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 health points", 1500)
super_potion = Item("Super-Potion", "potion", "Heals 500 health points", 3000)
elixer = Item("Elixer", "elixer",
              "Fully restores health points / magic points of one party member", 9999)
mega_elixer = Item("Mega-Elixer", "elixer",
                   "Fully restores party's health points / magic points", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 2200)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, bura, heloy]
enemy_spells = [fire, thunder, cure]
player_items = [
    {"item": potion, "qty": 2},
    {"item": hi_potion, "qty": 3},
    {"item": super_potion, "qty": 5},
    {"item": elixer, "qty": 2},
    {"item": mega_elixer, "qty": 5},
    {"item": grenade, "qty": 3}
]

# INSTANTIATE PLAYERS
player_1 = Gamer("RAGNAR", 4260, 265, 260, 34, player_spells, player_items)
player_2 = Gamer("DARKO ", 3160, 145, 230, 34, player_spells, player_items)
player_3 = Gamer("LUCY  ", 3460, 170, 250, 34,
                 player_spells, player_items)
enemy_1 = Gamer("DAMON ", 12200, 325, 545, 25, enemy_spells, [])
enemy_2 = Gamer("REXO  ", 5200, 295, 245, 25, enemy_spells, [])

players = [player_1, player_2, player_3]
enemies = [enemy_1, enemy_2]
running = True

print("\n\n")
print(BackgroundColors.FAIL + BackgroundColors.BOLD +
      "AN ENEMY ATTACK!".center(100, " ") + BackgroundColors.ENDC)


def defeat_enemy(choice_of_enemy):
    if enemies[choice_of_enemy].get_health_point() == 0:
        print(BackgroundColors.OKGREEN + BackgroundColors.BOLD +
              enemies[choice_of_enemy].name + " has died." + BackgroundColors.ENDC)
        del enemies[choice_of_enemy]


def defeat_player(choice_of_player):
    if players[choice_of_player].get_health_point() == 0:
        print(BackgroundColors.FAIL + BackgroundColors.BOLD +
              players[choice_of_player].name + " has died." + BackgroundColors.ENDC)
        del players[choice_of_player]


while running:
    print("".center(100, "="))

    print("\n")
    print(BackgroundColors.BOLD +
          "NAME                          HEALTH POINTS                           MAGIC POINTS" + BackgroundColors.ENDC)
    for player in players:
        player.get_stats()
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()
    print("\n\n")

    for player in players:

        player.choose_action()

        player_choice = int(input("Choose player action: ")) - 1

        if player_choice == 0:
            player_damage = player.generate_damage()

            choice_of_enemy = player.choose_target(enemies)
            enemies[choice_of_enemy].take_damage(player_damage)
            print(BackgroundColors.OKGREEN + player.name + " attack to " + enemies[choice_of_enemy].name.strip() + " for " +
                  str(player_damage) + " points of damages." + BackgroundColors.ENDC)

            defeat_enemy(choice_of_enemy)

        elif player_choice == 1:

            player.choose_magic()
            magic_choice = int(input("Choose player magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_damage = spell.generate_spell_damage()

            current_magic_point = player.get_magic_point()

            if spell.cost > current_magic_point:
                print(BackgroundColors.FAIL +
                      "Not enough magic points!".center(100, " ") + BackgroundColors.ENDC)
                continue

            player.reduce_magic_point(spell.cost)

            if spell.type == "White":

                player.heal(magic_damage)
                print(BackgroundColors.OKBLUE + spell.name + " heals for " +
                      str(magic_damage) + " points." + BackgroundColors.ENDC)

            elif spell.type == "Black":

                choice_of_enemy = player.choose_target(enemies)
                enemies[choice_of_enemy].take_damage(magic_damage)
                print(BackgroundColors.OKBLUE + spell.name + " deals " +
                      str(magic_damage) + " points of damage to " + enemies[choice_of_enemy].name.strip() + BackgroundColors.ENDC)

                defeat_enemy(choice_of_enemy)

        elif player_choice == 2:

            player.choose_items()
            item_choice = int(input("Choose player item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["qty"] == 0:
                print("\n" + BackgroundColors.FAIL +
                      "None left..." + BackgroundColors.ENDC)
                continue

            player.items[item_choice]["qty"] -= 1

            if item.type == "potion":

                player.heal(item.points)
                print(BackgroundColors.OKGREEN + item.name + " heals for " +
                      str(item.points) + " health points." + BackgroundColors.ENDC)

            elif item.type == "elixer":

                if item.name == "Mega-Elixer":
                    for p in players:
                        p.health_point = p.max_health_point
                        p.magic_point = p.max_magic_point
                else:
                    player.health_point = player.max_health_point
                    player.magic_point = player.max_magic_point

                print(BackgroundColors.OKGREEN + item.name +
                      " full restores health points / magic points " + BackgroundColors.ENDC)

            elif item.type == "attack":

                choice_of_enemy = player.choose_target(enemies)
                enemies[choice_of_enemy].take_damage(item.points)

                print(BackgroundColors.OKGREEN + item.name + " deals " +
                      str(item.points) + " points of damages to " + enemies[choice_of_enemy].name.strip() + BackgroundColors.ENDC)

                defeat_enemy(choice_of_enemy)

    defeated_enemies = 0
    defeated_player = 0

    for enemy in enemies:
        if enemy.get_health_point() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_health_point() == 0:
            defeated_player += 1

    if defeated_enemies == 2:
        print(BackgroundColors.OKGREEN + BackgroundColors.BOLD +
              "YOU WIN!".center(100, " ") + BackgroundColors.ENDC)
        running = False

    elif defeated_player == 2:
        print(BackgroundColors.FAIL + BackgroundColors.BOLD +
              "YOUR ENEMIES HAVE DEFEATED YOU!".center(100, " ") + BackgroundColors.ENDC)
        running = False

    # ENEMY ATTACK PHASE
    for enemy in enemies:

        enemy_choice = randrange(0, 2)

        if enemy_choice == 0:
            choice_of_player = randrange(0, len(players))
            enemy_damage = enemies[0].generate_damage()
            players[choice_of_player].take_damage(enemy_damage)
            print(BackgroundColors.FAIL + enemy.name.strip() + " attack for " +
                  str(enemy_damage) + " points of damages to " + players[choice_of_player].name.strip() + BackgroundColors.ENDC)

            defeat_player(choice_of_player)

        elif enemy_choice == 1:
            spell, magic_damage = enemy.choose_enemy_spell()
            enemy.reduce_magic_point(spell.cost)

            if spell.type == "White":

                enemy.heal(magic_damage)
                print(BackgroundColors.OKBLUE + spell.name + " heals " + enemy.name.strip() + " for " +
                      str(magic_damage) + " points." + BackgroundColors.ENDC)

            elif spell.type == "Black":

                choice_of_player = randrange(0, len(players))
                players[choice_of_player].take_damage(magic_damage)
                print(BackgroundColors.FAIL + spell.name + " deals " +
                      str(magic_damage) + " points of damage by " + enemy.name.strip() + " to " + players[choice_of_player].name.strip() + BackgroundColors.ENDC)

                defeat_player(choice_of_player)

    # for enemy in enemies:
    #     print(enemy.get_health_point())
    #     print(enemy)
    #     if enemy.get_health_point() == 0:
    #         print("delete " + enemy.name)
    #         del enemy
