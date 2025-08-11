# Cripter.py

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
 "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def create_encrypted_alphabet(key: str) ->  list:
    encrypted_alphabet = []
    temp_alphabet = alphabet.copy()
    #Count the number letters in the key
    n_letters = len(key)

    #Puts key letters at the beginning of the encrypted alphabet if they arent already there
    for letter in key:
        if letter not in encrypted_alphabet:
            encrypted_alphabet.append(letter)
        if letter in temp_alphabet:
            temp_alphabet.remove(letter)

    #Adds the rest of the letters from the original alphabet to the encrypted alphabet mantaining the order
    for letter in temp_alphabet:
        encrypted_alphabet.append(letter)
    
    
    #Shifts the letters in the encrypted alphabet by the number of letters in the key
    encrypted_alphabet = encrypted_alphabet[n_letters:] + encrypted_alphabet[:n_letters]

    #Returns the encrypted alphabet
    return encrypted_alphabet


def encrypt(message: str, key:str) -> str:
    encrypted_message = ""
    encrypted_alphabet = create_encrypted_alphabet(key)

    #Encrypts the message by replacing each letter with the corresponding letter in the encrypted alphabet
    for letter in message:
        letter = letter.lower()
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted_message += encrypted_alphabet[index]
        else:
            encrypted_message += letter
    return encrypted_message
    
def decrypt(encrypted_message: str, key:str) -> str:
    decrypted_message = ""
    encrypted_alphabet = create_encrypted_alphabet(key)

    #Decrypts the message by replacing each letter with the corresponding letter in the original alphabet
    for letter in encrypted_message:
        letter = letter.lower()
        if letter in encrypted_alphabet:
            index = encrypted_alphabet.index(letter)
            decrypted_message += alphabet[index]
        else:
            decrypted_message += letter
    return decrypted_message

if __name__ == "__main__":

    print("Welcome to Cripter!")
    print("This program encrypts and decrypts messages!")
    
    
    while True:

        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? or e(x)it -> ").lower()
        while choice not in ['e', 'd','x']:
            choice = input("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt: ").lower()

        if choice == 'e':
            message = input("Enter a message to encrypt: ")
            key = input("Enter a key: ").lower()
            encrypted_message = encrypt(message, key)
            print("Encrypted message:", encrypted_message)

        elif choice == 'd':
            encrypted_message = input("Enter a message to decrypt: ")
            key = input("Enter a key: ").lower()
            decrypted_message = decrypt(encrypted_message, key)
            print("Decrypted message:", decrypted_message)

        elif choice == 'x':
            print("Exiting the program. Goodbye!")
            break