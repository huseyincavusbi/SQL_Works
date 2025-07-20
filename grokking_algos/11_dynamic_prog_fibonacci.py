import time

# --- Version 1: Naive Recursive Fibonacci ---
def fib_naive(n):
    """
    Calculates Fibonacci using naive recursion. 
    Time Complexity: O(2^n) - Exponential.
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# --- Version 2: Dynamic Programming with Memoization ---
# The cache to store results of subproblems we've already solved.
# We define it outside the function so it persists across calls.
fib_cache = {}

def fib_dynamic(n):
    """
    Calculates Fibonacci using dynamic programming (memoization).
    Time Complexity: O(n) - Linear.
    """
    # Base case: if the result is already in our cache, return it instantly.
    if n in fib_cache:
        return fib_cache[n]
    
    # Standard Fibonacci base case
    if n <= 1:
        return n
    
    # If not in the cache, compute it recursively...
    result = fib_dynamic(n - 1) + fib_dynamic(n - 2)
    
    # ...and STORE the result in our cache before returning.
    fib_cache[n] = result
    
    return result


# --- Main Benchmarking Section ---
if __name__ == "__main__":
    TARGET_NUMBER = 35 # A good number to show the performance difference

    # --- Benchmark Naive Version ---
    print(f"--- Benchmarking Naive Recursive Fibonacci for n={TARGET_NUMBER} ---")
    start_time_naive = time.perf_counter()
    result_naive = fib_naive(TARGET_NUMBER)
    end_time_naive = time.perf_counter()
    duration_naive = end_time_naive - start_time_naive
    
    print(f"Result: {result_naive}")
    print(f"Execution Time: {duration_naive:.4f} seconds\n")
    
    
    # --- Benchmark Dynamic Programming Version ---
    print(f"--- Benchmarking Dynamic Programming Fibonacci for n={TARGET_NUMBER} ---")
    # Make sure to clear the cache for a fair test if run multiple times
    fib_cache.clear() 
    
    start_time_dynamic = time.perf_counter()
    result_dynamic = fib_dynamic(TARGET_NUMBER)
    end_time_dynamic = time.perf_counter()
    duration_dynamic = end_time_dynamic - start_time_dynamic
    
    print(f"Result: {result_dynamic}")
    print(f"Execution Time: {duration_dynamic:.8f} seconds\n") 

    # --- Final Comparison ---
    print("--- Conclusion ---")
    if duration_dynamic > 0:
        speedup = duration_naive / duration_dynamic
        print(f"The dynamic programming version was approximately {speedup:,.2f} times faster!")
    else:
        print("The dynamic programming version was virtually instantaneous!")