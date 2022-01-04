import random
def testCraps(n):
    wins = 0
    for i in range(n):
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        result = dice1 + dice2
        if result == 7 or result == 11:
            wins += 1
    return wins/n
