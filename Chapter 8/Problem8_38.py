import time
class Person:

    def __init__(self, name, byear):

        self.nome = name
        self.birthyear = byear

    def age(self):

        idade = (int(time.strftime('%Y', time.localtime()))) - self.birthyear
        return idade

    def name(self):

        return self.nome
    
class Instructor(Person):

    def __init__(self, name, byear, degree):

        self.nome = name
        self.birthyear = byear
        self.titulo = degree

    def degree(self):

        return self.titulo

class Student(Person):

    def __init__(self, name, byear, grad):

        self.nome = name
        self.birthyear = byear
        self.graduation = grad

    def major(self):

        return self.graduation
