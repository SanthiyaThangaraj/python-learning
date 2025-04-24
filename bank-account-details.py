#Create a class BankAccount with attributes account_holder, balance. Include methods to deposit, withdraw, and check balance.

class bankAccount:
    def __init__(self, acc_hold, balance):
        self.acc_hold=acc_hold
        self.balance=balance

    def action(self):
        activity=input("Enter your activity (deposit/withdraw/check balance): ")
        match(activity):
            case "deposit":
                amount=int(input("Enter deposit amount: "))
                self.balance+=amount
                print(f"{amount} is added to {self.acc_hold}'s account")
            case "withdraw":
                amount=int(input("Enter withdraw amount: "))
                self.balance-=amount
                print(f"{amount} is withdraw from {self.acc_hold}'s account")
            case "check balance":
                print(f"Balance {self.balance} is in {self.acc_hold}'s account")

money=bankAccount("Santhiya", 1000)
money.action()
            
