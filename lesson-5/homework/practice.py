# ============================================
# Problem 1: Leap Year Function (Already Done)
# ============================================
def is_leap(year):
    """
    Determines whether a given year is a leap year.
    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.
    Parameters:
    year (int): The year to be checked.
    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# ============================================
# Problem 2: Weird Number Classification
# ============================================
def weird_checker(n):
    """
    Determines if a number is weird or not based on specific rules.
    """
    if n % 2 == 1:  # odd number
        print("Weird")
    elif 2 <= n <= 5:  # even and between 2-5
        print("Not Weird")
    elif 6 <= n <= 20:  # even and between 6-20
        print("Weird")
    else:  # even and greater than 20
        print("Not Weird")


# ============================================
# Problem 3: Find Even Numbers Between a and b
# ============================================

# Solution 1: With if-else statement
def find_evens_with_if(a, b):
    """
    Find even numbers between a and b (inclusive) using if-else.
    Uses range with conditional step.
    """
    if a % 2 == 0:
        start = a
    else:
        start = a + 1
    
    return list(range(start, b + 1, 2))


# Solution 2: Without if-else statement
def find_evens_without_if(a, b):
    """
    Find even numbers between a and b (inclusive) without if-else.
    Uses list comprehension with filter condition.
    """
    return [num for num in range(a, b + 1) if num % 2 == 0]


# ============================================
# Testing the Solutions
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("Problem 1: Leap Year Tests")
    print("=" * 50)
    test_years = [2000, 2004, 1900, 2024, 2100]
    for year in test_years:
        print(f"{year}: {is_leap(year)}")
    
    print("\n" + "=" * 50)
    print("Problem 2: Weird Number Tests")
    print("=" * 50)
    test_numbers = [3, 4, 10, 25]
    for num in test_numbers:
        print(f"n = {num}: ", end="")
        weird_checker(num)
    
    print("\n" + "=" * 50)
    print("Problem 3: Find Even Numbers")
    print("=" * 50)
    test_ranges = [(2, 10), (3, 15), (1, 20), (5, 5), (6, 6)]
    for a, b in test_ranges:
        print(f"\nRange [{a}, {b}]:")
        print(f"  Solution 1 (with if-else): {find_evens_with_if(a, b)}")
        print(f"  Solution 2 (without if-else): {find_evens_without_if(a, b)}")
