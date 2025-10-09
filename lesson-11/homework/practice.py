##############################################
# 🧠 HOMEWORK: Custom Modules & Packages
##############################################

# ---------- Virtual Environment Instructions ----------
# Run these commands in your terminal (not in Python):
#
# python -m venv myenv
# myenv\Scripts\activate       (on Windows)
# source myenv/bin/activate    (on macOS/Linux)
#
# pip install requests numpy pandas
#
# -------------------------------------------------------


#########################################################
# 1️⃣  math_operations.py  (custom module)
#########################################################

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


#########################################################
# 2️⃣  string_utils.py  (custom module)
#########################################################

def reverse_string(s):
    """Return the reversed version of a string."""
    return s[::-1]

def count_vowels(s):
    """Return the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


#########################################################
# 3️⃣  geometry package
# geometry/
#     __init__.py
#     circle.py
#########################################################

# ----- geometry/__init__.py -----
# from .circle import calculate_area, calculate_circumference

# ----- geometry/circle.py -----
import math

def calculate_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Return the circumference of a circle."""
    return 2 * math.pi * radius


#########################################################
# 4️⃣  file_operations package
# file_operations/
#     __init__.py
#     file_reader.py
#     file_writer.py
#########################################################

# ----- file_operations/__init__.py -----
# from .file_reader import read_file
# from .file_writer import write_file

# ----- file_operations/file_reader.py -----
def read_file(file_path):
    """Read and return content from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

# ----- file_operations/file_writer.py -----
def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    return "File written successfully."


#########################################################
# 5️⃣  main.py (example usage / test)
#########################################################

if __name__ == "__main__":
    # Math operations
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))

    # String utils
    print("Reversed:", reverse_string("Python"))
    print("Vowel count:", count_vowels("Python Programming"))

    # Geometry
    print("Circle area (r=7):", calculate_area(7))
    print("Circle circumference (r=7):", calculate_circumference(7))

    # File operations
    write_file("example.txt", "Hello, this is a test file.")
    print(read_file("example.txt"))
