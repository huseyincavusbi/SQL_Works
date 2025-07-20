import time

def create_multiplication_table(arr):
  """Creates a multiplication table. This is an O(n^2) operation."""
  # The outer loop runs 'n' times
  for multiplier in arr:
    # The inner loop runs 'n' times for each outer loop iteration
    for element in arr:
      # This operation happens n * n times
      _ = multiplier * element # Assign to dummy variable to ensure work is done

# --- Benchmark ---
list_100 = list(range(100))
list_500 = list(range(500))
list_1000 = list(range(1000))

# Time the 100-item list
start_time = time.perf_counter()
create_multiplication_table(list_100)
end_time = time.perf_counter()
print(f"Table for {len(list_100)} items took: {(end_time - start_time):.6f} seconds")

# Time the 500-item list
start_time = time.perf_counter()
create_multiplication_table(list_500)
end_time = time.perf_counter()
print(f"Table for {len(list_500)} items took: {(end_time - start_time):.6f} seconds")

# Time the 1000-item list
start_time = time.perf_counter()
create_multiplication_table(list_1000)
end_time = time.perf_counter()
print(f"Table for {len(list_1000)} items took: {(end_time - start_time):.6f} seconds")