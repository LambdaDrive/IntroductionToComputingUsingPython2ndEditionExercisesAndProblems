class NegativeBalanceError(Exception):
    pass

class OverdraftError(Exception):
    pass

class DepositError(Exception):
    pass

class BankAccount3:

    def __init__(self,money=0):
         if money < 0:
            raise NegativeBalanceError('Account created with negative balance {}'.format(money))
         self.money = money
       
    def withdraw(self, amount):
        if amount > self.money:
            raise OverdraftError('Operation would result in negative balance {}'.format(self.money -amount ))
        self.money -= amount

    def deposit(self, amount):
        if amount < 0:
            raise DepositError('Negative deposit {}'.format(amount))
        self.money += amount

    def balance(self):
        return self.money

    
