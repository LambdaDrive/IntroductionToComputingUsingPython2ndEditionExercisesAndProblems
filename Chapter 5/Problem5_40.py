def approxPi(error):
    divup = 4
    div = 1
    div1 =1
    soma1 = 0
    soma2 = 0
    step = 1
    step1 = 1
    times = 1
    while soma1 - soma2 != error:
        for i in range(times - 1):
            if step1 % 2 == 0:
                soma2 -= 4/div1
            else:
                soma2 += 4/div1
            div1 += 2
            step1 += 1
        for i in range(times):
            if step % 2 == 0:
                soma1 -= 4/div
            else:
                soma1 += 4/div
            div += 2
            step += 1
        times += 1
        div1 = 1
        div = 1
        step1 = 1
        step = 1
        if abs(soma1 - soma2) <= error:
            return soma1
        soma1 = 0
        soma2 = 0
