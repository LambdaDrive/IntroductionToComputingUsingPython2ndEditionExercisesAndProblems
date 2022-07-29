def base(n, b):
    if n == 0:
        print(n%b, end ='')
    
    else:
        base(n//b, b)
        print(n%b, end = '')

