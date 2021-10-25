from unittest import TestCase


class Account():
    def __init__(self, accnumber, opening_date, interest_rate, balance):
        pass

    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass

    def transfer(self, amount, accountnumber):
        pass


class TestAccount(TestCase):
    def __init__(self):
        self.account = Account()

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.balance(500),500)

    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.balance(-500), 0)

    def test_transfer(self):
        acc = Account(123,"01-01-2020",3,500)
        self.account.transfer(100,acc)
        self.assertEqual(self.balance(-100),acc.balance(100))