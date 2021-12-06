def statement(floatlist):
    account = [0, 0]
    for number in floatlist:
        if number > 0:
            account[0] += number
        else:
            account[1] += number
    return account
