import math

def binary_search_steps(n):
  """
  Calculates the maximum number of steps for a binary search (log search).
  """
  return math.ceil(math.log2(n))

# For a list of 128 names
list_size = 128
max_steps = binary_search_steps(list_size)
print(f"For a sorted list of {list_size} names, the maximum number of steps for a binary search is: {max_steps}")
