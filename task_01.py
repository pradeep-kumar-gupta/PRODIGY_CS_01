# Encrypt & Decrept text using the Caesar Cipher algorithm.

# to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_val = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_val) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_val) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text


# to decrypt the text using encrypt() function
def decrypt(text, shift):
    return encrypt(text,-shift)


# main() function
while True:
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 2:
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
