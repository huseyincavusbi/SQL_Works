class TreeNode:
    """A node for a Splay Tree. It includes a parent pointer."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    """A class representing a Splay Tree."""
    def __init__(self):
        self.root = None

    # --- Rotations (more complex due to parent pointers) ---
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # --- The Splay Operation ---
    def _splay(self, node):
        while node.parent:
            parent = node.parent
            grandparent = parent.parent
            if not grandparent: # Zig case
                if node == parent.left:
                    self._right_rotate(parent)
                else:
                    self._left_rotate(parent)
            elif node == parent.left and parent == grandparent.left: # Zig-Zig case (left-left)
                self._right_rotate(grandparent)
                self._right_rotate(parent)
            elif node == parent.right and parent == grandparent.right: # Zig-Zig case (right-right)
                self._left_rotate(grandparent)
                self._left_rotate(parent)
            elif node == parent.right and parent == grandparent.left: # Zig-Zag case (left-right)
                self._left_rotate(parent)
                self._right_rotate(grandparent)
            else: # Zig-Zag case (right-left)
                self._right_rotate(parent)
                self._left_rotate(grandparent)

    # --- Public Insert Method ---
    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
            return

        current = self.root
        parent = None
        while current:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else: # Key already exists, splay it and return
                self._splay(current)
                return

        new_node = TreeNode(key)
        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        
        # Splay the newly inserted node to the root
        self._splay(new_node)
        
    # --- Public Search Method ---
    def search(self, key):
        current = self.root
        last_visited = None
        while current:
            last_visited = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else: # Found it!
                self._splay(current)
                return True
        
        # If not found, splay the last visited node
        if last_visited:
            self._splay(last_visited)
        return False

    # --- Visualization Method ---
    def visualize(self):
        self._visualize_recursive(self.root, "", True)

    def _visualize_recursive(self, node, prefix, is_left):
        if not node:
            return
        if node.right:
            self._visualize_recursive(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
        if node.left:
            self._visualize_recursive(node.left, prefix + ("    " if is_left else "│   "), True)

# --- Create and populate the Splay Tree ---
splay_tree = SplayTree()

# Insert keys one by one to see the splaying in action
keys_to_insert = [30, 20, 10, 50, 40] 

print("--- Building the Splay Tree Step-by-Step ---")
for key in keys_to_insert:
    print(f"\n>>> Inserting {key}...")
    splay_tree.insert(key)
    print("Tree Structure:")
    splay_tree.visualize()
    print("-" * 20)

print("\n\n--- Now, let's search for an element ---")
print(">>> Searching for 30...")
splay_tree.search(30)
print("Tree Structure after searching for 30:")
splay_tree.visualize()