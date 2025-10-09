"""
Python Dictionary and Set Exercises Solutions
"""

print("="*60)
print("DICTIONARY EXERCISES")
print("="*60)

# Exercise 1: Sort a Dictionary by Value
print("\n1. Sort a Dictionary by Value")
print("-" * 40)
sample_dict = {3: 45, 1: 20, 2: 35, 4: 10}
print(f"Original dictionary: {sample_dict}")

# Ascending order
sorted_asc = dict(sorted(sample_dict.items(), key=lambda x: x[1]))
print(f"Sorted (ascending): {sorted_asc}")

# Descending order
sorted_desc = dict(sorted(sample_dict.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted (descending): {sorted_desc}")

# Exercise 2: Add a Key to a Dictionary
print("\n2. Add a Key to a Dictionary")
print("-" * 40)
my_dict = {0: 10, 1: 20}
print(f"Original dictionary: {my_dict}")
my_dict[2] = 30
print(f"After adding key: {my_dict}")

# Exercise 3: Concatenate Multiple Dictionaries
print("\n3. Concatenate Multiple Dictionaries")
print("-" * 40)
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print(f"dic1: {dic1}")
print(f"dic2: {dic2}")
print(f"dic3: {dic3}")

# Method 1: Using update()
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)
print(f"Concatenated (method 1): {result}")

# Method 2: Using unpacking (Python 3.5+)
result2 = {**dic1, **dic2, **dic3}
print(f"Concatenated (method 2): {result2}")

# Exercise 4: Generate a Dictionary with Squares (1 to n)
print("\n4. Generate a Dictionary with Squares")
print("-" * 40)
n = 5
squares_dict = {x: x*x for x in range(1, n+1)}
print(f"Dictionary (n={n}): {squares_dict}")

# Exercise 5: Dictionary of Squares (1 to 15)
print("\n5. Dictionary of Squares (1 to 15)")
print("-" * 40)
squares_15 = {x: x*x for x in range(1, 16)}
print(f"Dictionary: {squares_15}")

print("\n" + "="*60)
print("SET EXERCISES")
print("="*60)

# Exercise 1: Create a Set
print("\n1. Create a Set")
print("-" * 40)
my_set = {1, 2, 3, 4, 5}
print(f"Created set: {my_set}")

# Alternative ways to create sets
set_from_list = set([10, 20, 30, 40])
print(f"Set from list: {set_from_list}")

empty_set = set()
print(f"Empty set: {empty_set}")

# Exercise 2: Iterate Over a Set
print("\n2. Iterate Over a Set")
print("-" * 40)
colors = {"red", "green", "blue", "yellow"}
print(f"Set: {colors}")
print("Iterating over set:")
for color in colors:
    print(f"  - {color}")

# Exercise 3: Add Member(s) to a Set
print("\n3. Add Member(s) to a Set")
print("-" * 40)
fruits = {"apple", "banana", "orange"}
print(f"Original set: {fruits}")

# Add single item
fruits.add("mango")
print(f"After add('mango'): {fruits}")

# Add multiple items
fruits.update(["grape", "kiwi"])
print(f"After update(['grape', 'kiwi']): {fruits}")

# Exercise 4: Remove Item(s) from a Set
print("\n4. Remove Item(s) from a Set")
print("-" * 40)
numbers = {1, 2, 3, 4, 5, 6}
print(f"Original set: {numbers}")

# Using remove() - raises error if item doesn't exist
numbers.remove(3)
print(f"After remove(3): {numbers}")

# Using discard() - doesn't raise error if item doesn't exist
numbers.discard(5)
print(f"After discard(5): {numbers}")

# Using pop() - removes arbitrary item
popped = numbers.pop()
print(f"Popped item: {popped}")
print(f"After pop(): {numbers}")

# Exercise 5: Remove an Item if Present in the Set
print("\n5. Remove an Item if Present in the Set")
print("-" * 40)
animals = {"dog", "cat", "bird", "fish"}
print(f"Original set: {animals}")

# Using discard() - safe method, no error if item not present
animals.discard("cat")
print(f"After discard('cat'): {animals}")

animals.discard("elephant")  # Won't raise error
print(f"After discard('elephant') (not in set): {animals}")

# Alternative: Check before removing
item_to_remove = "bird"
if item_to_remove in animals:
    animals.remove(item_to_remove)
    print(f"Removed '{item_to_remove}': {animals}")

print("\n" + "="*60)
print("ALL EXERCISES COMPLETED!")
print("="*60)
