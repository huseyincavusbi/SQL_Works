import time

class Counter:
    def __init__(self):
        self.comparisons = 0
        
def merge_sort_verbose(arr, counter):
    """Sorts a list using Merge Sort, printing steps and counting comparisons."""
    print(f"-> Calling merge_sort on: {arr}")
    # Base Case: A list with 1 or 0 elements is already sorted.
    # Recurse First, Work Later
    if len(arr) <= 1:
        print(f"   Base case hit. Returning: {arr}")
        return arr

    # 1. Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    print(f"   Dividing into: {left_half} and {right_half}")

    # 2. Recurse
    sorted_left = merge_sort_verbose(left_half, counter)
    sorted_right = merge_sort_verbose(right_half, counter)

    # 3. Conquer (The real work is in the merge step)
    print(f"<- Merging {sorted_left} and {sorted_right}")
    return merge_timed(sorted_left, sorted_right, counter)

def merge_timed(left, right, counter):
    """Helper function to merge two sorted lists and count comparisons."""
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        # A comparison happens here!
        counter.comparisons += 1
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    print(f"   Merged result is: {merged}")
    return merged

# --- Run the example ---
data_merge = [10, 80, 30, 90, 40]
merge_counter = Counter()

print("\n--- Starting Merge Sort ---")
start_time = time.perf_counter()
sorted_merge = merge_sort_verbose(data_merge, merge_counter)
end_time = time.perf_counter()

print("\n--- Merge Sort Summary ---")
print(f"Final sorted list: {sorted_merge}")
print(f"Execution Time: {(end_time - start_time) * 1e6:.2f} microseconds")
print(f"Total Comparisons: {merge_counter.comparisons}")