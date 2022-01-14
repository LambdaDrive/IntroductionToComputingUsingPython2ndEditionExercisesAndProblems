import random
def game(n):
    number1 = 0
    number2 = 0
    correct = 0
    for i in range(n):
        number1 = random.randrange(0, 9)
        number2 = random.randrange(0, 9)
        try:
            answer = int(input('{} + {} ='.format(number1, number2)))
        except ValueError:
            print('Please write you answer using digits 0 through 9. Try again!')
            answer = int(input('Enter answer:'))
        if answer == (number1 + number2):
            correct += 1
            print('Correct.')
        else:
            print('Incorrect.')
    print('You got {} correct answers out of {}'.format(correct, n))
