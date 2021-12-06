def pixels(twodlist):
    pixels = 0
    for i in range(len(twodlist)):
        for a in range(len(twodlist[0])):
            if twodlist[i][a] > 0:
                pixels += 1
    return pixels
