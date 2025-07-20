
# This file solves the 0/1 Knapsack problem using Dynamic Programming (Tabulation).

def knapsack_01(values, weights, capacity):
    """
    Solves the 0/1 Knapsack problem.
    :param values: A list of the values of the items.
    :param weights: A list of the weights of the items.
    :param capacity: The maximum weight capacity of the knapsack.
    :return: The maximum value that can be obtained.
    Time Complexity: O(n*W), where n is the number of items and W is the capacity.
    Space Complexity: O(n*W)
    """
    n = len(values)
    # Create a DP table to store the maximum value for a given weight and number of items.
    # dp[i][w] will be the maximum value that can be achieved with the first 'i' items and a capacity of 'w'.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # The current item's weight and value (using i-1 because of 0-based indexing)
            current_weight = weights[i-1]
            current_value = values[i-1]

            # If the current item's weight is more than the current capacity 'w',
            # we can't include it. So, the max value is the same as with the previous 'i-1' items.
            if current_weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                # If we can include the current item, we have two choices:
                # 1. Don't include the item: The value is the same as with the previous 'i-1' items (dp[i-1][w]).
                # 2. Include the item: The value is the current item's value plus the max value for the remaining capacity
                #    (w - current_weight) with the previous 'i-1' items.
                # We take the maximum of these two choices.
                include_item = current_value + dp[i-1][w - current_weight]
                exclude_item = dp[i-1][w]
                dp[i][w] = max(include_item, exclude_item)

    # The final answer is in the bottom-right cell of the table
    return dp[n][capacity]

# --- Demonstration ---
if __name__ == "__main__":
    print("--- 0/1 Knapsack Problem Demonstration ---")

    item_values = [60, 100, 120]
    item_weights = [10, 20, 30]
    knapsack_capacity = 50

    print(f"\nItem Values: {item_values}")
    print(f"Item Weights: {item_weights}")
    print(f"Knapsack Capacity: {knapsack_capacity}")

    max_value = knapsack_01(item_values, item_weights, knapsack_capacity)

    print(f"\nMaximum value that can be put in the knapsack: {max_value}")


