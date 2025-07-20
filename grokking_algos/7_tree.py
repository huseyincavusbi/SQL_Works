class TreeNode:
    """A simple node for a binary tree."""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def visualize_tree(node, prefix="", is_left=True):
    """Prints a tree structure in a readable format."""
    if node is None:
        return

    if node.right:
        visualize_tree(node.right, prefix + ("│   " if is_left else "    "), False)

    # Print the current node
    print(prefix + ("└── " if is_left else "┌── ") + str(node.data))

    if node.left:
        visualize_tree(node.left, prefix + ("    " if is_left else "│   "), True)


# --- Let's build a simple tree manually ---

# Level 3 (Leaves)
leaf1 = TreeNode(2)
leaf2 = TreeNode(7)
leaf3 = TreeNode(12)

# Level 2
node_level2_left = TreeNode(5, left=leaf1, right=leaf2)
node_level2_right = TreeNode(15, left=leaf3)

# Level 1 (Root)
root = TreeNode(10, left=node_level2_left, right=node_level2_right)


# --- Now, let's visualize it ---
print("--- Simple Tree Visualization ---")
visualize_tree(root)