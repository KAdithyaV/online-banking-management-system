"""
Transaction
-----------
Represents an immutable transaction record.
"""

from datetime import datetime


class Transaction:
    """Represents a single immutable transaction record."""
    def __init__(self, transaction_id, transaction_type, amount, balance_after, description=""):
        """Initialize a transaction with ID, type, amount, balance after transaction, and optional description."""
        self.transaction_id = transaction_id
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.description = description

    def to_dict(self):
        """Convert the Transaction object into a dictionary for JSON storage."""
        return {
            "transaction_id": self.transaction_id,
            "date": self.date,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "balance_after": self.balance_after,
            "description": self.description,
        }

    @staticmethod
    def from_dict(d: dict):
        """Recreate a Transaction object from a dictionary."""
        return Transaction(d["transaction_id"], d["transaction_type"],
                           d["amount"], d["balance_after"], d.get("description", ""))

    def __str__(self):
        """Return a string representation of the transaction (formatted)."""
        return f"{self.date} | {self.transaction_type} | {self.amount} | bal={self.balance_after} | {self.description}"
