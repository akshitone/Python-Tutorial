from random import choice
from classes.game import Gamer, BackgroundColors

magic = [
    {"name": "Fire", "cost": 15, "damage": 60},
    {"name": "Thunder", "cost": 10, "damage": 50},
    {"name": "Blizzard", "cost": 5, "damage": 40}
]

player_one = Gamer(460, 65, 60, 34, magic)
enemy_one = Gamer(1200, 65, 45, 25, magic)

running = True
print(BackgroundColors.FAIL + BackgroundColors.BOLD +
      "AN ENEMY ATTACK!" + BackgroundColors.ENDC)
while running:
    print("".center(30, "="))
    player_one.choose_action()
    choice = int(input("Choose your action: "))
    index = choice - 1
    if index == 0:
        damage = player_one.generate_damage()
        enemy_one.take_damage(damage)
        print("Damage: " + str(damage) + " Enemy Health Point: " +
              str(enemy_one.get_health_point()))
