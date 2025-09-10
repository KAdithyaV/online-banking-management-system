import os
import json
from database_manager import db_manager

class Accountrepository:
    def __init__(self,db_manager):
        self.db_manager = db_manager
    
    def create_account(self,account_data):
        data = self.db_manager.load_data()
        acc_no = account_data["account_number"]
        data["accounts"][acc_no] = account_data
        self.db_manager.save_data(data)
    
    def get_account(self, account_number):
        data = self.db_manager.load_data()
        return data["accounts"].get(account_number)

    def update_account(self, account_number, updated_data):
        data = self.db_manager.load_data()
        if account_number in data["accounts"]:
            data["accounts"][account_number].update(updated_data)
            self.db_manager.save_data(data)
    
    def delete_account(self, account_number):
        data = self.db_manager.load_data()
        if account_number in data["accounts"]:
            data["accounts"][account_number]["is_active"] = False
            self.db_manager.save_data(data)
            return True   # success
        return False      # account not found


    def get_all_accounts(self):
        data = self.db_manager.load_data()
        return data["accounts"]
    
    def account_exists(self, account_number):
        data = self.db_manager.load_data()
        return account_number in data["accounts"]

#create backup files
account_repo = Accountrepository(db_manager)
# transaction_repo = TransactionRepository(db_manager)

account_data = {
    "account_number": "ACC002",
    "pin": "1289",
    "name": "Joe",
    "balance": 10000.0,
    "account_type": "Savings",
    "created_date": "2025-09-08",
    "is_active": True
}


# # Create account
# account_repo.create_account(account_data)
# print("Account created ✅")

# # Fetch account
# acc = account_repo.get_account("ACC002")
# print("Fetched account:", acc)

# # Update account
# account_repo.update_account("ACC001", {"is_active": True})
# print("Updated account:", account_repo.get_account("ACC001"))

# Delete (deactivate) account
# account_repo.delete_account("ACC001")


# transaction
class TransactionRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_transaction(self, account_number, transaction):
        data = self.db_manager.load_data()
        if account_number not in data["transactions"]:
            data["transactions"][account_number] = []
        data["transactions"][account_number].append(transaction)
        self.db_manager.save_data(data)

    def get_transactions(self, account_number, limit=10):
        data = self.db_manager.load_data()
        return data["transactions"].get(account_number, [])[-limit:]

    def get_transaction_by_id(self, transaction_id):
        data = self.db_manager.load_data()
        for acc_txns in data["transactions"].values():
            for txn in acc_txns:
                if txn["transaction_id"] == transaction_id:
                    return txn
        return None

    def update_balance_after_transaction(self, account_number, new_balance):
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
    "amount": 500.0,
    "balance_after": 1500.0,
    "description": "Cash Deposit"
}

# Add transaction
transaction_repo.add_transaction("ACC001", transaction)
print("Transaction added ✅")

# Get transactions
print("Recent transactions:", transaction_repo.get_transactions("ACC001"))

# Get specific transaction
print("Fetch by ID:", transaction_repo.get_transaction_by_id("TXN001"))

# Update balance after transaction
transaction_repo.update_balance_after_transaction("ACC001", 2000.0)
print("Balance updated:", account_repo.get_account("ACC001")["balance"])

    

