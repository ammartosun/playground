MIN_BALANCE = 0 

class BankAccount:

    def __init__(self, name, bal):
        self.name = name
        self.__balance = bal
    
    def getBalance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance and amount > MIN_BALANCE:
            print("#Insufficient Funds")
        else:
            self.__balance -= amount
    
    def deposit(self, amount):
        if amount > MIN_BALANCE:
            self.__balance += amount
    
    def report(self):
        print(f"#{self.name}'s account: ${self.__balance}")
    
    def __add__(self,other):
        self.deposit(other.getBalance()) 


acct = BankAccount("Bob", 100)
acct.withdraw(200)      #Insufficient Funds 
acct.deposit(150)
acct.report()           #Bob's account: $250.00 
acct.withdraw(200)
acct.report()           #Bob's account: $50.00
# print(acct.getBalance())
myBalance = acct
print(myBalance)
myBalance.name = "hakan"
# myBalance += 10000000
print(acct.name)
print(acct)
# print(acct.getBalance())

# print(acct.__eq__(myBalance))
# print(acct.__str__())
myBalance = BankAccount("joe", 10000)
print(acct.__add__(myBalance))
acct.report()
