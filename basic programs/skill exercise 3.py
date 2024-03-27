class BankAccount:
    def _init_(self,accountNumber,name,balence):
        self.accountNumber=accountNumber
        self.name=name
        self.balence=balence
    def deposit(self,amount):
        if amount>0:
            self.balence+=amount
            print(f"Deposit of Rs.{amount}successful.")
        else:
            print("Invalid deposit amount")
    def withdrawal(self,amount):
        if 0<amount<=self.balence:
            self.balence-=amount
            print(f"withdrawal of Rs{amount}successful.")
    def bank_fees(self):
        fees=0.05*self.balence
        self.balence-=fees
        print(f"Bank fees of Rs.{fees}applied.")
    def display(self):
        print(f"Account Number:{self.accountNumber}")
        print(f"Account Holder:{self.name}")
        print(f"Balence:Rs.{self.balence}")
account1=BankAccount(accountNumber=1234,name="john",balence=1000)
account1.display()
account1.deposit(500)
account1.withdrawal(200)
account1.bank_fees()
account1.display()