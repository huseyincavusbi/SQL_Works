import time

# A simple class to hold our comparison counter
class Counter:
    def __init__(self):
        self.comparisons = 0

def quicksort_verbose(arr, counter):
    """Sorts a list using Quicksort, printing steps and counting comparisons."""
    # Partition First, Recurse Later
    print(f"-> Calling quicksort on: {arr}")
    
    # In this implementation, every element (except the pivot) is compared once per call.
    if len(arr) > 1:
        counter.comparisons += len(arr) - 1
    
    # Base Case: A list with 0 or 1 element is already sorted.
    if len(arr) < 2:
        print(f"   Base case hit. Returning: {arr}")
        return arr
    # Recursive Case
    else:
        pivot = arr[0]
        print(f"   Pivot is {pivot}. Partitioning...")
        
        # Partition the list into two sub-lists
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        print(f"     Less than pivot: {less}, Greater than pivot: {greater}")
        
        # Recursively sort the sub-lists
        sorted_less = quicksort_verbose(less, counter)
        sorted_greater = quicksort_verbose(greater, counter)
        
        # Combine the results
        result = sorted_less + [pivot] + sorted_greater
        print(f"<- Returning combined: {result}")
        return result

data_quick = [10, 80, 30, 90, 40]
quick_counter = Counter()

print("--- Starting Quicksort ---")
start_time = time.perf_counter()
sorted_quick = quicksort_verbose(data_quick, quick_counter)
end_time = time.perf_counter()

print("\n--- Quicksort Summary ---")
print(f"Final sorted list: {sorted_quick}")
print(f"Execution Time: {(end_time - start_time) * 1e6:.2f} microseconds") # Using microseconds for small lists
print(f"Total Comparisons: {quick_counter.comparisons}")