n = eval(input('Enter n:'))
conti = 0
mult=10
x = 0
a = n
while(conti==0):
    if a//mult>0:
        x+=1
    else:
        x+=1
        conti = 1
    a = a//mult
mult = 10**(x-1)
for i in range(x):
    if n//int(mult)>0:
        print(n//int(mult))
    else:
        print(n%int(mult))
    n=n%int(mult)
    mult = mult/10


    
    
