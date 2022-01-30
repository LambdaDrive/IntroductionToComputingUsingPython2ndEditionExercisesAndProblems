import math
class Polygon:

    def __init__(self, sides, lenght):
        self.n = sides
        self.s = lenght

    def perimeter(self):
        return self.n * self.s

    def area(self):
        return (((self.s**2) * self.n)/(4 * (math.tan(math.pi/self.n))))
    
        
