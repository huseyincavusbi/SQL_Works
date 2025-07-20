def simple_hash(key_string, array_size):
  """
  A very simple hash function for strings.
  1. Converts each character to its ASCII number.
  2. Sums the numbers.
  3. Uses modulo to fit the sum into the array size.
  """
  total = 0
  for char in key_string:
    total += ord(char) # ord() gets the ASCII value of a character
  
  # The modulo is the magic that maps the large 'total' to a valid index
  return total % array_size

array_size = 10 # Our array has 10 slots (indices 0 through 9)

index_for_apple = simple_hash("apple", array_size)
index_for_banana = simple_hash("banana", array_size)
index_for_bob = simple_hash("bob", array_size)

print(f"The key 'apple' maps to index: {index_for_apple}")
print(f"The key 'banana' maps to index: {index_for_banana}")
print(f"The key 'bob' maps to index: {index_for_bob}")

# Notice a 'collision' - two different keys map to the same spot!
index_for_obb = simple_hash("obb", array_size)
print(f"The key 'obb' maps to index: {index_for_obb}") # Also maps to the same index as 'bob'