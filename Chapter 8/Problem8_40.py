class BankAccount2:

    def __init__(self,money=0):
         if money < 0:
            raise ValueError('Illegal balance')
         self.money = money
       
    def withdraw(self, amount):
        if amount > self.money:
            raise ValueError('Overdraft')
        self.money -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Negative deposit')
        self.money += amount

    def balance(self):
        return self.money

    
