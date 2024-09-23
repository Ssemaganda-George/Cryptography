def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split())

def reverse_sentence(text):
    return text[::-1]

def create_key(mode):
    return mode

def parse_key(key):
    if key in ['1', '2']:
        return key
    return None

def main():
    while True:
        choice = input("Do you want to encrypt, decrypt, or stop? (e/d/s): ").lower()
        
        if choice == 's':
            print("Stopping the program.")
            break
        
        if choice == 'e':
            while True:
                mode = input("Choose mode: (1) Reverse words only, (2) Reverse entire sentence: ")
                if mode in ['1', '2']:
                    break
                print("Invalid mode. Please choose '1' or '2'.")
            
            key = create_key(mode)
            text = input("Enter the text to encrypt: ")
            if mode == '1':
                encrypted_text = reverse_words(text)
            elif mode == '2':
                encrypted_text = reverse_sentence(text)
            print(f"Encrypted text: {encrypted_text}")
            print(f"Provide the key '{key}' to the reader for decryption.")
        
        elif choice == 'd':
            while True:
                key = input("Enter the decryption key ('1' for reversing words only, '2' for reversing the entire sentence): ").strip()
                mode = parse_key(key)
                if mode is not None:
                    text = input("Enter the text to decrypt: ")
                    if mode == '1':
                        decrypted_text = reverse_words(text)
                    elif mode == '2':
                        decrypted_text = reverse_sentence(text)
                    print(f"Decrypted text: {decrypted_text}")
                    break
                else:
                    print("Invalid key format. Please provide '1' or '2'.")
        
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 's' to stop.")

if __name__ == "__main__":
    main()