class Animal:

    def __init__(self, talk):

        self.voice = talk

    def speak(self):
        return self.voice

class Mammal(Animal):

    pass

class Cat(Mammal):

    def __init__(self):

        self.voice = 'Meeow'

class Dog(Mammal):

    def __init__(self):

        self.voice = 'Auau'

class Primate(Mammal):

    def __init__(self):
        self.voice = 'Ugabuga'

class Hacker(Primate):

    def __init__(self):
        self.voice = 'Hello world!'

