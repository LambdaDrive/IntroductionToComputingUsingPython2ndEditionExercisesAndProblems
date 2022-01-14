def inValues():
    soma = 0
    error = 0
    while error < 2:
        try:
            number = float(input('Please enter a number:'))
        except ValueError:
            print('Error. Please re-enter the value.')
            try:
                number = float(input('Please enter a number:'))
            except ValueError:
                error = 2
                print('Two errors in a row. Quitting ...')
        soma += number
        if number == 0:
            return soma

                
