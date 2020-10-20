import random

running = True
lose = 0

while running:
    player = input("what's your hand: ").lower()
    computer = random.choice(["rock", "paper", "scissor"])
    if player == computer:
        print("You won!")
        running = False
    else:
        lose += 1
        print("You lose!")
        continue

print("You lose in game " + str(lose) + " times.")
