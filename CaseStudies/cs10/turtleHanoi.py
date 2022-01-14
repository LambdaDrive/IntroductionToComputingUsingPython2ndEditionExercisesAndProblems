from turtle import Turtle, Screen



class Disk(Turtle):
    'a Tower of Hanoi disk class'

    def __init__(self, n):
        'initializes disk n'
        Turtle.__init__(self, shape='square', visible=False)
        self.penup()                # moves should not be traced
        self.sety(300)              # moves are above the pegs
        self.shapesize(1, 1.5*n, 2) # set disk diameter
        self.fillcolor(1, 1, 1)     # disk is white
        self.showturtle()           # disk is made visible



class Peg(Turtle, list):
    'a Tower of Hanoi peg class, inherits from Turtle and list'
    pos = -200                    # x-coordinate of next peg

    def __init__(self, n):
        'initializes a peg for n disks'

        Turtle.__init__(self, shape='square',visible=False)
        self.penup()              # peg moves should not be traced
        self.shapesize(n*1.25,.75,1) # height of peg is function
                                     # of the number of disks
        self.sety(12.5*n)         # bottom of peg is y=0
        self.x = Peg.pos          # x-coord of peg
        self.setx(self.x)         # peg moved to its x-coord
        self.showturtle()         # peg made visible
        Peg.pos += 200            # position of next peg

    def push(self, disk):
        'pushes disk around peg'

        disk.setx(self.x)         # moves disk to x-coord of peg
        disk.sety(10+len(self)*25)# moves disk vertically to just
                                  # above the topmost disk of peg
        self.append(disk)         # adds disk to peg

    def pop(self):
        'removes top disk from peg and returns it'

        disk = list.pop(self)     # removes disk from peg
        disk.sety(300)            # lifts disk above peg
        return disk



def move_disk(from_peg, to_peg):
    'moves top disk from from_peg to to_peg'
    disk = from_peg.pop()
    to_peg.push(disk)



def hanoi(n, peg1, peg2, peg3):
    'move n disks from peg1 to peg3 using peg2'

    # base case: n == 0. Do nothing

    if n > 0: # recursive step 
        hanoi(n-1, peg1, peg3, peg2) # recursively move top n-1 disks
                                     # from peg1 to peg2
        move_disk(peg1, peg3)        # move largest disk
                                     # from peg1 to peg2
        hanoi(n-1, peg2, peg1, peg3) # recursively move n-1 disks
                                     # from peg2 to peg3



def play(n):
    'shows the solution of a Tower of Hanoi problem with n disks'
    screen = Screen()
    Peg.pos = -200
    p1 = Peg(n)
    p2 = Peg(n)
    p3 = Peg(n)

    for i in range(n):      # disks are pushed around peg 1
        p1.push(Disk(n-i))  # in decreasing order of diameter       

    hanoi(n, p1, p2, p3)

    screen.bye()
