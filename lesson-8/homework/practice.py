# ============================================================
# 🧩 PYTHON HOMEWORK: EXCEPTION HANDLING + FILE I/O SOLUTIONS
# ============================================================

# -----------------------------
# Exception Handling Exercises
# -----------------------------

# 1. Handle ZeroDivisionError
def zero_division_example():
    try:
        num = int(input("Enter a number: "))
        result = num / 0
        print(result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# 2. Raise ValueError if not integer
def value_error_example():
    try:
        val = input("Enter an integer: ")
        if not val.isdigit():
            raise ValueError("Invalid input! Not an integer.")
        print(f"You entered: {int(val)}")
    except ValueError as e:
        print(e)

# 3. Handle FileNotFoundError
def file_not_found_example():
    try:
        filename = input("Enter filename to open: ")
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found!")

# 4. Raise TypeError if inputs not numerical
def type_error_example():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
            raise TypeError("Both inputs must be numbers!")
        print(float(a) + float(b))
    except TypeError as e:
        print(e)

# 5. Handle PermissionError
def permission_error_example():
    try:
        with open('/root/testfile.txt', 'r') as f:
            print(f.read())
    except PermissionError:
        print("Error: You don't have permission to access this file.")

# 6. Handle IndexError
def index_error_example():
    try:
        lst = [10, 20, 30]
        index = int(input("Enter index: "))
        print(lst[index])
    except IndexError:
        print("Error: Index out of range!")

# 7. Handle KeyboardInterrupt
def keyboard_interrupt_example():
    try:
        num = input("Enter a number (press Ctrl+C to cancel): ")
        print(f"You entered: {num}")
    except KeyboardInterrupt:
        print("\nInput canceled by user.")

# 8. Handle ArithmeticError
def arithmetic_error_example():
    try:
        x = 10
        y = 0
        print(x / y)
    except ArithmeticError:
        print("Arithmetic Error occurred!")

# 9. Handle UnicodeDecodeError
def unicode_decode_error_example():
    try:
        with open('file_with_encoding_issue.txt', 'r', encoding='ascii') as f:
            print(f.read())
    except UnicodeDecodeError:
        print("Unicode Decode Error: Cannot read file with current encoding.")

# 10. Handle AttributeError
def attribute_error_example():
    try:
        lst = [1, 2, 3]
        lst.upper()  # invalid attribute for list
    except AttributeError:
        print("Error: Attribute does not exist for this object.")


# ---------------------------------
# File Input / Output Exercises
# ---------------------------------

# 1. Read entire text file
def read_entire_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

# 2. Read first n lines
def read_first_n_lines(filename, n):
    with open(filename, 'r') as f:
        for _ in range(n):
            print(f.readline(), end='')

# 3. Append text to a file and display
def append_text(filename, text):
    with open(filename, 'a') as f:
        f.write(text + '\n')
    with open(filename, 'r') as f:
        print(f.read())

# 4. Read last n lines
def read_last_n_lines(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(''.join(lines[-n:]))

# 5. Read file line by line → list
def file_to_list(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

# 6. Read file line by line → variable
def file_to_variable(filename):
    with open(filename, 'r') as f:
        return ''.join(f.readlines())

# 7. Read file → array
def file_to_array(filename):
    return file_to_list(filename)

# 8. Find longest word
def find_longest_word(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
        print(max(words, key=len))

# 9. Count number of lines
def count_lines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

# 10. Count frequency of words
def word_frequency(filename):
    from collections import Counter
    with open(filename, 'r') as f:
        words = f.read().split()
        return Counter(words)

# 11. Get file size
import os
def file_size(filename):
    return os.path.getsize(filename)

# 12. Write list to file
def write_list_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")

# 13. Copy contents to another file
def copy_file(src, dest):
    with open(src, 'r') as s, open(dest, 'w') as d:
        d.write(s.read())

# 14. Combine lines from two files
def combine_files(file1, file2, output):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
        for l1, l2 in zip(f1, f2):
            out.write(l1.strip() + ' ' + l2)

# 15. Read random line
import random
def random_line(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(random.choice(lines))

# 16. Check if file closed
def check_file_closed(filename):
    f = open(filename, 'r')
    print(f.closed)  # False
    f.close()
    print(f.closed)  # True

# 17. Remove newline characters
def remove_newlines(filename):
    with open(filename, 'r') as f:
        lines = f.read().replace('\n', '')
    print(lines)

# 18. Count words (including commas)
def count_words(filename):
    with open(filename, 'r') as f:
        text = f.read().replace(',', ' ')
        return len(text.split())

# 19. Extract characters from multiple files
def extract_characters(file_list):
    chars = []
    for file in file_list:
        with open(file, 'r') as f:
            chars.extend(list(f.read()))
    return chars

# 20. Generate 26 text files A-Z
import string
def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as f:
            f.write(f"This is file {letter}\n")

# 21. Create alphabet file with n letters per line
def alphabet_with_n_per_line(n, filename='alphabet.txt'):
    import textwrap
    alphabet = ''.join([chr(i) for i in range(65, 91)])
    wrapped = textwrap.fill(alphabet, n)
    with open(filename, 'w') as f:
        f.write(wrapped)


# ============================================================
# ✅ END OF HOMEWORK
# ============================================================

