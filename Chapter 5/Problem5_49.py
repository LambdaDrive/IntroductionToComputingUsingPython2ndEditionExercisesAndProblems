def heron(n, error):
    tries = []
    prev = 1.0
    while True:
        tries.append(1/2*(prev + n / prev))
        if len(tries)>1:
            for i in range(len(tries)-1):
                dim = tries[i] - tries[i+1]
            if abs(dim) <= error:
                return tries[-1]
        prev = tries[-1]
