import math
def points(x1, y1, x2, y2):
    
    distance = str(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
    if x1 == x2:
        slope = 'infinity'
    else:
        slope = str((y2 - y1)/(x2 - x1))
    print('The slope is '+slope+' and the distance is '+distance)
