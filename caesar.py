def encrypt_text(text, shift):
    encrypted_text = []
    for char in text:
        if char.isupper():
            pos = ord(char) - ord('A')
            new_pos = (pos + shift) % 26
            new_char = chr(new_pos + ord('A'))
            encrypted_text.append(new_char)
        elif char.islower():
            pos = ord(char) - ord('a')
            new_pos = (pos + shift) % 26
            new_char = chr(new_pos + ord('a'))
            encrypted_text.append(new_char)
        elif char.isdigit():
            new_pos = (int(char) + shift) % 10
            encrypted_text.append(str(new_pos))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def main():
    while True:
        choice = input("Select an option: encrypt, decrypt, or stop? (e/d/s): ").lower()
        
        if choice == 's':
            print("Stopping the program.")
            break
        
        if choice == 'e':
            text = input("Enter the text to encrypt: ")
            while True:
                try:
                    shift = int(input("Enter the number to use for encryption (positive or negative): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the shift value.")
            encrypted_text = encrypt_text(text, shift)
            print(f"Encrypted text: {encrypted_text}")
            print(f"Provide the number {shift} to the reader for decryption.")
        
        elif choice == 'd':
            text = input("Enter the text to decrypt: ")
            while True:
                try:
                    shift = int(input("Enter the decryption number provided by the encrypter: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the decryption shift value.")
            decrypted_text = encrypt_text(text, -shift)
            print(f"Decrypted text: {decrypted_text}")
        
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 's' to stop.")

if __name__ == "__main__":
    main()
