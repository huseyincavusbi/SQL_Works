def factorial(n):
    # Base Case: When n is 1, we stop.
    if n == 1:
        print(f"Base case hit for n={n}. Returning 1.")
        return 1
    # Recursive Case:
    else:
        print(f"Recursive call for n={n}. Calling factorial({n-1})...")
        return n * factorial(n-1)

result = factorial(4)
print(f"\nFinal result: {result}")