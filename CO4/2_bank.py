class Bank:
    def __init__(self, acno, name, type, bal):
        self.acno = acno
        self.name = name
        self.type = type
        self.bal = bal

    def deposite(self, amount):
        self.bal = self.bal + amount
        print("amount deposited successfully")
        return self.bal

    def withdraw(self, amount):
        if amount > self.bal:
            print("insufficient balance")
            return self.bal
        else:
            self.bal = self.bal - amount
            print("amount withdrawed successfully")
            return self.bal


b = Bank(1001, "jazz", "savings", 2500)
damount = float(input("Enter the amount to be deposited:"))
print("Account balance:", b.deposite(damount))
wamount = float(input("Enter the amount to be withdrawn:"))
print("Account balance:", b.withdraw(wamount))
