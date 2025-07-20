import time

def print_elements(arr):
  """Prints each element in an array. This is an O(n) operation."""
  for element in arr:
    # This action is performed 'n' times.
    pass # We use 'pass' to avoid cluttering the output during timing.
         # The 'for' loop itself is the O(n) work.

# --- Benchmark ---
small_list = list(range(100))
large_list = list(range(10000))

# Time the small list
start_time = time.perf_counter()
print_elements(small_list)
end_time = time.perf_counter()
print(f"Printing {len(small_list)} items took: {(end_time - start_time) * 1e6:.2f} microseconds")

# Time the large list
start_time = time.perf_counter()
print_elements(large_list)
end_time = time.perf_counter()
print(f"Printing {len(large_list)} items took: {(end_time - start_time) * 1e6:.2f} microseconds")

### 4.6: Doubling the value of each element in an array
import time

def double_all_elements(arr):
  """Doubles the value of each element. This is an O(n) operation."""
  for i in range(len(arr)):
    # This read/write operation is performed 'n' times.
    arr[i] *= 2

# --- Benchmark ---
small_list = list(range(100))
large_list = list(range(10000))

# Time the small list
start_time = time.perf_counter()
double_all_elements(small_list)
end_time = time.perf_counter()
print(f"Doubling {len(small_list)} items took: {(end_time - start_time) * 1e6:.2f} microseconds")

# Time the large list
start_time = time.perf_counter()
double_all_elements(large_list)
end_time = time.perf_counter()
print(f"Doubling {len(large_list)} items took: {(end_time - start_time) * 1e6:.2f} microseconds")