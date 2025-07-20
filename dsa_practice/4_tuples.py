
# This file covers the basics of tuples in Python.

# 1. Creating a tuple
# A tuple is an ordered, immutable collection of items.
print("--- Creating a tuple ---")
my_tuple = (1, "hello", 3.14, True)
print(f"my_tuple: {my_tuple}")

# Parentheses are optional in many cases
another_tuple = 1, 2, 3
print(f"another_tuple: {another_tuple}")

# A tuple with a single element needs a trailing comma
single_element_tuple = (1,)
print(f"single_element_tuple: {single_element_tuple}")


# 2. Accessing elements
# Accessing elements is the same as with lists, using indexes.
print("\n--- Accessing elements ---")
print(f"The first element is: {my_tuple[0]}")
print(f"The last element is: {my_tuple[-1]}")


# 3. Slicing
# Slicing also works the same way as lists.
print("\n--- Slicing ---")
sub_tuple = my_tuple[1:3]
print(f"Sub-tuple from index 1 to 3 (exclusive): {sub_tuple}")


# 4. Immutability
# This is the key difference between tuples and lists. You cannot change a tuple.
print("\n--- Immutability ---")
try:
    my_tuple[0] = 99
except TypeError as e:
    print(f"Error when trying to change an element: {e}")


# 5. Tuple packing and unpacking
# This is a very common and useful feature.
print("\n--- Tuple packing and unpacking ---")
# Packing: variables are packed into a tuple
packed_tuple = 4, 5, "world"
print(f"Packed tuple: {packed_tuple}")

# Unpacking: values from a tuple are assigned to variables
a, b, c = packed_tuple
print(f"Unpacked variables: a={a}, b={b}, c={c}")


# 6. When to use tuples
# - For data that should not change (e.g., coordinates, configuration settings).
# - As dictionary keys (since they are immutable).
# - When you want a slight performance increase over lists for iteration.


# Time Complexity of Tuple Operations:
# - Accessing an element by index: O(1)
# - Slicing: O(k) where k is the size of the slice
# - Checking for membership (`x in my_tuple`): O(n)
