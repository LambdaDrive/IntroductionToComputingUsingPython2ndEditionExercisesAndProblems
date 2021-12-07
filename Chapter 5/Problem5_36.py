def prime(number):
    numdiv = 0
    for i in range(1, number + 1):
        if number % i == 0:
            numdiv += 1
    if numdiv == 2:
        return True
    return False
