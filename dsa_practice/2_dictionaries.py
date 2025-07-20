
# This file covers the basics of dictionaries (hash maps in Python).

# 1. Creating a dictionary
# A dictionary is an unordered collection of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples).
print("--- Creating a dictionary ---")
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"my_dict: {my_dict}")

empty_dict = {}
print(f"empty_dict: {empty_dict}")


# 2. Accessing elements
# You can access values by their key.
print("\n--- Accessing elements ---")
print(f"Name: {my_dict['name']}")
# Using the .get() method is safer as it returns None if the key is not found, instead of raising a KeyError.
print(f"Country: {my_dict.get('country')}")
print(f"Country (with default): {my_dict.get('country', 'USA')}")


# 3. Adding and updating elements
# You can add new key-value pairs or update existing ones.
print("\n--- Adding and updating elements ---")
my_dict["email"] = "alice@example.com" # Add a new entry
print(f"After adding email: {my_dict}")

my_dict["age"] = 31 # Update an existing entry
print(f"After updating age: {my_dict}")


# 4. Removing elements
# You can remove elements using pop() or the del keyword.
print("\n--- Removing elements ---")
removed_age = my_dict.pop("age")
print(f"Removed age: {removed_age}")
print(f"Dictionary after popping age: {my_dict}")

del my_dict["city"]
print(f"Dictionary after deleting city: {my_dict}")


# 5. Iterating through a dictionary
print("\n--- Iterating through a dictionary ---")
# Iterate through keys
print("Keys:")
for key in my_dict.keys():
    print(key)

# Iterate through values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Iterate through key-value pairs
print("\nItems (key-value pairs):")
for key, value in my_dict.items():
    print(f"{key}: {value}")


# 6. Dictionary comprehensions
# A concise way to create dictionaries.
print("\n--- Dictionary comprehensions ---")
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dictionary: {squares_dict}")


# Time Complexity of Dictionary Operations (Average Case):
# - Accessing an element by key: O(1)
# - Adding/updating an element: O(1)
# - Removing an element: O(1)
# - Searching for a key: O(1)
# - Iterating over keys/values/items: O(n)
