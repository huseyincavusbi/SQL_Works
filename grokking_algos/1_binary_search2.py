import math

def binary_search_steps(n):
  """
  Calculates the maximum number of steps for a binary search.
  """
  return math.ceil(math.log2(n))

# Original list size
original_list_size = 128
original_max_steps = binary_search_steps(original_list_size)
print(f"For a sorted list of {original_list_size} names, the maximum number of steps is: {original_max_steps}")

# Doubled list size
doubled_list_size = original_list_size * 2
doubled_max_steps = binary_search_steps(doubled_list_size)
print(f"For a sorted list of {doubled_list_size} names, the maximum number of steps is: {doubled_max_steps}")