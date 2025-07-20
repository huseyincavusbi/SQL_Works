import timeit
from collections import deque

# --- 2. Inserting at the beginning ---
def insert_at_beginning_list():
    temp_list = list(range(100000))
    temp_list.insert(0, -1) # 0.777516 seconds

def insert_at_beginning_deque():
    temp_deque = deque(range(100000))
    temp_deque.appendleft(-1) # 0.917724 seconds

# Time the operations
time_list_insert = timeit.timeit(insert_at_beginning_list, number=1000)
time_deque_insert = timeit.timeit(insert_at_beginning_deque, number=1000)

print("\n--- Insertion at the Beginning ---")
print(f"list (array) insert time: {time_list_insert:.6f} seconds")
print(f"deque (linked list) insert time: {time_deque_insert:.6f} seconds")
print("-" * 20)