class BankAccount:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def dump(self):
        s  = '%s, %s, %s' % \
             (self.name, self.no, self.balance)
        print s
