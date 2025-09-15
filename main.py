"""
Main entry point
----------------
Wires everything together and runs BankingSystem.
"""

from core.banking_system import BankingSystem
from database.database_manager import DatabaseManager
from database.account_repository import AccountRepository
from database.transaction_repository import TransactionRepository
from utils.security_utils import SecurityUtils
from utils.config_manager import ConfigManager
from utils.validation_utils import ValidationUtils
from utils.format_utils import FormatUtils


if __name__ == "__main__":
    try:
        db = DatabaseManager("accounts.json")
        accounts = AccountRepository(db)
        txns = TransactionRepository(db)
        sec = SecurityUtils()
        cfg = ConfigManager()
        val = ValidationUtils()
        frmt = FormatUtils()

        system = BankingSystem(db, accounts, txns, cfg, sec, val, frmt)
        system.run()
    except Exception as e:
        print("Fatal error in system:", e)
