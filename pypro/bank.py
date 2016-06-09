from account import BankAccount
a = BankAccount('ganesh', 12, 2000)
a.deposit(1000)
a.deposit(2330)
a.withdraw(4000)
print a.get_balance()
