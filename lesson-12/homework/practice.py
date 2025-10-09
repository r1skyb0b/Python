# ===============================
# Homework: Multithreading in Python
# ===============================
import threading
from collections import Counter
import math

# ========================================
# Exercise 1: Threaded Prime Number Checker
# ========================================

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, result_list):
    """Check primes in a range and add them to the shared result list."""
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    result_list.extend(local_primes)

def threaded_prime_checker(start, end, num_threads=4):
    """Divide the range and check primes using multiple threads."""
    threads = []
    result = []
    step = (end - start + 1) // num_threads

    for i in range(num_threads):
        s = start + i * step
        e = start + (i + 1) * step - 1 if i < num_threads - 1 else end
        t = threading.Thread(target=check_primes_in_range, args=(s, e, result))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    result.sort()
    print(f"Prime numbers between {start} and {end}:")
    print(result)


# ======================================
# Exercise 2: Threaded File Processing
# ======================================

def process_lines(lines, counter_dict):
    """Count words in a subset of lines."""
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    # Update the shared dictionary safely
    with threading.Lock():
        for word, count in local_counter.items():
            counter_dict[word] = counter_dict.get(word, 0) + count

def threaded_word_count(filename, num_threads=4):
    """Threaded word counting from a text file."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    step = total_lines // num_threads
    threads = []
    global_counter = {}

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else total_lines
        t = threading.Thread(target=process_lines, args=(lines[start:end], global_counter))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nWord count summary:")
    for word, count in sorted(global_counter.items(), key=lambda x: -x[1]):
        print(f"{word}: {count}")


# ===============================
# Example Usage
# ===============================
if __name__ == "__main__":
    # Exercise 1 Demo
    threaded_prime_checker(1, 100, num_threads=4)

    # Exercise 2 Demo (Make sure to have 'sample.txt' in the same folder)
    # Example: create a simple file with some repeated words
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("hello world\n")
        f.write("hello python world\n")
        f.write("multithreading in python is fun\n")
        f.write("python python hello\n")

    threaded_word_count("sample.txt", num_threads=4)
