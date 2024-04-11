# Joshua Rivera

def encode(password):
    new_password = ""
    for char in password:
        new_password += str(int(char)+3)
    return new_password

def decode(password):
    new_password = ""
    for i in range(0, len(password)):
        new_password += str((int(password[i]) - 3))
    return new_password

def main():
    while True:
        print("""
        Menu
        -------------
        1. Encode
        2. Decode
        3. Quit
        """)

        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_p = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            print(f"The encoded password is {encoded_p}, and the original password is {decode(encoded_p)}.")
        elif choice == 3:
            break

if __name__ == '__main__':
    main()
