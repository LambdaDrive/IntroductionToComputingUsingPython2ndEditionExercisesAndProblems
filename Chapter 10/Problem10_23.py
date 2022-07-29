def tough(iden, number):
    if number > 0:
        tough(iden, number // 2)
        print(' ' * iden + '*'*number)
        tough(iden + number // 2, number // 2)

