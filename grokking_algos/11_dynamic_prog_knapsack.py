def knapsack_dp_visualized(items, max_weight):
    """
    Solves the 0/1 knapsack problem using dynamic programming (tabulation)
    and visualizes the process.
    """
    print("--- Starting Knapsack DP Algorithm ---")
    
    # Create the DP grid, initialized with zeros.
    # Rows = number of items + 1, Columns = max_weight + 1
    num_items = len(items)
    grid = [[0 for _ in range(max_weight + 1)] for _ in range(num_items + 1)]
    
    # Iterate through the items (rows)
    for i in range(1, num_items + 1):
        # The current item's properties (adjust for 0-based index)
        name, weight, value = items[i - 1]
        
        print(f"\nConsidering Item '{name}' (Weight: {weight}, Value: {value})")
        
        # Iterate through the knapsack capacities (columns)
        for w in range(1, max_weight + 1):
            # The value if we DON'T include the current item
            value_without_item = grid[i - 1][w]
            
            # The value if we DO include the current item
            value_with_item = 0
            # We can only include it if its weight is less than the current capacity
            if weight <= w:
                # Value of the item + max value of the remaining space
                remaining_weight = w - weight
                value_with_item = value + grid[i - 1][remaining_weight]
            
            # The cell gets the maximum of these two choices
            grid[i][w] = max(value_without_item, value_with_item)
            
    # Print the final grid for visualization
    print("\n--- Final DP Grid ---")
    for row in grid:
        print(row)
        
    # The final answer is in the bottom-right corner
    max_value = grid[num_items][max_weight]
    print(f"\nMaximum value that can be carried is: {max_value}")

# --- Let's run it ---
# Each item is a tuple: (name, weight, value)
store_items = [
    ("Guitar", 1, 1500),
    ("Stereo", 4, 3000),
    ("Laptop", 3, 2000)
]
knapsack_capacity = 4

knapsack_dp_visualized(store_items, knapsack_capacity)