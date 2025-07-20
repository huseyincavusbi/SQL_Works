import collections

# The Node for our Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # This helps in sorting the nodes based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(text):
    """
    Performs Huffman Coding on a given text.
    """
    # 1. Count character frequencies
    frequency = collections.Counter(text)
    
    # 2. Create a list of leaf nodes
    nodes = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    
    # 3. Build the Huffman Tree
    while len(nodes) > 1:
        # Sort nodes to easily find the two with the smallest frequencies
        nodes.sort()
        
        # Get the two smallest nodes
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)
        
        # Create a new internal node
        # Its frequency is the sum of its children's frequencies
        # It has no character associated with it (char=None)
        merged_freq = left_node.freq + right_node.freq
        parent_node = HuffmanNode(None, merged_freq)
        parent_node.left = left_node
        parent_node.right = right_node
        
        # Add the new parent node back to the list
        nodes.append(parent_node)
        
    # The last remaining node is the root of the tree
    root = nodes[0]
    
    # 4. Generate codes by traversing the tree
    codes = {}
    def generate_codes(node, current_code=""):
        if node is None:
            return
        # If it's a leaf node, we've found a character code
        if node.char is not None:
            codes[node.char] = current_code
            return
        # Go left (add '0') and right (add '1')
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root)
    return codes, frequency

# --- Let's run it ---
my_text = "a simple sentence"
huffman_codes, frequencies = huffman_coding(my_text)

print(f"Original Text: '{my_text}'\n")
print("--- Huffman Codes ---")
# Sort by frequency for a nice display
sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

for char, freq in sorted_freq:
    print(f"Character: '{char}' | Frequency: {freq:<2} | Code: {huffman_codes[char]}")