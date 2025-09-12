import os
import datetime
import json
import random


class ValidationUtils:
    """Validation helper functions."""
    
    @staticmethod
    def is_positive_number(value):
        """Checks if the given value is a positive number (int or float).
        Returns True if it's a number and greater than zero."""
        try:
            return isinstance(value, (int, float)) and value > 0
        except Exception as e:
            print(e)
        
    
    @staticmethod
    def validate_amount(amount):
        """Validates if the amount is a positive number using is_positive_number()."""
        try:
             return ValidationUtils.is_positive_number(amount)
        except Exception as e:
            print(e)

       
    
    @staticmethod
    def validate_pin(pin):
        """ Validates if the PIN:
        - Contains only digits
        - Has a length between 4 and 6 characters
          Accepts string or number input."""
        try:
            pin_str = str(pin)
            return pin_str.isdigit() and 4 <= len(pin_str) <= 6
        except Exception as e:
            print(e)

        

    @staticmethod
    def validate_account_number(account_number):
        """ Validates if the account number:
        - Contains only digits
        - Has a length between 8 and 12 characters
          Accepts string or number input."""
        try:
            acc_str = str(account_number)
            return acc_str.isdigit() and 8 <= len(acc_str) <= 12
        except Exception as e:
            print(e)
       

    @staticmethod
    def validate_name(name):
        """Validates if the name:
        - Is not empty
        - Contains only alphabetic characters or spaces"""
        try:
            return bool(name) and all(c.isalpha() or c.isspace() for c in name)
        except Exception as e:
            print(e)

        
v = ValidationUtils()
print(v.validate_pin("1234"))  
print(v.validate_name("John Doe"))  
