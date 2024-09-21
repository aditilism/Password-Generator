import random
import string


def generate_password(length):
    # Define character sets for different types of characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + symbols

    # Generate a password by randomly selecting characters from the combined set
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password


def main():
    # Get user input for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()
