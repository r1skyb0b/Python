# Problem 1: Square perimeter and area
def square_calculations(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area

# Problem 2: Circle circumference from diameter
def circle_length(diameter):
    import math
    circumference = math.pi * diameter
    return circumference

# Problem 3: Mean of two numbers
def mean_of_two(a, b):
    mean = (a + b) / 2
    return mean

# Problem 4: Sum, product, and squares
def number_operations(a, b):
    sum_ab = a + b
    product = a * b
    square_a = a ** 2
    square_b = b ** 2
    return sum_ab, product, square_a, square_b

# Testing the functions
print("Problem 1: Square with side = 5")
side = 5
perimeter, area = square_calculations(side)
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")
print()

print("Problem 2: Circle with diameter = 10")
diameter = 10
length = circle_length(diameter)
print(f"Circumference: {length:.2f}")
print()

print("Problem 3: Mean of a = 8 and b = 12")
a, b = 8, 12
mean = mean_of_two(a, b)
print(f"Mean: {mean}")
print()

print("Problem 4: Operations on a = 6 and b = 4")
a, b = 6, 4
sum_ab, product, sq_a, sq_b = number_operations(a, b)
print(f"Sum: {sum_ab}")
print(f"Product: {product}")
print(f"Square of a: {sq_a}")
print(f"Square of b: {sq_b}")
