
# This file implements a Stack using a Python list.

class Stack:
    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def is_empty(self):
        """Checks if the stack is empty. Time complexity: O(1)"""
        return not self.items

    def push(self, item):
        """Adds an item to the top of the stack. Time complexity: O(1)"""
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item of the stack. Returns None if the stack is empty. Time complexity: O(1)"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Returns the top item of the stack without removing it. Returns None if the stack is empty. Time complexity: O(1)"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        """Returns the number of items in the stack. Time complexity: O(1)"""
        return len(self.items)

    def display(self):
        """Displays the stack content."""
        print(f"Stack (top to bottom): {self.items[::-1]}")


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Stack Demonstration ---")
    s = Stack()

    print(f"Is stack empty? {s.is_empty()}")

    print("\nPushing elements 10, 20, 30:")
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print(f"Stack size: {s.size()}")

    print(f"\nPeek at top element: {s.peek()}")

    print(f"\nPopping an element: {s.pop()}")
    s.display()

    print(f"\nPopping another element: {s.pop()}")
    s.display()

    print(f"\nIs stack empty? {s.is_empty()}")

    print(f"\nPopping last element: {s.pop()}")
    print(f"Popping from an empty stack: {s.pop()}")
    s.display()
    print(f"Is stack empty? {s.is_empty()}")
