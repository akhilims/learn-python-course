# Methods: an Account that remembers
# Every cell of the notebook, in order, as one script (run: python Methods__an_Account_that_remembers.py)

# Writing a method: the Account class

class Account:
    def __init__(self):
        self.balance = 0
    def deposit(self, n):
        self.balance = self.balance + n

# Calling a method with a dot

acc = Account()
acc.deposit(50)
print(acc.balance)

# The object remembers between calls

acc.deposit(25)
print(acc.balance)
