from cmath import log


class TreeNode:
    """A node for an AVL Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # A new node is initially at height 1

class AVLTree:
    """A class representing an AVL Tree."""

    # --- Core insert function (recursive) ---
    def insert(self, root, key):
        # 1. Perform standard BST insertion
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3. Get the balance factor
        balance = self.getBalance(root)
        print(f"Node {root.key} has balance: {balance}") # For visualization

        # 4. If the node becomes unbalanced, then try out the 4 cases
        # Left-Left Case
        if balance < -1 and key < root.left.key:
            print(f"  Imbalance found at node {root.key}! Performing Right Rotation.")
            return self.rightRotate(root)

        # Right-Right Case
        if balance > 1 and key > root.right.key:
            print(f"  Imbalance found at node {root.key}! Performing Left Rotation.")
            return self.leftRotate(root)

        # Left-Right Case
        if balance < -1 and key > root.left.key:
            print(f"  Imbalance found at node {root.key}! Performing Left-Right Rotation.")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right-Left Case
        if balance > 1 and key < root.right.key:
            print(f"  Imbalance found at node {root.key}! Performing Right-Left Rotation.")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # --- Rotation Helper Functions ---
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        # Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        # Return the new root
        return y

    # --- Height and Balance Helper Functions ---
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.right) - self.getHeight(root.left)

    # --- Visualization Method ---
    def visualize(self, root):
        self._visualize_recursive(root, "", True)

    def _visualize_recursive(self, node, prefix, is_left):
        if not node:
            return
        if node.right:
            self._visualize_recursive(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
        if node.left:
            self._visualize_recursive(node.left, prefix + ("    " if is_left else "│   "), True)

# --- Create and populate the AVL Tree ---
avl_tree = AVLTree()
root = None

# Insert keys one by one to see the balancing in action
# This sequence will trigger a simple Left Rotation
keys_to_insert = [10, 20, 30] 

print("--- Building the AVL Tree Step-by-Step ---")
for key in keys_to_insert:
    print(f"\n>>> Inserting {key}...")
    root = avl_tree.insert(root, key)
    print("Current Tree Structure:")
    avl_tree.visualize(root)
    print("-" * 20)

# AVL trees are self-balancing BSTs, guaranteeing their height will be O(log n).
