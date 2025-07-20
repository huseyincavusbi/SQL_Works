
# This file covers the basics of sets in Python.

# 1. Creating a set
# A set is an unordered collection of unique elements.
print("--- Creating a set ---")
my_set = {1, 2, 3, 4, 5, 5, 4} # Duplicate elements are automatically removed
print(f"my_set: {my_set}")

empty_set = set()
print(f"empty_set: {empty_set}")

# Creating a set from a list
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(list_with_duplicates)
print(f"Set from list: {set_from_list}")


# 2. Adding and removing elements
print("\n--- Adding and removing elements ---")
my_set.add(6)
print(f"After adding 6: {my_set}")

my_set.remove(3) # Raises a KeyError if the element is not found
print(f"After removing 3: {my_set}")

my_set.discard(10) # Does not raise an error if the element is not found
print(f"After discarding 10 (which is not in the set): {my_set}")

popped_element = my_set.pop() # Removes and returns an arbitrary element
print(f"Popped element: {popped_element}")
print(f"Set after pop: {my_set}")


# 3. Set operations
print("\n--- Set operations ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union: all elements from both sets
union_set = set_a.union(set_b) # or set_a | set_b
print(f"Union (A | B): {union_set}")

# Intersection: elements that are in both sets
intersection_set = set_a.intersection(set_b) # or set_a & set_b
print(f"Intersection (A & B): {intersection_set}")

# Difference: elements in set_a but not in set_b
difference_set = set_a.difference(set_b) # or set_a - set_b
print(f"Difference (A - B): {difference_set}")

# Symmetric Difference: elements in either set, but not both
symmetric_difference_set = set_a.symmetric_difference(set_b) # or set_a ^ set_b
print(f"Symmetric Difference (A ^ B): {symmetric_difference_set}")


# 4. Checking for membership
print("\n--- Checking for membership ---")
print(f"Is 2 in set_a? {2 in set_a}")
print(f"Is 10 in set_a? {10 in set_a}")


# Time Complexity of Set Operations (Average Case):
# - Adding an element: O(1)
# - Removing an element: O(1)
# - Checking for membership (e.g., `x in my_set`): O(1)
# - Union, Intersection, Difference: O(len(set1) + len(set2))
