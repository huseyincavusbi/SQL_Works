import timeit
from collections import deque

# Setup a large list and a large deque
num_items = 100_000
my_list = list(range(num_items))
my_deque = deque(range(num_items))

# --- 1. Accessing an element in the middle ---
def get_list_middle_element():
    _ = my_list[num_items // 2]

def get_deque_middle_element():
    _ = my_deque[num_items // 2]

# Time the operations
time_list = timeit.timeit(get_list_middle_element, number=10000)
time_deque = timeit.timeit(get_deque_middle_element, number=10000)

print("--- Access by Index (Reading) ---")
print(f"list (array) access time: {time_list:.6f} seconds")
print(f"deque (linked list) access time: {time_deque:.6f} seconds")
print("-" * 20)