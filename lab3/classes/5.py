class Bank:
    def __init__(self, account, money):
        self.account = account
        self.money = money

    def balance(self):
        return self.money
    
    def owner(self):
        return self.account
    
    def deposit(self, amount):
        self.money += amount
    
    def withdraw(self, amount):
        if self.money >= amount:
            self.money -= amount
            print(f"withdrawn = {amount}, Remaining = {self.money}")
        else:
            print("insufficient funds")

bank = Bank("Azhar",5000)

print(bank.balance())  
print(bank.owner())   

bank.deposit(1000)  
bank.withdraw(3000)  
bank.withdraw(2000)