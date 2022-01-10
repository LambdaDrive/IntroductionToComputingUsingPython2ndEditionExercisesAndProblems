import random
def diceprob(roll):
    rolls = 0
    total = 0
    while rolls != 100:
        dice1, dice2 = random.randrange(1, 7),random.randrange(1, 7)
        if dice1 + dice2 == roll:
            rolls += 1
        total += 1
    print('It took {} rolls to get 100 rolls of {}'.format(total, roll))
    
