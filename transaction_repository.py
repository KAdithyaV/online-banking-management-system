import json
import os
from datetime import datetime
from database_manager import db_manager
from account_repository import account_repo

class TransactionRepository:
    def __init__(self,db_manager):
        self.db_manager = db_manager

    def add_transaction(self, account_number, transaction):
        data = self.db_manager.load_data()
        if "transactions" not in data:
            data["transactions"] = {}   #  ensure key exists
        if account_number not in data["transactions"]:
            data["transactions"][account_number] = []
        """Preventing duplicate transactions"""
        for txn in data["transactions"][account_number]:
            if txn["transaction_id"] == transaction["transaction_id"]:
                print("Transaction already exists, skipping...")
                return
        print("Transaction added ")
        data["transactions"][account_number].append(transaction)
        self.db_manager.save_data(data)

    
    def get_transactions(self, account_number, limit =10):
        data = self.db_manager.load_data()
        return data["transactions"].get(account_number,[])
    
    def get_transaction_by_id(self, transaction_id):
        data = self.db_manager.load_data()
        for acc_tran in data["transactions"].values():
            for tran in acc_tran:
                if tran["transaction_id"] == transaction_id:
                    return tran
        
    def update_balance_after_transaction(self,account_number, new_balance):
        data = self.db_manager.load_data()
        if account_number in data["accounts"]:
            data["accounts"][account_number]["balance"] = new_balance
            self.db_manager.save_data(data)

transaction_repo = TransactionRepository(db_manager)
# Step 4: Work with Transactions
transaction = {
    "transaction_id": "TXN001",
    "date": "2025-09-08 12:00:00",
    "type": "DEPOSIT",
    "amount": 400.0,
    "balance_after": 1500.0,
    "description": "Cash Deposit"
}

""" Add Transaction """
transaction_repo.add_transaction("ACC001", transaction)


"""Get transactions"""
# print(f"Recent transactions: {transaction_repo.get_transactions("ACC001")}")

"""Get specific transaction"""
# print(f"Fetch by ID : {transaction_repo.get_transaction_by_id("TXN001")}")

"""Update balance after transaction"""
# transaction_repo.update_balance_after_transaction("ACC001",2000)
# print(f"Balance updated: {account_repo.get_account("ACC001")["balance"]}")