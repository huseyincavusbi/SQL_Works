
# This solution uses a hash map for an efficient O(n) time complexity.

def two_sum(nums, target):
    """
    Finds two numbers in a list that add up to a specific target.
    :param nums: A list of integers.
    :param target: The target integer sum.
    :return: A list containing the indices of the two numbers, or an empty list if no solution is found.
    """
    num_to_index = {}  # Hash map to store number -> index

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            # Found the pair
            return [num_to_index[complement], index]
        # Store the current number and its index for future lookups
        num_to_index[num] = index

    return [] # Should not be reached based on problem description

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Practice Problem: Two Sum ---")

    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"\nInput: nums = {nums1}, target = {target1}")
    result1 = two_sum(nums1, target1)
    print(f"Output: {result1}") # Expected: [0, 1]

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\nInput: nums = {nums2}, target = {target2}")
    result2 = two_sum(nums2, target2)
    print(f"Output: {result2}") # Expected: [1, 2]

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    print(f"\nInput: nums = {nums3}, target = {target3}")
    result3 = two_sum(nums3, target3)
    print(f"Output: {result3}") # Expected: [0, 1]

