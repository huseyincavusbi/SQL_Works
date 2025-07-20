

# This file implements a Binary Search Tree (BST) from scratch.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # --- Insertion ---
    def insert(self, key):
        """Public method to insert a key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Private recursive helper for insertion. Time complexity: O(log n) on average, O(n) in the worst case."""
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        # If key is equal, we do nothing (no duplicates allowed in this BST)

    # --- Search ---
    def search(self, key):
        """Public method to search for a key. Returns the node if found, else None."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        """Private recursive helper for searching. Time complexity: O(log n) on average, O(n) in the worst case."""
        if current_node is None or current_node.val == key:
            return current_node
        if key < current_node.val:
            return self._search_recursive(current_node.left, key)
        return self._search_recursive(current_node.right, key)

    # --- Traversals ---
    # In-order traversal: Left -> Root -> Right. Visits nodes in ascending order.
    def in_order_traversal(self):
        """Performs an in-order traversal and prints the node values."""
        elements = []
        self._in_order_recursive(self.root, elements)
        print(f"In-order (sorted): {' -> '.join(map(str, elements))}")

    def _in_order_recursive(self, node, elements):
        if node:
            self._in_order_recursive(node.left, elements)
            elements.append(node.val)
            self._in_order_recursive(node.right, elements)

    # Pre-order traversal: Root -> Left -> Right.
    def pre_order_traversal(self):
        """Performs a pre-order traversal and prints the node values."""
        elements = []
        self._pre_order_recursive(self.root, elements)
        print(f"Pre-order: {' -> '.join(map(str, elements))}")

    def _pre_order_recursive(self, node, elements):
        if node:
            elements.append(node.val)
            self._pre_order_recursive(node.left, elements)
            self._pre_order_recursive(node.right, elements)

    # Post-order traversal: Left -> Right -> Root.
    def post_order_traversal(self):
        """Performs a post-order traversal and prints the node values."""
        elements = []
        self._post_order_recursive(self.root, elements)
        print(f"Post-order: {' -> '.join(map(str, elements))}")

    def _post_order_recursive(self, node, elements):
        if node:
            self._post_order_recursive(node.left, elements)
            self._post_order_recursive(node.right, elements)
            elements.append(node.val)

# --- Deletion ---
    def delete(self, key):
        """Public method to delete a key from the BST."""
        self.root = self._delete_recursive(self.root, key)

    def _find_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_recursive(self, current_node, key):
        """Private recursive helper for deletion. Time complexity: O(log n) on average, O(n) in the worst case."""
        if current_node is None:
            return current_node

        # Recur down the tree
        if key < current_node.val:
            current_node.left = self._delete_recursive(current_node.left, key)
        elif key > current_node.val:
            current_node.right = self._delete_recursive(current_node.right, key)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._find_min_value_node(current_node.right)
            current_node.val = temp.val
            # Delete the inorder successor
            current_node.right = self._delete_recursive(current_node.right, temp.val)
            
        return current_node

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Binary Search Tree Demonstration ---")
    bst = BinarySearchTree()
    nodes_to_insert = [50, 30, 20, 40, 70, 60, 80]
    print(f"\nInserting nodes: {nodes_to_insert}")
    for node_val in nodes_to_insert:
        bst.insert(node_val)

    print("\n--- Initial Tree ---")
    bst.in_order_traversal()

    print("\n--- Deleting a leaf node (20) ---")
    bst.delete(20)
    bst.in_order_traversal()

    print("\n--- Deleting a node with two children (70) ---")
    bst.delete(70)
    bst.in_order_traversal()

    print("\n--- Deleting the root node (50) ---")
    bst.delete(50)
    bst.in_order_traversal()
    
    print("\n--- Final Tree Traversals ---")
    bst.in_order_traversal()
    bst.pre_order_traversal()
    bst.post_order_traversal()

