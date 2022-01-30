class Point:
    'class that represents a point in the plane'

#    Added in section 8.2
#    def __init__(self, xcoord=0, ycoord=0):
#        'initialize point coordinates to (xcoord, ycoord)'
#        self.x = xcoord
#        self.y = ycoord

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return a tuple with x and y coordinates of the point'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x and y coordinates by dx and dy'
        self.x += dx
        self.y += dy

#    Added in Section 8.4
#    def __eq__(self, other):
#        'self == other if they have the same coordinates'
#        return self.x == other.x and self.y == other.y
#    def __repr__(self):
#        'return canonical string representation Point(x, y)'
#        return 'Point({}, {})'.format(self.x, self.y)
#
#    Solution to Practice Problem 8.1
#    def getx(self):
#        'return x coordinate'
#        return self.xcoord



class Animal:
    'represents an animal'

#    Solution to Practice Problem 8.4
#    def __init__(self, species='animal', language='make sounds'):
#        self.spec = species
#        self.lang = language

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))
        


class Bird(Animal):
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print('{}! '.format(self.language) * 3)



class EmptyQueueError(Exception):
    pass

class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        self.q = []

    def isEmpty(self):
        'returns True if queue is empty, False otherwise'
        return (len(self.q) == 0)

    def enqueue (self, item):
        'insert item at rear of queue'
        return self.q.append(item)

    def dequeue(self):
        'remove and return item at front of queue'
        return self.q.pop(0)

#   Added in Section 8.4
#    def __init__(self, q=None):
#        'initialize queue based on list q, default is empty queue'
#        if q == None:
#            self.q = []
#        else:
#            self.q = q
#
#    def __eq__(self, other):
#        '''return True if queues self and other contain
#           the same items in the same order'''
#        return self.q == other.q
#
#    def __len__(self):
#        'returns number of items in queue'
#        return len(self.q)
#
#    def __repr__(self):
#        'return canonical string representation of queue'
#        return 'Queue({})'.format(self.q)
#
#    Added in Section 8.6
#    def dequeue(self):
#        'remove and return item at front of queue'
#        if len(self) == 0:
#            raise EmptyQueueError('dequeue from empty queue')
#        return self.q.pop(0)
#
#    Solution to Problem 8.9
#    def dequeue(self):
#        '''removes and returns item at front of the queue
#           raises KeyboardInterrupt exception if queue is empty'''
#        if len(self) == 0:
#            raise KeyboardInterrupt('dequeue from empty queue')
#
#        return self.q.pop(0)



class Representation(object):
    def __repr__(self):
        return 'canonical string representation'
    def __str__(self):
        return 'Pretty string representation.'



import random
class MyList(list):
    'a subclass of list that implements method choice'

    def choice(self):
        'return item from list chosen uniformly at random'
        return random.choice(self)


class Super:
    'a generic class with one method'
    def method(self):                     # the Super method
        print('in Super.method')

class Inheritor(Super):
    'class that inherits method'
    pass

class Replacer(Super):
    'class that overrides method'
    def method(self):
        print('in Replacer.method')

class Extender(Super):
    'class that extends method'
    def method(self):
        print('starting Extender.method')
        Super.method(self)                # calling Super method
        print('ending Extender.method')



class Queue2(list): 
    'a queue class, subclass of list'

    def isEmpty(self):
        'returns True if queue is empty, False otherwise'
        return (len(self) == 0)

    def dequeue(self):
        'remove and return item at front of queue'
        return self.pop(0)

    def enqueue (self, item):
        'insert item at rear of queue'
        return self.append(item)



##################################
# Solutions to Practice Problems #
##################################


# Practice Problem 8.3
class Rectangle:
    'class that represents rectangles'

    def setSize(self, xcoord, ycoord):
        'constructor'
        self.x = xcoord
        self.y = ycoord

    def perimeter(self):
        'returns perimeter of rectangle'
        return 2 * (self.x + self.y)

    def area(self):
        'returns area of rectangle'
        return self.x * self.y


# Practice Problem 8.8
class Vector(Point):
    'a 2D vector class'

    def __mul__(self, v):
        'vector product'
        return self.x * v.x + self.y * v.y

    def __add__(self, v):
        'vector addition'
        return Vector(self.x + v.x, self.y + v.y)

    def __repr__(self):
        'returns the canonical string representation'
        return 'Vector{}'.format(self.get())
