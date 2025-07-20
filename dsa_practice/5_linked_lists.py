
# This file implements a Singly Linked List from scratch.

# A Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # The pointer to the next node

# The LinkedList class to manage the nodes
class LinkedList:
    def __init__(self):
        self.head = None  # The head (or first node) of the list

    # Method to add a new node to the end of the list (append)
    # Time Complexity: O(n) because we have to traverse to the end
    def append(self, data):
        new_node = Node(data)
        if not self.head: # If the list is empty, the new node is the head
            self.head = new_node
            return
        last_node = self.head
        while last_node.next: # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node # Link the last node to the new node

    # Method to add a new node to the beginning of the list (prepend)
    # Time Complexity: O(1)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to delete a node with a given key
    # Time Complexity: O(n) in the worst case (if the element is at the end)
    def delete(self, key):
        current_node = self.head

        # If the head node itself holds the key to be deleted
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # If the key was not present in the linked list
        if not current_node:
            return

        # Unlink the node from the linked list
        prev.next = current_node.next
        current_node = None

    # Method to display the linked list
    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(elements))


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Linked List Demonstration ---")
    llist = LinkedList()

    print("\nAppending elements 1, 2, 3:")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.display()

    print("\nPrepending element 0:")
    llist.prepend(0)
    llist.display()

    print("\nDeleting element 2:")
    llist.delete(2)
    llist.display()

    print("\nDeleting head element 0:")
    llist.delete(0)
    llist.display()

    print("\nTrying to delete a non-existent element (99):")
    llist.delete(99)
    llist.display()
