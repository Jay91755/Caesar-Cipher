# caesar_cipher.py

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if it's a letter
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    print("==== Caesar Cipher Tool ====")
    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (e.g. 3): "))
    except ValueError:
        print("Shift must be an integer!")
        exit()

    print("\nChoose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        encrypted = caesar_encrypt(message, shift)
        print(f"\n🔐 Encrypted message: {encrypted}")
    elif choice == '2':
        decrypted = caesar_decrypt(message, shift)
        print(f"\n🔓 Decrypted message: {decrypted}")
    else:
        print("Invalid option! Please select 1 or 2.")
