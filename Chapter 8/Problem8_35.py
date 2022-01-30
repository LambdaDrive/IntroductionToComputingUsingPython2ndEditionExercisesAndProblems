class Stack(object):

    def __init__(self):
        self.pilha = []

    def __len__(self):
        return len(self.pilha)

    def __repr__(self):
        return str(self.pilha)

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        return self.pilha.pop()

    def isEmpty(self):
        return len(self.pilha) == 0
