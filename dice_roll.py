from random import randint

def dice_roll():
    count = 0
    trials = 100000
    for _ in range(100000):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        if (dice1 * dice2) % 2 == 0:
            count += 1
    return count*1.0 / trials


print(dice_roll())

