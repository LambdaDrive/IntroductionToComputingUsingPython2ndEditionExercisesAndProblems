def reverse_int(number):
    'reverse a 3 digit number'
    newnumber = 0
    for i in range(3):
        reversing=number%10
        newnumber += reversing
        number = number//10
        if i!=2:
            newnumber = newnumber*10
    return newnumber
