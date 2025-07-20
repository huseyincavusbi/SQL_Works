
# This file implements and demonstrates several common sorting algorithms.

def bubble_sort(arr):
    """Sorts an array using the Bubble Sort algorithm. Time complexity: O(n^2)"""
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    """Sorts an array using the Insertion Sort algorithm. Time complexity: O(n^2)"""
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    """Sorts an array using the Merge Sort algorithm. Time complexity: O(n log n)"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Recursive call on each half
        merge_sort(L)
        merge_sort(R)

        # Merge the two halves
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    """Sorts an array using the Quick Sort algorithm. Time complexity: O(n log n) on average."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Sorting Algorithm Demonstration ---")
    
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original list: {unsorted_list}")

    # --- Bubble Sort ---
    # Make a copy to not modify the original list
    list_for_bubble = list(unsorted_list)
    print(f"\nBubble Sort Result: {bubble_sort(list_for_bubble)}")

    # --- Insertion Sort ---
    list_for_insertion = list(unsorted_list)
    print(f"Insertion Sort Result: {insertion_sort(list_for_insertion)}")

    # --- Merge Sort ---
    list_for_merge = list(unsorted_list)
    print(f"Merge Sort Result: {merge_sort(list_for_merge)}")

    # --- Quick Sort ---
    list_for_quick = list(unsorted_list)
    print(f"Quick Sort Result: {quick_sort(list_for_quick)}")
