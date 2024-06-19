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
