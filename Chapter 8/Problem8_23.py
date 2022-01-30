import math
class Point:

    def __init__(self,x=0, y=0):
        self.cordx = x
        self.cordy = y

class Segment:

    def __init__(self, point1, point2):
        self.ponto1 = point1
        self.ponto2 = point2

    def length(self):
        seg = math.sqrt(((self.ponto2.cordx - self.ponto1.cordx)**2)+((self.ponto2.cordy - self.ponto1.cordy)**2))
        return seg
    
    def slope(self):
        slop = ((self.ponto2.cordx - self.ponto1.cordx)/(self.ponto2.cordy - self.ponto1.cordy))
        return slop
