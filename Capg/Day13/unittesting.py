class BankAccount:
    def __init__(self, owner, balance=0.0):
        """
        Initializes the bank account with the owner's name and initial balance.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a given amount to the bank account.
        """
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a given amount from the bank account if sufficient balance exists.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            return self.balance
        

import unittest
from __main__ import BankAccount  # Import the class from the current module

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """
        This method runs before every test case. It sets up a fresh account.
        """
        self.account = BankAccount("John Doe", 100.0)  # Initial balance is 100

    def test_deposit_valid(self):
        """
        Test case for depositing a valid amount.
        """
        self.assertEqual(self.account.deposit(50), 150)  # Balance should be 150

    def test_deposit_invalid(self):
        """
        Test case for depositing a negative amount, which should raise an error.
        """
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_withdraw_valid(self):
        """
        Test case for withdrawing a valid amount.
        """
        self.assertEqual(self.account.withdraw(30), 70)  # Balance should be 70

    def test_withdraw_insufficient_funds(self):
        """
        Test case for withdrawing an amount greater than the balance.
        """
        with self.assertRaises(ValueError):
            self.account.withdraw(200)  # Should raise an error

    def test_withdraw_negative_amount(self):
        """
        Test case for withdrawing a negative amount.
        """
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

if __name__ == '__main__':
    unittest.main()
