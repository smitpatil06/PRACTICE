class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print(f"Account Balance: ₹{self.balance:.2f}")

    def apply_interest(self, rate):
        new_balance = self.balance + (self.balance * rate / 100)
        return BankAccount(new_balance)


account1 = BankAccount(10000)
print("Original Account:")
account1.display()

# Apply 5% interest
account2 = account1.apply_interest(5)
print("Account After Interest:")
account2.display()
