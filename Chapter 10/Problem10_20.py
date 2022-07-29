def rgcd(a, b):
    if b == 0:
        return a
    else:
        return rgcd(b, a%b)
