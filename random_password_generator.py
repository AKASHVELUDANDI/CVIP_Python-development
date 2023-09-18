import string
import random

def generate_strong_password(length):
    # Define character sets for the password
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # Check if the requested length is at least 8 characters
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Calculate the number of characters for each category
    num_letters = round(length * 0.6)
    num_digits_and_punctuations = length - num_letters

    # Shuffle each character set
    random.shuffle(lowercase_letters)
    random.shuffle(uppercase_letters)
    random.shuffle(digits)
    random.shuffle(punctuation)

    # Create the password by selecting characters from each category
    password = []
    password.extend(lowercase_letters[:min(num_letters // 2, len(lowercase_letters))])
    password.extend(uppercase_letters[:min(num_letters // 2, len(uppercase_letters))])
    password.extend(digits[:min(num_digits_and_punctuations // 2, len(digits))])
    password.extend(punctuation[:min(num_digits_and_punctuations // 2, len(punctuation))])

    # Shuffle the final password
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    while True:
        user_input = input("How many characters do you want in your password? ")

        try:
            password_length = int(user_input)
            generated_password = generate_strong_password(password_length)
            
            if generated_password:
                print("Generated Password:", generated_password)
                break

        except ValueError:
            print("Please, enter a valid number.")