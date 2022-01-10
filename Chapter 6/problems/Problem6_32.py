import random
def manhattan(rows, col):
    grid = []
    direction = ['N', 'S', 'E', 'W']
    for a in range(rows):
        grid.append([])
        for i in range(col):
            grid[a].append(0)
    positiony = rows//2
    positionx = col//2
    choice = ''
    while positiony > 0 and positiony <= rows-1 and positionx > 0 and positionx <= col-1:
        grid[positiony][positionx] += 1
        choice = random.choice(direction)
        if choice == 'N':
            positiony -= 1
        elif choice == 'S':
            positiony += 1
        elif choice == 'E':
            positionx += 1
        elif choice == 'W':
            positionx -= 1
    for line in grid:
        print(line)
