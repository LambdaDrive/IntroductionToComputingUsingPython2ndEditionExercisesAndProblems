import random
def simul(n):
        listchoice = ['R', 'P', 'S']
        players = {'Player1':0,'Player2':0,'Tie':0}
        choice1 = ''
        choice2 = ''
        for i in range(n):
                choice1 = random.choice(listchoice)
                choice2 = random.choice(listchoice)
                if choice1 == 'R' and choice2 == 'S':
                        players['Player1'] += 1
                elif choice1 == 'S' and choice2 == 'P':
                        players['Player1'] += 1
                elif choice1 == 'P' and choice2 == 'R':
                        players['Player1'] += 1
                elif choice2 == 'R' and choice1 == 'S':
                        players['Player2'] += 1
                elif choice2 == 'S' and choice1 == 'P':
                        players['Player2'] += 1
                elif choice2 == 'P' and choice1 == 'R':
                        players['Player2'] += 1
                else:
                        players['Tie'] += 1
        if players['Player1'] > players['Player2']:
                return 'Player 1'
        elif players['Player2'] > players['Player1']:
                return 'Player 2'
        else:
                return 'Tie'
