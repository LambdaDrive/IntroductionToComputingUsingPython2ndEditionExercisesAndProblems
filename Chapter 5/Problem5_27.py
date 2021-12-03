def letter2number(grade):
    number = 0
    if grade[0] == 'A':
        number = 4
    if grade[0] == 'B':
        number = 3
    if grade[0] == 'C':
        number = 2
    if grade[0] == 'D':
        number = 1
    if len(grade) > 1:
        if grade[1] == '+':
            number += 0.3
        if grade[1] == '-':
            number -= 0.3
    return number
