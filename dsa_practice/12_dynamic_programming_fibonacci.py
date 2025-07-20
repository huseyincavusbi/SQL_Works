
# This file introduces Dynamic Programming using the Fibonacci sequence as an example.
import time

# 1. Naive Recursive Approach
# This approach is very slow for larger n due to re-computation of the same subproblems.
# Time Complexity: O(2^n) - Exponential
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

# 2. Dynamic Programming - Memoization (Top-Down)
# We store the results of expensive function calls and return the cached result when the same inputs occur again.
def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    result = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    memo[n] = result
    return result

# 3. Dynamic Programming - Tabulation (Bottom-Up)
# We build the solution iteratively from the base cases up to the desired number.
# This is often more space-efficient.
# Time Complexity: O(n) - Linear
# Space Complexity: O(n) - Linear (can be optimized to O(1))
def fibonacci_tabulation(n):
    if n <= 1:
        return n
    
    # Create a table to store fibonacci numbers
    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    for i in range(2, n + 1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]

    return fib_table[n]

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Dynamic Programming Demonstration: Fibonacci ---")

    n_value = 35

    print(f"Calculating the {n_value}th Fibonacci number:\n")

    # --- Memoization (fast) ---
    start_time = time.time()
    fib_memo = fibonacci_memoization(n_value, memo={}) # Reset memo for clean run
    end_time = time.time()
    print(f"DP (Memoization) Result: {fib_memo}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    # --- Tabulation (fast) ---
    start_time = time.time()
    fib_tab = fibonacci_tabulation(n_value)
    end_time = time.time()
    print(f"\nDP (Tabulation) Result:  {fib_tab}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    # --- Naive (slow) ---
    # Note: This will be noticeably slow. For n > 40, it can take a very long time.
    print("\n--- WARNING: The naive recursive approach is very slow. ---")
    start_time = time.time()
    fib_naive = fibonacci_naive(n_value)
    end_time = time.time()
    print(f"\nNaive Recursive Result:  {fib_naive}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
