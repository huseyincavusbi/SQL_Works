def binary_search_recursive_verbose(arr, target, low, high):
    """
    Performs a recursive binary search and prints its steps.
    """
    # The current slice of the array we are considering
    search_slice = arr[low:high+1]
    print(f"-> Searching for {target} in slice: {search_slice} (low={low}, high={high})")

    # Base Case (Failure)
    if low > high:
        print("   Base case hit: low > high. Target not found. Returning None.")
        return None

    mid = (low + high) // 2
    guess = arr[mid]
    print(f"   Midpoint is index {mid}, value is {guess}.")

    # Base Case (Success)
    if guess == target:
        print(f"   Base case hit: Guess ({guess}) == Target ({target}). Found! Returning index {mid}.")
        return mid
    
    # Recursive Case 1
    if guess > target:
        print(f"   Guess ({guess}) > Target ({target}). Searching left half next.")
        return binary_search_recursive_verbose(arr, target, low, mid - 1)
    # Recursive Case 2
    else: # guess < target
        print(f"   Guess ({guess}) < Target ({target}). Searching right half next.")
        return binary_search_recursive_verbose(arr, target, mid + 1, high)

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target_to_find = 13
print(f"\n--- Starting Recursive Binary Search for {target_to_find} ---")
found_index = binary_search_recursive_verbose(sorted_list, target_to_find, 0, len(sorted_list) - 1)
print(f"\nFinal result: {found_index}")