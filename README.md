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







# Simple Reversal Encryption/Decryption

## Overview
This Python script provides a simple text encryption and decryption system that reverses words or entire sentences. The user can select whether to reverse each word individually or reverse the entire sentence. The key provided by the encrypter must be used by the decrypter to correctly restore the original message.

## Features
- **Encryption**: Reverse the words only or reverse the entire sentence.
- **Decryption**: Based on the encryption mode (key), restore the original message.
- Supports a simple command-line interface for ease of use.
- Can handle sentences with multiple words, including spaces and punctuation.

## How It Works

There are two modes of encryption:
1. **Mode 1 (Reverse words only)**: Each word in the sentence is reversed individually, but the order of words remains the same.
2. **Mode 2 (Reverse entire sentence)**: The entire sentence is reversed, including spaces and punctuation.

During decryption, the appropriate mode (key) needs to be provided in order to correctly decrypt the text.

### Example Workflow

1. **Encrypting with mode 1**:
   ```bash
   Do you want to encrypt, decrypt, or stop? (e/d/s): e
   Choose mode: (1) Reverse words only, (2) Reverse entire sentence: 1
   Enter the text to encrypt: Hello World
   Encrypted text: olleH dlroW
   Provide the key '1' to the reader for decryption.

1. Run the script:
   ```bash
   python reverse.py

   

### To install dependencies, users can run:
pip install -r requirements.txt
