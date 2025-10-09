# ========================================
# LEARNING SECTION: map() and filter()
# ========================================

print("=" * 50)
print("MAP AND FILTER EXAMPLES")
print("=" * 50)

# Example 1: map() with lambda
print("\n1. MAP example - converting Celsius to Fahrenheit:")
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Example 2: filter() with lambda
print("\n2. FILTER example - getting numbers greater than 10:")
numbers = [5, 12, 8, 15, 3, 20]
filtered = list(filter(lambda x: x > 10, numbers))
print(f"Original: {numbers}")
print(f"Filtered (>10): {filtered}")

# Example 3: Combining map() and filter()
print("\n3. COMBINED example - square only even numbers:")
nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(f"Original: {nums}")
print(f"Squared evens: {result}")

print("\n" + "=" * 50)
print("HOMEWORK PROBLEMS")
print("=" * 50)

# ========================================
# PROBLEM 1: is_prime(n) function
# ========================================

def is_prime(n):
    """
    Berilgan n sonining tub yoki tub emasligini aniqlaydi.
    
    Args:
        n (int): Tekshiriladigan son (n > 0)
    
    Returns:
        bool: Agar n tub son bo'lsa True, aks holda False
    """
    # 1 va undan kichik sonlar tub emas
    if n <= 1:
        return False
    
    # 2 yagona juft tub son
    if n == 2:
        return True
    
    # Juft sonlar (2 dan boshqa) tub emas
    if n % 2 == 0:
        return False
    
    # 3 dan boshlab n ning kvadrat ildizigacha toq sonlarga bo'linishni tekshirish
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


print("\n--- Problem 1: is_prime(n) ---")
print(f"is_prime(4) = {is_prime(4)}")  # False
print(f"is_prime(7) = {is_prime(7)}")  # True
print(f"is_prime(1) = {is_prime(1)}")  # False
print(f"is_prime(13) = {is_prime(13)}")  # True
print(f"is_prime(100) = {is_prime(100)}")  # False

# Using filter with is_prime
numbers_to_check = list(range(1, 21))
prime_numbers = list(filter(is_prime, numbers_to_check))
print(f"\nTub sonlar (1-20 oralig'ida): {prime_numbers}")


# ========================================
# PROBLEM 2: digit_sum(k) function
# ========================================

def digit_sum(k):
    """
    Berilgan k sonining raqamlari yig'indisini hisoblaydi.
    
    Args:
        k (int): Raqamlari yig'indisi hisoblaniladigan son
    
    Returns:
        int: Raqamlar yig'indisi
    """
    # Sonni musbat qilish (manfiy sonlar uchun ham ishlaydi)
    k = abs(k)
    
    # Yechim 1: String konversiya orqali
    return sum(int(digit) for digit in str(k))
    
    # Yechim 2: Matematik usul (alternative)
    # total = 0
    # while k > 0:
    #     total += k % 10
    #     k //= 10
    # return total


print("\n--- Problem 2: digit_sum(k) ---")
print(f"digit_sum(24) = {digit_sum(24)}")  # 6
print(f"digit_sum(502) = {digit_sum(502)}")  # 7
print(f"digit_sum(9999) = {digit_sum(9999)}")  # 36
print(f"digit_sum(123) = {digit_sum(123)}")  # 6

# Using map with digit_sum
numbers = [24, 502, 123, 9999]
digit_sums = list(map(digit_sum, numbers))
print(f"\nSonlar: {numbers}")
print(f"Raqamlar yig'indisi: {digit_sums}")


# ========================================
# PROBLEM 3: Powers of 2 up to N
# ========================================

def powers_of_two(N):
    """
    N dan kichik yoki teng bo'lgan barcha 2 ning darajalarini chop etadi.
    
    Args:
        N (int): Maksimal chegara
    """
    k = 1
    powers = []
    
    while 2**k <= N:
        powers.append(2**k)
        k += 1
    
    print(" ".join(map(str, powers)))
    return powers


print("\n--- Problem 3: Powers of 2 up to N ---")
print("N = 10:")
powers_of_two(10)  # 2 4 8

print("\nN = 50:")
powers_of_two(50)  # 2 4 8 16 32

print("\nN = 100:")
powers_of_two(100)  # 2 4 8 16 32 64

# Alternative using filter and lambda
def powers_of_two_alternative(N):
    """
    filter() dan foydalangan holda alternativ yechim
    """
    # Barcha mumkin bo'lgan darajalarni yaratish
    max_power = N.bit_length()  # N ning bit uzunligi
    all_powers = [2**k for k in range(1, max_power + 1)]
    
    # N dan kichik yoki tenglarini filtrlash
    result = list(filter(lambda x: x <= N, all_powers))
    print(" ".join(map(str, result)))
    return result


print("\n--- Alternative yechim (filter bilan) ---")
print("N = 10:")
powers_of_two_alternative(10)


# ========================================
# INTERACTIVE TEST SECTION
# ========================================

print("\n" + "=" * 50)
print("INTERAKTIV TEST")
print("=" * 50)

# Foydalanuvchidan kiritish olish
print("\nO'z qiymatlaringizni sinab ko'ring:")
print("\nMisol uchun quyidagi kodlarni ishlatishingiz mumkin:")
print("# is_prime(29)")
print("# digit_sum(4567)")
print("# powers_of_two(128)")
