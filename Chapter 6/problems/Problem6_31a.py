import random
def craps():
    result = 0
    while result != 7 or result != 11 or result != 2 or result != 3 or result != 12:
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        result = dice1 + dice2
        if result == 7 or result == 11:
            return 1
        if result == 2 or result == 3 or result == 12:
            return 0

    
