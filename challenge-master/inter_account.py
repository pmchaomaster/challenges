class Account(object):
    def __init__(self,acctNumner, balance):
        self.acctNumber = acctNumner
        self.balance=balance

    def __str__(self):
        return "Account numner:" + str(self.acctNumner)+ "\n" +\
            "Balance: "+str(self.balance)

class Checking(Account):
    def __init__(self, acctNumner,balance, fee):
        Account.__init__(self, acctNumner, balance)
        self.fee=fee

    def __str__(self):
        retStr = "Account type: Checking\n"
        retstr += Account.__str__(self)
        return retStr

    def getFee(self):
        return self.fee

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if  amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount - self.fee

class Saving(Account):
    def __init__(self,acctNumner,balance):
        Account.__init__(self, acctNumber, balance):
        Accout.__init__(acctNumber, balance)

        def __str__(self):
            retStr="Account type: Savings\n"
            retStr += Account.__str__(self)
            return retStr

        def deposite (self, amount):
            self.balance += amount

        def withdraw(self, amount):
            if amount > self.balance:
                print ("Insufficient funds")
            else:
                self.balance = self.balance-amount

sa = Saving















