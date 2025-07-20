def simple_search_with_steps(data_list, target):
  """
  Performs a simple search (linear search) and returns the index and the number of steps taken.
  """
  steps = 0
  for i, item in enumerate(data_list):
    steps += 1  # Increment step counter for each comparison
    if item == target:
      return i, steps
  return None, steps # Target not found

# Create a sorted list of 128 numbers (0 to 127)
my_list = list(range(128))

# Target is the last element (worst-case for simple search)
target_value = 127

# Perform the simple search
index, steps_taken = simple_search_with_steps(my_list, target_value)

print(f"--- Simple Search ---")
print(f"List size: {len(my_list)}")
if index is not None:
  print(f"Target {target_value} found at index {index} in {steps_taken} steps.")
else:
  print(f"Target {target_value} not found after {steps_taken} steps.")