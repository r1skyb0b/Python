# ===== HOMEWORK 1: Modify String with Underscores =====
def add_underscores(txt):
    vowels = 'aeiouAEIOU'
    result = []
    count = 0

    for i, char in enumerate(txt):
        result.append(char)
        count += 1
        
        # Check if we should add underscore
        if count == 3 and i < len(txt) - 1:
            # If current char is vowel or next position would have underscore, skip
            if char not in vowels and (i + 1 < len(txt)):
                result.append('_')
                count = 0
            else:
                # Continue counting until we find non-vowel
                count = 0 if char in vowels else count
        
        # Reset counter after underscore or vowel
        if char in vowels:
            count = 0
    
    return ''.join(result)

# Test cases
print("=== Homework 1 ===")
print(f"Input: 'hello' -> Output: '{add_underscores('hello')}'")
print(f"Input: 'assalom' -> Output: '{add_underscores('assalom')}'")
print(f"Input: 'abcabcdabcdeabcdefabcdefg' -> Output: '{add_underscores('abcabcdabcdeabcdefabcdefg')}'")
print()


# ===== HOMEWORK 2: Integer Squares =====
def print_squares(n):
    for i in range(n):
        print(i ** 2)

print("=== Homework 2 ===")
n = 5
print(f"Input: {n}")
print("Output:")
print_squares(n)
print()


# ===== HOMEWORK 3: Loop-Based Exercises =====

# Exercise 1: First 10 natural numbers
print("=== Exercise 1: First 10 natural numbers ===")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

# Exercise 2: Number pattern
print("=== Exercise 2: Number pattern ===")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
print()

# Exercise 3: Sum of numbers
print("=== Exercise 3: Sum of numbers from 1 to n ===")
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

num = 10
print(f"Enter number {num}")
print(f"Sum is: {sum_numbers(num)}")
print()

# Exercise 4: Multiplication table
print("=== Exercise 4: Multiplication table ===")
def multiplication_table(n):
    for i in range(1, 11):
        print(n * i)

multiplication_table(2)
print()

# Exercise 5: Display specific numbers from list
print("=== Exercise 5: Display numbers divisible by 5 from list ===")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0 and num > 50 and num < 500:
        print(num)
print()

# Exercise 6: Count digits
print("=== Exercise 6: Count digits ===")
def count_digits(n):
    return len(str(abs(n)))

print(f"75869 -> Output: {count_digits(75869)}")
print()

# Exercise 7: Reverse number pattern
print("=== Exercise 7: Reverse number pattern ===")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
print()

# Exercise 8: Print list in reverse
print("=== Exercise 8: Print list in reverse ===")
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
print()

# Exercise 9: Numbers from -10 to -1
print("=== Exercise 9: Numbers from -10 to -1 ===")
for i in range(-10, 0):
    print(i)
print()

# Exercise 10: Display "Done" after loop
print("=== Exercise 10: Display 'Done' ===")
for i in range(5):
    print(i)
print("Done!")
print()

# Exercise 11: Prime numbers in range
print("=== Exercise 11: Prime numbers between 25 and 50 ===")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 25 and 50:")
for num in range(25, 51):
    if is_prime(num):
        print(num)
print()

# Exercise 12: Fibonacci series
print("=== Exercise 12: Fibonacci series (10 terms) ===")
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

print("Fibonacci sequence:")
print(' '.join(map(str, fibonacci(10))))
print()

# Exercise 13: Factorial
print("=== Exercise 13: Factorial ===")
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
print(f"{n}! = {factorial(n)}")
print()


# ===== HOMEWORK 4: Return Uncommon Elements =====
print("=== Homework 4: Uncommon Elements ===")
def uncommon_elements(list1, list2):
    from collections import Counter
    
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    result = []
    
    # Add elements from list1 that are not in list2
    for elem in list1:
        if elem not in count2:
            result.append(elem)
    
    # Add elements from list2 that are not in list1
    for elem in list2:
        if elem not in count1:
            result.append(elem)
    
    return result

# Test cases
print(f"list1 = [1, 1, 2], list2 = [2, 3, 4]")
print(f"Output: {uncommon_elements([1, 1, 2], [2, 3, 4])}")
print()

print(f"list1 = [1, 2, 3], list2 = [4, 5, 6]")
print(f"Output: {uncommon_elements([1, 2, 3], [4, 5, 6])}")
print()

print(f"list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]")
print(f"Output: {uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])}")
