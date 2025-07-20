
# This file implements and demonstrates Linear Search and Binary Search.

def linear_search(arr, target):
    """Searches for a target in an array using Linear Search. Time complexity: O(n)"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not in the list

def binary_search_iterative(arr, target):
    """Searches for a target in a sorted array using iterative Binary Search. Time complexity: O(log n)"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    return -1  # Target is not present in the array

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Searching Algorithm Demonstration ---")

    my_list = [2, 3, 4, 10, 40, 55, 67, 89, 91]
    target_to_find = 40

    print(f"List to search in: {my_list}")
    print(f"Target to find: {target_to_find}")

    # --- Linear Search ---
    print("\n--- Linear Search ---")
    linear_result = linear_search(my_list, target_to_find)
    if linear_result != -1:
        print(f"Target found at index: {linear_result}")
    else:
        print("Target not found.")

    # --- Binary Search ---
    # Note: Binary search requires the list to be sorted, which my_list already is.
    print("\n--- Binary Search ---")
    binary_result = binary_search_iterative(my_list, target_to_find)
    if binary_result != -1:
        print(f"Target found at index: {binary_result}")
    else:
        print("Target not found.")

    # --- Searching for a non-existent element ---
    target_to_find_2 = 99
    print(f"\nSearching for non-existent target: {target_to_find_2}")
    binary_result_2 = binary_search_iterative(my_list, target_to_find_2)
    if binary_result_2 != -1:
        print(f"Target found at index: {binary_result_2}")
    else:
        print("Target not found.")

