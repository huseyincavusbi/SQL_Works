def max_recursive_verbose(numbers):
    """
    Recursively finds the max number and prints its steps.
    """
    print(f"-> Finding max in: {numbers}")

    # Base Case
    if len(numbers) == 1:
        print(f"   Base case hit: Only one item ({numbers[0]}). Returning it.")
        return numbers[0]
    # Recursive Case
    else:
        first_element = numbers[0]
        max_of_the_rest = max_recursive_verbose(numbers[1:])
        print(f"<- Resuming call for: {numbers}. Comparing {first_element} with max_of_the_rest ({max_of_the_rest}).")
        
        if first_element > max_of_the_rest:
            print(f"   {first_element} is bigger. Returning {first_element}.")
            return first_element
        else:
            print(f"   {max_of_the_rest} is bigger. Returning {max_of_the_rest}.")
            return max_of_the_rest

my_numbers = [5, 2, 9, 1]
print("\n--- Starting Recursive Max ---")
final_max = max_recursive_verbose(my_numbers)
print(f"\nFinal result: {final_max}")