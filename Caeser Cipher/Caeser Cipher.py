def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - offset + shift) % 26 + offset)
            elif mode == 'decrypt':
                result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result

def get_user_input():
    text = input("Enter the text: ")
    
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")
    return text, shift

def main_menu():
    while True:
        print("\nCaesar Cipher Menu")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
      
        choice = input("Choose an option: ")
       
        if choice == '1':
            text, shift = get_user_input()
            result_text = caesar_cipher(text, shift, mode='encrypt')
            print(f"Encrypted Text is {result_text}")
        elif choice == '2':
            text, shift = get_user_input()
            result_text = caesar_cipher(text, shift, mode='decrypt')
            print(f"Decrypted Text is {result_text}")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
