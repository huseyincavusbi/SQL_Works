# This file covers the basics of arrays (lists in Python).

# 1. Creating a list
# A list is an ordered collection of items. The items can be of different types.
print("--- Creating a list ---")
my_list = [1, "hello", 3.14, True]
print(f"my_list: {my_list}")

empty_list = []
print(f"empty_list: {empty_list}")


# 2. Accessing elements
# You can access elements of a list using their index. The index starts from 0.
print("\n--- Accessing elements ---")
print(f"The first element is: {my_list[0]}")
print(f"The last element is: {my_list[-1]}")


# 3. Slicing
# You can get a sublist from a list using slicing.
print("\n--- Slicing ---")
sub_list = my_list[1:3]
print(f"Sublist from index 1 to 3 (exclusive): {sub_list}")


# 4. Adding elements
# You can add elements to a list using append() or insert().
print("\n--- Adding elements ---")
my_list.append("new item")
print(f"After appending 'new item': {my_list}")

my_list.insert(1, "inserted item")
print(f"After inserting 'inserted item' at index 1: {my_list}")


# 5. Removing elements
# You can remove elements using remove() or pop().
print("\n--- Removing elements ---")
my_list.remove("hello")
print(f"After removing 'hello': {my_list}")

popped_item = my_list.pop(2)
print(f"Popped item at index 2: {popped_item}")
print(f"List after popping: {my_list}")


# 6. Iterating through a list
print("\n--- Iterating through a list ---")
for item in my_list:
    print(item)


# 7. List comprehensions
# A concise way to create lists.
print("\n--- List comprehensions ---")
squares = [x**2 for x in range(5)]
print(f"Squares of numbers from 0 to 4: {squares}")


# Time Complexity of List Operations:
# - Accessing an element by index: O(1)
# - Appending an element: O(1)
# - Inserting an element at a specific position: O(n)
# - Removing an element by value: O(n)
# - Removing an element by index: O(n)
# - Searching for an element: O(n)
# - Slicing: O(k) where k is the size of the slice