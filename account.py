class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def open(self):
        self.is_open = True

    def get_balance(self):
        if not self.is_open:
            raise ValueError('Cannot access account!')

        return self.balance

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('Cannot access account!')

        if amount <= -1:
            raise ValueError('Error: Put valid amount')

        self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('Cannot access account!')
            
        if amount > self.balance:
            raise ValueError('Error: Insufficient funds')

        if amount <= -1:
            raise ValueError('Error: Put valid amount')

        self.balance -= amount

    def close(self):
        self.is_open = False
