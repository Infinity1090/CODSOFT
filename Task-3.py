# Password Generator in Python.

import random
import string
def generate_password(length, include_digits=True, include_special_chars=True):
    # Define character sets based on complexity
    letters = string.ascii_letters
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''
    characters = letters + digits + special_chars
    if not characters:
        return "Please include at least one character set for the password."
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    include_digits = input("Include digits (yes/no)? ").strip().lower() == 'yes'
    include_special_chars = input("Include special characters (yes/no)? ").strip().lower() == 'yes'
    password = generate_password(length, include_digits, include_special_chars)
    print("Generated Password:", password)
main()
