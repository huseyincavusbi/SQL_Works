import time
import random
import sys

# Set a higher recursion limit for Quicksort with larger lists
sys.setrecursionlimit(20000)

def selection_sort(data_list):
    # This function is O(n^2)
    for i in range(len(data_list) - 1):
        min_index = i
        for j in range(i + 1, len(data_list)):
            if data_list[j] < data_list[min_index]:
                min_index = j
        if min_index != i:
            data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
    return data_list

def quicksort(data_list): # Divide and conquer 
    # This function is O(n log n) on average
    if len(data_list) < 2:
        return data_list
    else:
        pivot = data_list[0]
        less = [i for i in data_list[1:] if i <= pivot]
        greater = [i for i in data_list[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# --- Benchmark ---
list_sizes = [100, 500, 1000, 5000]

print("--- Sorting Time Comparison ---")
print(f"{'List Size':<12} | {'Selection Sort':<18} | {'Quicksort':<15}")
print("-" * 50)

for size in list_sizes:
    # Generate a new random list for each test
    data = [random.randint(0, size * 10) for _ in range(size)]

    # Time Selection Sort
    selection_data = data.copy()
    start_time_ss = time.perf_counter()
    selection_sort(selection_data)
    end_time_ss = time.perf_counter()
    time_ss = end_time_ss - start_time_ss

    # Time Quicksort
    quick_data = data.copy()
    start_time_qs = time.perf_counter()
    quicksort(quick_data)
    end_time_qs = time.perf_counter()
    time_qs = end_time_qs - start_time_qs

    print(f"{size:<12} | {time_ss:<18.6f} | {time_qs:<15.6f}")