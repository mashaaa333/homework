import random

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        deposit_amount = float(input("Input amount to add:\t"))
        current_amount = self.balance + deposit_amount
        return "Success! Your current balance is:", current_amount

    def withdraw(self):
        withdraw_amount = float(input("Input amount to withdraw:\t"))
        if withdraw_amount > self.balance:
            return "Insufficient balance"
        else:
            return "Success! Your current balance is:", self.balance - withdraw_amount

    def print_balance(self):
        return f"Your current balance is {self.balance}"

try:
    account_number = int(input("Input your account number:\t"))
    if account_number == 0000:
        balance = random.randint(0, 500)
        transaction_type = input("\nV- view balance\n D- deposit\n W- withdraw\n Select your transaction type:")
        account = BankAccount(account_number, balance)
        if transaction_type.upper() == "V":
            print(account.print_balance())
        elif transaction_type.upper() == "D":
            print(account.deposit())
        elif transaction_type.upper() == "W":
            print(account.withdraw())
        else:
            print("Error, please try again")
    else:
        print("Invalid account number.")
except ValueError:
    print("Invalid account number. Please input a valid account number.")


