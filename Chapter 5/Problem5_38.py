def collatz(x):
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = int(x/2)
        else:
            x = (3 * x) + 1
    print(x)            
