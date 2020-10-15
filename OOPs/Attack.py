import random


class Enemy:
    health_power = 200

    def __init__(self, attack_low, attack_high):
        self.attack_low = attack_low
        self.attack_high = attack_high

    def get_attack(self):
        print(self.attack_low, self.attack_high)

    def get_health_power(self):
        print(self.health_power)


enemy_lucifer = Enemy(40, 50)
enemy_lucifer.get_attack()
enemy_lucifer.get_health_power()

enemy_damon = Enemy(75, 90)
enemy_damon.get_attack()
enemy_damon.get_health_power()


# player_health_power = 260
# enemy_low_power = 60
# enemy_high_power = 80

# while player_health_power > 0:
#     damage = random.randrange(enemy_low_power, enemy_high_power)
#     player_health_power -= damage
#     if player_health_power <= 30:
#         player_health_power = 30

#     print("Enemy damage:", damage, "Player HP:", player_health_power)

#     if player_health_power > 30:
#         continue

#     print("You have low health. You need to do something.")
#     break
