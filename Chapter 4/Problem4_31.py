def duplicate(filename):
    file = open(filename)
    content = file.read()
    file.close()
    content = content.split()
    lenum = len(content)
    for z in range(0, lenum-1):
        for i in range(lenum-1, 0 , -1):
            if i==z:
                pass
            elif content[i]==content[z]:
                return True
    return False
