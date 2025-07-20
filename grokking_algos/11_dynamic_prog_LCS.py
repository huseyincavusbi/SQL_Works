def longest_common_substring(s1, s2):
    """
    Finds the longest common substring between two strings using dynamic programming.
    """
    print(f"--- Finding Longest Common Substring between '{s1}' and '{s2}' ---")
    
    # Get the lengths of the strings
    m = len(s1)
    n = len(s2)
    
    # Create the DP grid (m+1 rows, n+1 columns) initialized to all zeros
    dp_grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Variables to store the length of the longest substring found so far and the row index where it ends.
    max_length = 0
    end_index_s1 = 0
    
    # Fill the DP grid
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters match, extend the common substring
            # Note: s1[i-1] and s2[j-1] are used because strings are 0-indexed while our grid is (m+1)x(n+1).
            if s1[i - 1] == s2[j - 1]:
                # The new length is 1 + the length of the common substring
                # ending at the previous characters.
                dp_grid[i][j] = dp_grid[i - 1][j - 1] + 1
                
                # Check if this is the new longest substring we've found
                if dp_grid[i][j] > max_length:
                    max_length = dp_grid[i][j]
                    end_index_s1 = i # Record the end position in s1
            else:
                # If characters do not match, the common substring is broken.
                dp_grid[i][j] = 0
                
    # --- Visualization of the final DP grid ---
    print("\n--- Final Dynamic Programming Grid ---")
    # Header for columns
    print("      " + "   ".join(s2))
    print("    " + "-" * (len(s2) * 4))
    
    for i, row in enumerate(dp_grid):
        # Header for rows
        row_char = s1[i-1] if i > 0 else '"'
        print(f'"{row_char}" |', end="")
        for val in row:
            print(f"{val:^3}", end=" ")
        print()
        
    # --- Reconstruct the longest common substring ---
    if max_length == 0:
        lcs = ""
    else:
        # Slice the original string s1 to get the result
        start_index_s1 = end_index_s1 - max_length
        lcs = s1[start_index_s1:end_index_s1]
        
    print("\n--- Results ---")
    print(f"Length of the Longest Common Substring: {max_length}")
    print(f"The Longest Common Substring is: '{lcs}'")
    
    return max_length, lcs

# --- Run the example from the book ---
string1 = "blue"
string2 = "clues"
longest_common_substring(string1, string2)