def geometric(array):
    division = False
    for i in range(len(array) - 4):
        if array[i]/array[i+1] == array[i+2]/array[i+3]:
            division = True
    return division
