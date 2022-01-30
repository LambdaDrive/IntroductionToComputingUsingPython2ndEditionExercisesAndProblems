import random
class Craps:

    def __init__(self):

        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        result = dice1  + dice2
        if result == 7 or result == 11:
            stresult = 'You won!'
        elif result == 2 or result == 3 or result == 12:
            stresult = 'You lost!'
        else:
            stresult = 'Throw for Point.'
        print('Throw total: {}. {}'.format(result, stresult))

    def forPoint(self):

        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        result = dice1  + dice2
        if result == 7 or result == 11:
            stresult = 'You won!'
        elif result == 2 or result == 3 or result == 12:
            stresult = 'You lost!'
        else:
            stresult = 'Throw for Point.'
        print('Throw total: {}. {}'.format(result, stresult))

