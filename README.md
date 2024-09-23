# Caesar Cipher Encryption/Decryption

## Overview
This Python script provides a basic implementation of the **Caesar Cipher** encryption and decryption method. The Caesar Cipher shifts each letter in the plaintext by a certain number of positions in the alphabet, making the text unreadable without the shift value. The script allows users to encrypt or decrypt text with both uppercase and lowercase letters, digits, and handles non-alphabetical characters without modification.

## Features
- Encrypts text by shifting letters and digits by a user-specified value.
- Decrypts text by reversing the shift.
- Supports both uppercase and lowercase letters.
- Handles numbers and non-alphabetic characters (e.g., spaces and punctuation) without altering them.
- Simple command-line interface to select between encryption, decryption, and exiting the program.

## How the Caesar Cipher Works
The Caesar Cipher works by shifting each character in the input text by a specified number of positions in the alphabet. For example, if the letter "A" is shifted by 3 positions, it becomes "D". The same logic applies to decryption but in reverse.

For example:
- **Plaintext**: `Hello, World!`
- **Shift Value**: `3`
- **Encrypted Text**: `Khoor, Zruog!`

## Usage

1. Run the script:
   ```bash
   python caesar.py
