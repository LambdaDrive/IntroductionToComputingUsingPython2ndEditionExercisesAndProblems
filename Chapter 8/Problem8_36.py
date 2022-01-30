class PriorityQueue:

    def __init__(self):
        self.fila = []

    def __len__(self):
        return len(self.fila)

    def insert(self, value):
        self.fila.append(value)

    def min(self):
        return min(self.fila)

    def removeMin(self):
        self.fila.remove(min(self.fila))

    def isEmpty(self):
        return len(self.fila) == 0

    
