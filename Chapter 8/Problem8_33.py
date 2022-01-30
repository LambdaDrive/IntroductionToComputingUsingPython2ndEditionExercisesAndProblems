class Pseudorandom:

    def __init__(self, a, x, c, m):
        self.a = a
        self.x = x
        self.c = c
        self.m = m

    def next(self):
        self.x = (self.a*self.x+self.c)%self.m
        return self.x
