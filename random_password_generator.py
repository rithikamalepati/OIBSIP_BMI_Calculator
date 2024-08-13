# -*- coding: utf-8 -*-
"""Random_PassWord_Generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vJ_tt6tK0v8_r3qY0g9znGkDtaXC18YI
"""

import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be selected.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()