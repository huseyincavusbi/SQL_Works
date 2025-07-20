class TreeNode:
    """A node for a Binary Search Tree."""
    def __init__(self, key):
        self.key = key  # The value of the node
        self.left = None
        self.right = None

class BinarySearchTree:
    """A class representing a Binary Search Tree."""
    def __init__(self):
        self.root = None # A new tree is initially empty

    # --- Public insert method ---
    def insert(self, key):
        """Public method to insert a new key into the tree."""
        # If the tree is empty, the new node becomes the root
        if self.root is None:
            self.root = TreeNode(key)
        else:
            # Otherwise, call the private recursive helper function
            self._insert_recursive(self.root, key)

    # --- Private recursive helper for insert ---
    def _insert_recursive(self, current_node, key):
        """Recursively find the correct spot to insert the new key."""
        # If the new key is less than the current node's key, go left
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = TreeNode(key)
            else:
                self._insert_recursive(current_node.left, key)
        # If the new key is greater than the current node's key, go right
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = TreeNode(key)
            else:
                self._insert_recursive(current_node.right, key)
        # If key is equal, we do nothing (no duplicate keys allowed in this simple BST)

    # --- Public search method ---
    def search(self, key):
        """Public method to search for a key. Returns True if found, False otherwise."""
        return self._search_recursive(self.root, key)

    # --- Private recursive helper for search ---
    def _search_recursive(self, current_node, key):
        """Recursively search for a key starting from the current node."""
        # Base Case 1: The node doesn't exist (we've hit the bottom) or tree is empty
        if current_node is None:
            return False
        # Base Case 2: We found the key!
        if current_node.key == key:
            return True
        
        # Recursive Step: Decide whether to go left or right
        if key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else: # key > current_node.key
            return self._search_recursive(current_node.right, key)

    # --- Visualization Method ---
    def visualize(self):
        """Prints a visual representation of the tree."""
        self._visualize_recursive(self.root, "", True)

    def _visualize_recursive(self, node, prefix, is_left):
        if node is None:
            return
        if node.right:
            self._visualize_recursive(node.right, prefix + ("│   " if is_left else "    "), False)
        
        print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
        
        if node.left:
            self._visualize_recursive(node.left, prefix + ("    " if is_left else "│   "), True)

# --- Create and populate the BST ---
bst = BinarySearchTree()
keys_to_insert = [10, 5, 15, 2, 7, 12, 18]

print(f"Inserting the following keys: {keys_to_insert}")
for key in keys_to_insert:
    bst.insert(key)

print("\n--- Visualizing the Final Tree ---")
bst.visualize()

print("\n--- Searching for values ---")
print(f"Is 7 in the tree?  {bst.search(7)}")   # Expected: True
print(f"Is 20 in the tree? {bst.search(20)}")  # Expected: False