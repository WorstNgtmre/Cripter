# Cripter2.0.py

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Create a Vigenère square for encryption and decryption
vigenere_square = {}
for i in range(len(alphabet)):
    vigenere_square[i] = (alphabet[i:] + alphabet[:i])


def encrypt(message: str, key: str) -> str:
    
    encrypted_message = ""

    # Create a key that is as long as the message
    if len(key) < len(message):
        key = (key * (len(message) // len(key) + 1))[:len(message)]
    else:
        key = key[:len(message)]

    # Encrypt the message using the key
    for i in range(len(message)):
        if message[i].lower() in alphabet:
            column = alphabet.index(message[i].lower())
            row = alphabet.index(key[i].lower())
            encrypted_message += vigenere_square[row][column]
        else:
            encrypted_message += message[i]
        
    return encrypted_message


def decrypt(encrypted_message: str, key: str) -> str:
    decrypted_message = ""

    # Create a key that is as long as the encrypted message
    if len(key) < len(encrypted_message):
        key = (key * (len(encrypted_message) // len(key) + 1))[:len(encrypted_message)]
    else:
        key = key[:len(encrypted_message)]

    # Decrypt the message using the key
    for i in range(len(encrypted_message)):
        if encrypted_message[i].lower() in alphabet:
            row = alphabet.index(key[i].lower())
            column = vigenere_square[row].index(encrypted_message[i].lower())
            decrypted_message += alphabet[column]
        else:
            decrypted_message += encrypted_message[i]
        
    return decrypted_message

# Main loop
if __name__ == "__main__":

    print("Welcome to Cripter 2.0!")
    print("This program encrypts and decrypts messages!")
    
    
    while True:

        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? or e(x)it -> ").lower()
        while choice not in ['e', 'd','x']:
            choice = input("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt: ").lower()

        if choice == 'e':
            message = input("Enter a message to encrypt: ")
            if not message:
                message = input("Message cannot be empty. Please try again. Enter a message to encrypt: ")
            key = input("Enter a key: ").lower()
            encrypted_message = encrypt(message, key)
            print("Encrypted message:", encrypted_message)

        elif choice == 'd':
            encrypted_message = input("Enter a message to decrypt: ")
            if not encrypted_message:
                encrypted_message = input("Encrypted message cannot be empty. Please try again. Enter a message to decrypt: ")
            key = input("Enter a key: ").lower()
            decrypted_message = decrypt(encrypted_message, key)
            print("Decrypted message:", decrypted_message)

        elif choice == 'x':
            print("Exiting the program. Goodbye!")
            break
