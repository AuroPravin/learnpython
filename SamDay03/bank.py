class bankac:
    def __init__(self,accountno,bal=0):
        self.accountno=accountno
        self.bal=bal

    def deposit(self,amount):
        self.bal+=amount
        print(f"deposit {amount}.new balance:{self.bal}")

    def withdraw(self,amount):
        if amount<=self.bal:
            self.bal=self.bal-amount
            print(f"withdrew {amount}. new balance: {self.bal}")
        else:
            print("insufficient funds")

    def display(self):
        print(f"acc number: {self.accountno}\nBalance: {self.bal}")

accountno=input("Enter ur account number :")
initialbal=float(input("Enter your initial balance :"))
account=bankac(accountno,initialbal)

while True:
    print("\n 1. Deposit")
    print("\n 2. Withdraw")
    print("\n 3. Display Balance")
    print("\n 4.Exit")
    choice=input("Enter ur choice: ")

    if choice=="1":
        amount=float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif choice=="2":
        amount=float(input("Enter the amount to withdraw :"))
        account.withdraw(amount)
    elif choice=="3":
        account.display()
    elif choice=="4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again")

    