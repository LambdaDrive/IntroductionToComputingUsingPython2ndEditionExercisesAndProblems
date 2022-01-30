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
    
