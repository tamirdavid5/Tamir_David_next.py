#Name: Tamir David

import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, invalid_char, char_index):
        self.invalid_char = invalid_char
        self.char_index = char_index
        super().__init__(
            f"Username '{username}' contains an illegal character '{invalid_char}' at index {char_index}. Please use only English letters, numbers, and underscores.")


class UsernameTooShort(Exception):
    def __str__(self):
        return "Username is too short. Please choose a username with at least 3 characters."


class UsernameTooLong(Exception):
    def __str__(self):
        return "Username is too long. Please choose a username with at most 16 characters."


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "Password is missing at least one mandatory character."


class MissingUppercaseCharacter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Missing uppercase letter)"


class MissingLowercaseCharacter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Missing lowercase letter)"


class MissingNumberCharacter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Missing number)"


class MissingSpecialCharacter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Missing special character)"


def check_input(username, password):
    # Check username requirements
    if len(username) < 3:
        raise UsernameTooShort()

    if len(username) > 16:
        raise UsernameTooLong()

    for index, char in enumerate(username):
        if not (char.isalnum() or char == '_'):
            raise UsernameContainsIllegalCharacter(username, char, index)

    # Check password requirements
    if len(password) < 8:
        raise MissingUppercaseCharacter()

    if len(password) > 40:
        raise MissingLowercaseCharacter()

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if not has_upper:
        raise MissingUppercaseCharacter()

    if not has_lower:
        raise MissingLowercaseCharacter()

    if not has_number:
        raise MissingNumberCharacter()

    if not has_special:
        raise MissingSpecialCharacter()

    # If all requirements are met
    print("OK")


def main():
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        try:
            check_input(username, password)
            break
        except UsernameTooShort as e:
            print(e)
        except UsernameTooLong as e:
            print(e)
        except UsernameContainsIllegalCharacter as e:
            print(e)
        except PasswordMissingCharacter as e:
            print(e)


if __name__ == '__main__':
    main()
