"""
BankingSystem
-------------
Main controller with try/except in every method.
"""

from core.bank_account import BankAccount
from core.transaction import Transaction
from utils.format_utils import FormatUtils
from utils.validation_utils import ValidationUtils

class BankingSystem:
    def __init__(self, db, account_repo, txn_repo, config, security, validity, format_u):
        self.db = db
        self.accounts = account_repo
        self.txns = txn_repo
        self.cfg = config
        self.sec = security
        self.current_user = None
        self.val = validity
        self.frmt = format_u

    def authenticate_user(self):
        """Login process with try/except."""
        try:
            acc_no = input("Account number: ")
            pin = input("PIN: ")
            rec = self.accounts.get_account(acc_no)
            if not rec:
                print("Invalid account.")
                return
            acct = BankAccount.from_dict(rec)
            if not self.val.validate_pin(pin):
                print("Incorrect PIN.")
                return
            self.current_user = acct
            print(f"Welcome {acct.name}!")
        except Exception as e:
            print("Error in authentication:", e)

    def create_account(self):
        try:
            name = input("Name: ")
            pin = input("PIN: ")
            initial = float(input("Initial deposit: "))
            if initial < self.cfg.get_minimum_balance():
                print("Below minimum balance.")
                return
            acc_no = self.sec.generate_account_number()
            acct = BankAccount(acc_no, self.sec.encrypt_pin(pin), name, initial)
            self.accounts.create_account(acct.to_dict())
            txn = Transaction(self.sec.generate_transaction_id(), "OPEN", initial, initial, "Account opened")
            self.txns.add_transaction(acc_no, txn)
            print("Created account", acc_no)
        except Exception as e:
            print("Error in create_account:", e)

    def main_menu(self):
        while self.current_user:
            print("\n1) Balance 2) Deposit 3) Withdraw 4) Transfer 5) History 6) Details 7) Logout")
            c = input("Choose: ")
            try:
                if c == "1": self.current_user.check_balance()
                elif c == "2": self.deposit()
                elif c == "3": self.withdraw()
                elif c == "4": self.transfer_money()
                elif c == "5": self.frmt.print_transaction_history(self.txns.get_transactions(self.current_user.account_number))
                elif c == "6": self.frmt.print_account_summary(self.current_user.get_account_info())
                elif c == "7": self.logout()
            except Exception as e:
                print("Error in menu:", e)

    def deposit(self):
        try:
            amt = float(input("Deposit: "))
            self.current_user.deposit(amt)
            print(self.current_user.account_number)
            print(self.current_user.to_dict())
            self.accounts.update_account(self.current_user.account_number, self.current_user.to_dict())
            print(f"Transaction obj: {Transaction(self.sec.generate_transaction_id(), "DEPOSIT", amt, self.current_user.balance)}")
            self.txns.add_transaction(self.current_user.account_number,
                                      Transaction(self.sec.generate_transaction_id(), "DEPOSIT", amt, self.current_user.balance))
        except Exception as e:
            print("Error in deposit:", e)

    def withdraw(self):
        try:
            amt = float(input("Withdraw: "))
            self.current_user.withdraw(amt, self.cfg.get_minimum_balance(), self.cfg.get_withdrawal_limit())
            self.accounts.update_account(self.current_user.account_number, self.current_user.to_dict())
            self.txns.add_transaction(self.current_user.account_number,
                                      Transaction(self.sec.generate_transaction_id(), "WITHDRAW", amt, self.current_user.balance))
        except Exception as e:
            print("Error in withdraw:", e)

    def transfer_money(self):
        try:
            to_acc = input("Recipient account: ")
            amt = float(input("Amount: "))
            rec = self.accounts.get_account(to_acc)
            if not rec:
                print("Recipient not found.")
                return
            self.withdraw()
            r = BankAccount.from_dict(rec)
            r.deposit(amt)
            self.accounts.update_account(to_acc, r.to_dict())
            self.txns.add_transaction(to_acc, Transaction(self.sec.generate_transaction_id(), "TRANSFER_IN", amt, r.balance))
            print(f"Transferred {amt} to {to_acc}")
        except Exception as e:
            print("Error in transfer:", e)

    def logout(self):
        try:
            print("Logout...")
            self.current_user = None
        except Exception as e:
            print("Error in logout:", e)

    def run(self):
        while True:
            print("\n1) Login 2) Create Account 0) Exit")
            c = input("Choose: ")
            try:
                if c == "1":
                    self.authenticate_user()
                    self.main_menu()
                elif c == "2":
                    self.create_account()
                elif c == "0":
                    break
            except Exception as e:
                print("Error in run loop:", e)
