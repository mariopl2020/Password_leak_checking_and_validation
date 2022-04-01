""""""

from passwords_set import PasswordsSet
from abc import ABC, abstractmethod


class Validation(ABC):
    """Interface of validator"""

    @abstractmethod
    def __init__(self, text):
        """Initialization of validator"""

        self.text = text

    @abstractmethod
    def is_valid(self):
        """Abstract method as template to implement password validation"""
        pass


class HasDigitValidation(Validation):
    """Represents validator what checks if password has any number"""

    def __init__(self, password: str):
        """Initialization of validator"""

        self.password = password

    def is_valid(self):
        """Checks if password has any number

        Returns:
            is_valid (bool): indicates if password is valid or not"""

        output = [(str(char) in self.password) for char in range(0,10)]
        is_valid = any(output)
        return is_valid


class HasSpecialCharValidation(Validation):
    """Represents validator what checks if password has any special character"""

    def __init__(self, password):
        """Initialization of validator"""

        self.password = password

    def is_valid(self):
        """Checks if password has any special character

        Returns:
            is_valid (bool): indicates if password is valid or not"""

        output = [not char.isalnum() for char in self.password]
        is_valid = any(output)
        return is_valid


class HasLowerCaseValidation(Validation):
    """Represents validator what checks if password has any low case"""

    def __init__(self, password):
        """Initialization of validator"""

        self.password = password

    def is_valid(self):
        """Checks if password has any low case

        Returns:
            is_valid (bool): indicates if password is valid or not"""

        output = [letter.islower() for letter in self.password]
        is_valid = any(output)
        return is_valid


class HasUpperCaseValidation(Validation):
    """Represents validator what checks if password has any upper case"""

    def __init__(self, password):
        """Initialization of validator"""

        self.password = password

    def is_valid(self):
        """Checks if password has any upper case

        Returns:
            is_valid (bool): indicates if password is valid or not"""

        output = [letter.isupper() for letter in self.password]
        is_valid = any(output)
        return is_valid


class IsLongEnoughValidation(Validation):
    """Represents validator what checks if password is as long as required"""

    def __init__(self, password, password_length: int = 8):
        """Initialization of validator"""

        self.password = password
        self.password_length = password_length

    def is_valid(self):
        """Checks if password is as long as required

        Returns:
            is_valid (bool): indicates if password is valid or not"""

        is_valid = len(self.password) >= self.password_length
        return is_valid


class PasswordValidation():
    """Represents main password validator what checks if it is validated by all implemented simple validation
    conditions"""

    def __init__(self, user_passwords_set: PasswordsSet):
        """Initialization of new validator"""

        self.user_passwords_set = user_passwords_set
        self.validators = [
            HasDigitValidation,
            HasSpecialCharValidation,
            HasUpperCaseValidation,
            HasLowerCaseValidation,
            IsLongEnoughValidation
        ]

    def is_valid(self):
        """Checks if all provided passwords fill all validation conditions"""

        for password in self.user_passwords_set.passwords_list:
            for class_name in self.validators:
                validator = class_name(password.password_content)
                if not validator.is_valid():
                    password.is_valid = False
                    break
