class BankAccount:

    def __init__(self,money=0):
        self.money = money

    def withdraw(self, amount):
        self.money -= amount

    def deposit(self, amount):
        self.money += amount

    def balance(self):
        return self.money

    
