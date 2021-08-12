def collision(x1, y1, r1, x2, y2, r2):
    for i in range(-int(r1), int(r1)):
        for a in range(-int(r2), int(r2)):
            pontox1 = x1+i
            pontoy1 = y1+i
            pontox2 = x2+a
            pontoy2 = y2+a
            if pontox1==pontox2 or pontoy1==pontoy2:
                return True
    return False
