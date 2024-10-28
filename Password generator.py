import string
import secrets

def containsUpper(password: str) -> bool:
    for char in password:
        if char.isupper():  # Checks for uppercase
            return True
    return False

def containsSymbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:  # Checks for symbols
            return True
    return False

def password_generator(length: int, symbols: bool, uppercase: bool) -> str:
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Start with lowercase letters and digits
    combination = string.ascii_lowercase + string.digits
    password_chars = []

    # Ensure at least one symbol if required
    if symbols:
        password_chars.append(secrets.choice(string.punctuation))  # Add one symbol
        combination += string.punctuation  # Add symbols to the character pool

    # Ensure at least one uppercase letter if required
    if uppercase:
        password_chars.append(secrets.choice(string.ascii_uppercase))  # Add one uppercase letter
        combination += string.ascii_uppercase  # Add uppercase letters to the character pool

    # Fill the remaining length with random characters from the full combination
    while len(password_chars) < length:
        password_chars.append(secrets.choice(combination))

    # Shuffle to mix guaranteed characters
    secrets.SystemRandom().shuffle(password_chars)

    # Join list into a string and return
    return ''.join(password_chars[:length])  # Truncate in case extra chars were added

if __name__ == '__main__':
    # Get user input for password generation
    try:
        length = int(input("Enter the desired length of the password: "))
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'

        # Generate the password based on user input
        new_pass = password_generator(length=length, symbols=use_symbols, uppercase=use_uppercase)

        # Display the generated password
        print(f"Generated Password: {new_pass}")
        print(f"Specifications: Uppercase: {use_uppercase}, Symbols: {use_symbols}")

    except ValueError as e:
        print(f"Error: {e}")
