class Worker:

    def __init__ (self, stringname, hourlypay):
        self.name = stringname
        self.wage = hourlypay

    def changeRate(self, newrate):
        self.wage = newrate

    def pay(self, hours):
        print('Not Implemented')

class HourlyWorker(Worker):

     def pay(self, hours):
         money = 0
         for i in range(1, hours + 1):
             if i <= 40:
                 money += self.wage
             else:
                 money += (self.wage) * 2
         return money

class SalariedWorker(Worker):

    def pay(self, hours=0):
        return self.wage * 40
    
    
