class Stat:

    def __init__(self):
        self.numbers = []

    def __len__(self):
        return len(self.numbers)

    def __contains__(self, key, /):
        return key in self.numbers

    def add(self, number):
        self.numbers.append(number)

    def min(self):
        return min(self.numbers)

    def max(self):
        return max(self.numbers)

    def sum(self):
        return sum(self.numbers)

    def mean(self):
        return (sum(self.numbers)/len(self.numbers))

    def clear(self):
        self.numbers.clear()

        
