import random
def war():
    battles = 0
    wars = 0
    twowar = 0
    choice1 = 0
    choice2 = 0
    wardeck1 = []
    wardeck2 = []
    baralho = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
               14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
               14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
               14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    random.shuffle(baralho)
    player1 = []
    player2 = []
    for i in range(len(baralho)):
        if i < (len(baralho)//2) - 1:
            player1.append(baralho[i])
        else:
            player2.append(baralho[i])
    while len(player1) != 0 or len(player2) != 0:
        if len(player1) == 0 or len(player2) == 0:
            break
        elif player1[-1] > player2[-1]:
            random.shuffle(player1)
            player1.insert(0, player2[-1])
            player2.pop()
            battles += 1
        elif player2[-1] > player1[-1]:
            random.shuffle(player2)
            player2.insert(0, player1[-1])
            player1.pop()
            battles += 1
        else:
            wars += 1
            war = True
            if len(player1) > 3 or len(player2) > 3:
                if len(player1) < len(player2):
                    for i in range(-2, -len(player1), -1):
                        wardeck1.append(player1[i])
                        wardeck2.append(player2[i])
                else:
                    for i in range(-2, -len(player2), -1):
                        wardeck1.append(player1[i])
                        wardeck2.append(player2[i])    
            elif len(player1) < 2 or len(player2) < 2:
                wardeck1.append(player1[-1])
                wardeck2.append(player2[-1])
            elif len(player1) <= 3 or len(player2) <= 3:
                if len(player1) < len(player2):
                    for i in range(-len(player1), 0):
                        wardeck1.append(player1[i])
                        wardeck2.append(player2[i])
                else:
                    for i in range(-len(player2), 0):
                        wardeck1.append(player1[i])
                        wardeck2.append(player2[i])    
            while war ==  True:    
                if len(player1) == 0 or len(player2) == 0:
                    war = False
                    break
                if len(wardeck1) > 0 and len(wardeck2) > 0:
                    choice1 = random.choice(wardeck1)
                    choice2 = random.choice(wardeck2)
                elif len(wardeck1) == 0 or len(wardeck2) == 0:
                    war = False
                    break
                if choice1 > choice2:
                    if len(player2) > 4:
                        for i in range(-1, -4, -1):
                            random.shuffle(player1)
                            player1.insert(0, player2[i])
                            player2.remove(player2[i])
                    elif len(player2) < 2 :
                        random.shuffle(player1)
                        player1.insert(0, player2[-1])
                        player2.pop()
                    elif len(player2) <= 3 :
                        for i in range(-(len(player2)), 0):
                            random.shuffle(player1)
                            player1.insert(0, player2[i])
                            player2.pop()
                    battles += 1
                    war = False
                elif choice2 > choice1:
                    if len(player1) > 4:
                        for i in range(-1, -4, -1):
                            random.shuffle(player2)
                            player2.insert(0, player1[i])
                            player1.remove(player1[i])
                    elif len(player1) < 2 :
                        random.shuffle(player1)
                        player2.insert(0, player1[-1])
                        player1.pop()
                    elif len(player1) <= 3 :
                        for i in range(-(len(player1)), 0):
                            random.shuffle(player2)
                            player2.insert(0, player1[i])
                            player1.pop()
                    battles += 1
                    war = False
                else:
                    if len(wardeck1) > 0 and len(wardeck2) > 0:
                        wardeck1.remove(choice1)
                        wardeck2.remove(choice2)
                        battles += 1
                    else:
                        twowar += 1
                        if len(player1) > 7 or len(player2) > 7:
                            for i in range(-5, -8, -1):
                                wardeck1.append(player1[i])
                                wardeck2.append(player2[i])
                        elif len(player1) < 2 or len(player2) < 2:
                            wardeck1.append(player1[-1])
                            wardeck2.append(player2[-1])
                        elif len(player1) <= 3 or len(player2) <= 3:
                            if len(player1) < len(player2):
                                for i in range(-len(player1), 0):
                                    wardeck1.append(player1[i])
                                    wardeck2.append(player2[i])
                            else:
                                for i in range(-len(player2), 0):
                                    wardeck1.append(player1[i])
                                    wardeck2.append(player2[i])
                        choice1 = random.choice(wardeck1)
                        choice2 = random.choice(wardeck2)
                        if choice1 > choice2:
                            if len(player2) > 3:
                                for i in range(-1, -4, -1):
                                    random.shuffle(player1)
                                    player1.insert(0, player2[i])
                                    player2.remove(player2[i])
                            elif len(player2) < 2 :
                                random.shuffle(player1)
                                player1.insert(0, player2[-1])
                                player2.pop()
                            elif len(player2) <= 3 :
                                for i in range(-(len(player2)), 0):
                                    random.shuffle(player1)
                                    player1.insert(0, player2[i])
                                    player2.pop()
                            battles += 1
                            war = False
                        elif choice2 > choice1:
                            if len(player1) > 3:
                                for i in range(-1, -4, -1):
                                    random.shuffle(player2)
                                    player2.insert(0, player1[i])
                                    player1.remove(player1[i])
                            elif len(player1) < 2 :
                                random.shuffle(player1)
                                player2.insert(0, player1[-1])
                                player1.pop()
                            elif len(player1) <= 3 :
                                for i in range(-(len(player1)), 0):
                                    random.shuffle(player2)
                                    player2.insert(0, player1[i])
                                    player1.pop()
                            battles += 1
                            war = False
                        else:
                            if len(wardeck1) > 0 and len(wardeck2) > 0:
                                wardeck1.remove(choice1)
                                wardeck2.remove(choice2)
                            battles += 1    
                                                        
            wardeck1.clear()
            wardeck2.clear()
    result = (battles, wars, twowar)
    return result
