import time
from collections import deque

# --- Setup ---
# Create the data structures once, outside the timing loop.
num_items = 100_000
my_list = list(range(num_items))
my_deque = deque(range(num_items))

# --- 1. Time Deleting 10,000 items from the list (array) ---
start_time_list = time.perf_counter()

for _ in range(10000): 
    my_list.pop(0)

end_time_list = time.perf_counter()
time_list = end_time_list - start_time_list

print("--- Corrected Benchmark: Deleting 10,000 items from the front ---")
print(f"Time for list (array): {time_list:.6f} seconds")


# --- 2. Time Deleting 10,000 items from the deque (linked list) ---
start_time_deque = time.perf_counter()

for _ in range(10000): 
    my_deque.popleft()

end_time_deque = time.perf_counter()
time_deque = end_time_deque - start_time_deque

print(f"Time for deque (linked list): {time_deque:.6f} seconds")
print("-" * 20)