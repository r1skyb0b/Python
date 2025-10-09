# List and Tuple Exercises - Solutions

# 1. Create and Access List Elements
print("=" * 50)
print("Exercise 1: Create and Access List Elements")
print("=" * 50)
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]
print(f"List of fruits: {fruits}")
print(f"Third fruit: {fruits[2]}")
print()

# 2. Concatenate Two Lists
print("=" * 50)
print("Exercise 2: Concatenate Two Lists")
print("=" * 50)
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
concatenated_list = list1 + list2
print(f"First list: {list1}")
print(f"Second list: {list2}")
print(f"Concatenated list: {concatenated_list}")
print()

# 3. Extract Elements from a List
print("=" * 50)
print("Exercise 3: Extract Elements from a List")
print("=" * 50)
numbers = [10, 20, 30, 40, 50, 60, 70]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]
extracted = [first, middle, last]
print(f"Original list: {numbers}")
print(f"Extracted elements (first, middle, last): {extracted}")
print()

# 4. Convert List to Tuple
print("=" * 50)
print("Exercise 4: Convert List to Tuple")
print("=" * 50)
movies_list = ["Inception", "The Matrix", "Interstellar", "The Shawshank Redemption", "The Dark Knight"]
movies_tuple = tuple(movies_list)
print(f"List of movies: {movies_list}")
print(f"Converted to tuple: {movies_tuple}")
print(f"Type: {type(movies_tuple)}")
print()

# 5. Check Element in a List
print("=" * 50)
print("Exercise 5: Check Element in a List")
print("=" * 50)
cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
print(f"List of cities: {cities}")
if "Paris" in cities:
    print("Paris is in the list!")
else:
    print("Paris is not in the list.")
print()

# 6. Duplicate a List Without Using Loops
print("=" * 50)
print("Exercise 6: Duplicate a List Without Using Loops")
print("=" * 50)
original_numbers = [1, 2, 3, 4, 5]
duplicated_list = original_numbers * 2
print(f"Original list: {original_numbers}")
print(f"Duplicated list: {duplicated_list}")
print()

# 7. Swap First and Last Elements of a List
print("=" * 50)
print("Exercise 7: Swap First and Last Elements")
print("=" * 50)
num_list = [5, 10, 15, 20, 25]
print(f"Original list: {num_list}")
num_list[0], num_list[-1] = num_list[-1], num_list[0]
print(f"After swapping first and last: {num_list}")
print()

# 8. Slice a Tuple
print("=" * 50)
print("Exercise 8: Slice a Tuple")
print("=" * 50)
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced_tuple = numbers_tuple[3:8]
print(f"Original tuple: {numbers_tuple}")
print(f"Slice from index 3 to 7: {sliced_tuple}")
print()

# 9. Count Occurrences in a List
print("=" * 50)
print("Exercise 9: Count Occurrences in a List")
print("=" * 50)
colors = ["red", "blue", "green", "blue", "yellow", "blue", "orange"]
blue_count = colors.count("blue")
print(f"List of colors: {colors}")
print(f"Number of times 'blue' appears: {blue_count}")
print()

# 10. Find the Index of an Element in a Tuple
print("=" * 50)
print("Exercise 10: Find Index of Element in Tuple")
print("=" * 50)
animals = ("cat", "dog", "lion", "tiger", "elephant")
lion_index = animals.index("lion")
print(f"Tuple of animals: {animals}")
print(f"Index of 'lion': {lion_index}")
print()

# 11. Merge Two Tuples
print("=" * 50)
print("Exercise 11: Merge Two Tuples")
print("=" * 50)
tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
merged_tuple = tuple1 + tuple2
print(f"First tuple: {tuple1}")
print(f"Second tuple: {tuple2}")
print(f"Merged tuple: {merged_tuple}")
print()

# 12. Find the Length of a List and Tuple
print("=" * 50)
print("Exercise 12: Find Length of List and Tuple")
print("=" * 50)
sample_list = [10, 20, 30, 40, 50]
sample_tuple = (100, 200, 300, 400)
print(f"List: {sample_list}")
print(f"Length of list: {len(sample_list)}")
print(f"Tuple: {sample_tuple}")
print(f"Length of tuple: {len(sample_tuple)}")
print()

# 13. Convert Tuple to List
print("=" * 50)
print("Exercise 13: Convert Tuple to List")
print("=" * 50)
numbers_tuple_13 = (5, 10, 15, 20, 25)
numbers_list = list(numbers_tuple_13)
print(f"Original tuple: {numbers_tuple_13}")
print(f"Converted to list: {numbers_list}")
print(f"Type: {type(numbers_list)}")
print()

# 14. Find Maximum and Minimum in a Tuple
print("=" * 50)
print("Exercise 14: Find Max and Min in Tuple")
print("=" * 50)
values_tuple = (45, 12, 78, 23, 67, 89, 34)
max_value = max(values_tuple)
min_value = min(values_tuple)
print(f"Tuple: {values_tuple}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print()

# 15. Reverse a Tuple
print("=" * 50)
print("Exercise 15: Reverse a Tuple")
print("=" * 50)
words_tuple = ("hello", "world", "python", "programming", "fun")
reversed_tuple = words_tuple[::-1]
print(f"Original tuple: {words_tuple}")
print(f"Reversed tuple: {reversed_tuple}")
print()

print("=" * 50)
print("All exercises completed!")
print("=" * 50)
