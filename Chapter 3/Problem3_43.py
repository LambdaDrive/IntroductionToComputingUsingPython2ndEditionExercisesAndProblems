def hit(xcircle, ycircle, rcircle, xpoint, ypoint):
    for i in range(-rcircle, rcircle+1):
        for a in range(-rcircle, rcircle+1):
            if xpoint==(xcircle+i) and ypoint==(ycircle+a):
                return True
    return False
