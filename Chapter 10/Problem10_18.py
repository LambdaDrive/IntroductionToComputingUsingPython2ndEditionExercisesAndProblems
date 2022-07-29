def silly(n):
    if n > 0:
        print('?')
        n -= 1
        silly(n)
        print('!')
        
