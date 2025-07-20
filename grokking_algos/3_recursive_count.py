def count_recursive_verbose(items):
    """
    Recursively counts items and prints its steps.
    """
    print(f"-> Calling count_recursive with list: {items}")
    
    # Base Case
    if not items:
        print("   Base case hit: List is empty. Returning 0.")
        return 0
    # Recursive Case
    else:
        # The recursive call happens *inside* the return statement
        # so we calculate it first to be able to print the result.
        result_from_below = count_recursive_verbose(items[1:])
        my_result = 1 + result_from_below
        print(f"<- Returning from call with list: {items}. Will return 1 + {result_from_below} = {my_result}")
        return my_result

# --- Let's test it ---
my_list = ['a', 'b', 'c']
print("--- Starting Recursive Count ---")
final_count = count_recursive_verbose(my_list)
print(f"\nFinal result: {final_count}")