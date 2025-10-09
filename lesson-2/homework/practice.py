import random
import string
from datetime import datetime

# Exercise 1: Age Calculator
def age_calculator():
    print("=== Exercise 1: Age Calculator ===")
    name = input("Enter your name: ")
    birth_year = int(input("Enter your year of birth: "))
    current_year = datetime.now().year
    age = current_year - birth_year
    print(f"Hello {name}! You are {age} years old.\n")

# Exercise 2: Extract Car Names from 'LMaasleitbtui'
def extract_cars_1():
    print("=== Exercise 2: Extract Car Names ===")
    txt = 'LMaasleitbtui'
    # Extract every other character starting from index 0
    car_name = txt[::2]
    print(f"Original text: {txt}")
    print(f"Extracted car name: {car_name}\n")

# Exercise 3: Extract Car Names from 'MsaatmiazD'
def extract_cars_2():
    print("=== Exercise 3: Extract Car Names ===")
    txt = 'MsaatmiazD'
    # Extract every other character starting from index 0
    car_name = txt[::2]
    print(f"Original text: {txt}")
    print(f"Extracted car name: {car_name}\n")

# Exercise 4: Extract Residence Area
def extract_residence():
    print("=== Exercise 4: Extract Residence Area ===")
    txt = "I'am John. I am from London"
    # Split by "from " and get the last part
    residence = txt.split("from ")[-1]
    print(f"Original text: {txt}")
    print(f"Residence area: {residence}\n")

# Exercise 5: Reverse String
def reverse_string():
    print("=== Exercise 5: Reverse String ===")
    user_input = input("Enter a string to reverse: ")
    reversed_str = user_input[::-1]
    print(f"Original: {user_input}")
    print(f"Reversed: {reversed_str}\n")

# Exercise 6: Count Vowels
def count_vowels():
    print("=== Exercise 6: Count Vowels ===")
    user_input = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in user_input if char in vowels)
    print(f"Number of vowels in '{user_input}': {count}\n")

# Exercise 7: Find Maximum Value
def find_maximum():
    print("=== Exercise 7: Find Maximum Value ===")
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = [float(num) for num in numbers_input.split()]
    if numbers:
        max_value = max(numbers)
        print(f"Maximum value: {max_value}\n")
    else:
        print("No numbers entered.\n")

# Exercise 8: Check Palindrome
def check_palindrome():
    print("=== Exercise 8: Check Palindrome ===")
    word = input("Enter a word: ")
    cleaned_word = word.lower().replace(" ", "")
    if cleaned_word == cleaned_word[::-1]:
        print(f"'{word}' is a palindrome!\n")
    else:
        print(f"'{word}' is not a palindrome.\n")

# Exercise 9: Extract Email Domain
def extract_email_domain():
    print("=== Exercise 9: Extract Email Domain ===")
    email = input("Enter an email address: ")
    if '@' in email:
        domain = email.split('@')[-1]
        print(f"Email: {email}")
        print(f"Domain: {domain}\n")
    else:
        print("Invalid email format.\n")

# Exercise 10: Generate Random Password
def generate_password():
    print("=== Exercise 10: Generate Random Password ===")
    length = int(input("Enter password length (minimum 8): "))
    if length < 8:
        length = 8
        print("Password length set to minimum: 8")
    
    # Create character pool
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits  # 0-9
    special = string.punctuation  # Special characters
    
    all_chars = letters + digits + special
    
    # Ensure at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest randomly
    password += random.choices(all_chars, k=length - 3)
    
    # Shuffle to avoid predictable pattern
    random.shuffle(password)
    
    password_str = ''.join(password)
    print(f"Generated password: {password_str}\n")

# Main menu
def main():
    print("=" * 50)
    print("PYTHON HOMEWORK EXERCISES")
    print("=" * 50)
    
    exercises = {
        '1': age_calculator,
        '2': extract_cars_1,
        '3': extract_cars_2,
        '4': extract_residence,
        '5': reverse_string,
        '6': count_vowels,
        '7': find_maximum,
        '8': check_palindrome,
        '9': extract_email_domain,
        '10': generate_password
    }
    
    while True:
        print("\nSelect an exercise to run (1-10) or 'all' to run all, 'q' to quit:")
        choice = input("Your choice: ").strip().lower()
        
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'all':
            for func in exercises.values():
                func()
            break
        elif choice in exercises:
            exercises[choice]()
        else:
            print("Invalid choice. Please select 1-10, 'all', or 'q'.")

if __name__ == "__main__":
    main()
