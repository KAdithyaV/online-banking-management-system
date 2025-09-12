import os
import datetime

class FormatUtils:
    """Helper functions for formatting and displaying data."""

    def __init__(self):
        """Initialize FormatUtils instance (no data members needed)."""
        pass

    def format_currency(self, amount):
        """Format a number as currency with commas and 2 decimals."""
        try:
            return f"${amount:,.2f}"
        except Exception as e:
            print(e)
        

    def format_date(self, date=None):
        """Format date as 'YYYY-MM-DD HH:MM:SS'. Defaults to now."""
        try:
             if date is None:
                 date = datetime.datetime.now()
                 return date.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print(e)     

       
    def print_transaction_history(self, transactions):
        """Print a list of transactions in a readable format."""
        try:
            print("\nTransaction History:")
            for txn in transactions:
                  print(f"ID: {txn['transaction_id']} | Date: {txn['date']} | "
                        f"Amount: {self.format_currency(txn['amount'])} | Type: {txn['type']}")
        except Exception as e:
            print(e)           
 

    def print_account_summary(self, account):
        """Print basic account info."""
        try:
            print("\nAccount Summary")
            print(f"Account Number: {account.get('account_number')}")
            print(f"Name: {account.get('name')}")
            print(f"Balance: {self.format_currency(account.get('balance', 0))}")
        except Exception as e:
            print(e)         
        

    def clear_screen(self):
        """Clear the console screen."""
        try:
              os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(e)      
     

    def print_header(self, title):
        """Print a centered header with surrounding '=' lines."""
        try:
            print("=" * 40)
            print(title.center(40))
            print("=" * 40)
        except Exception as e:
            print(e)      


f = FormatUtils()
print(f.format_currency(1234.56))  
f.print_header("Welcome to Banking System")
