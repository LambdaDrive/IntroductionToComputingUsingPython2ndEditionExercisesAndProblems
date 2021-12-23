def primeFac(integer):
    primes = []
    numprime = 1
    divisors = 0
    factorization = []
    while integer != 1:
        for i in range(1 ,numprime + 1):
            if numprime % i == 0:
                divisors += 1
        if divisors == 2:
            primes.append(numprime)
        divisors = 0
        if len(primes) >= 1:
            for number in primes:
                if integer % number == 0:
                    integer = integer // number
                    factorization.append(number)
        numprime += 1
    return factorization
