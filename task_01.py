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

# main() function

while True:
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")
