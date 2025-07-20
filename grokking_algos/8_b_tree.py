
# First, a class for the nodes
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

# The main B-Tree class
class BTree:
    def __init__(self, t): # t is the minimum degree
        self.root = BTreeNode(leaf=True)
        self.t = t

    def insert(self, key):
        """Public method to insert a key."""
        root = self.root
        # If the root is full, the tree grows in height
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode()
            self.root = new_root
            new_root.children.insert(0, root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        """Helper to insert a key into a non-full node."""
        i = len(node.keys) - 1
        if node.leaf:
            # Find location for new key and insert it
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # Find the child which is going to have the new key
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            # If the found child is full, split it
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                # After split, the middle key of child moves up
                # and child is split into two. Check which of the two
                # is going to have the new key.
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent_node, child_index):
        """Splits a full child of a parent node."""
        t = self.t
        full_child = parent_node.children[child_index]
        new_child = BTreeNode(leaf=full_child.leaf)

        # Move the middle key of the full child up to the parent
        parent_node.keys.insert(child_index, full_child.keys[t - 1])
        parent_node.children.insert(child_index + 1, new_child)

        # Move the second half of the full child's keys to the new child
        new_child.keys = full_child.keys[t:(2 * t) - 1]
        full_child.keys = full_child.keys[0:t - 1]

        # If the child was not a leaf, move its children too
        if not full_child.leaf:
            new_child.children = full_child.children[t:(2 * t)]
            full_child.children = full_child.children[0:t]

    def visualize(self):
        """Prints a level-by-level visualization of the tree."""
        if not self.root:
            print("The tree is empty.")
            return

        q = [(self.root, 0)]
        level_nodes = [[]]
        current_level = 0

        while q:
            node, level = q.pop(0)
            if level > current_level:
                current_level = level
                level_nodes.append([])
            
            level_nodes[current_level].append(node.keys)
            
            if not node.leaf:
                for child in node.children:
                    q.append((child, level + 1))
        
        print("--- B-Tree Structure ---")
        for i, level in enumerate(level_nodes):
            print(f"Level {i}: ", end="")
            for node_keys in level:
                print(f"{node_keys}", end="  ")
            print()

# --- Create and populate the B-Tree with t=2 ---
b_tree = BTree(t=2)

keys_to_insert = [10, 20, 30, 5, 6, 7]

print("--- Building the B-Tree Step-by-Step ---\n")
for key in keys_to_insert:
    print(f">>> Inserting {key}...")
    b_tree.insert(key)
    b_tree.visualize()
    print("-" * 30)