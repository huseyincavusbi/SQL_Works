
# This file implements a Queue using collections.deque for efficiency.
from collections import deque

class Queue:
    def __init__(self):
        """Initializes an empty queue using a deque object."""
        self.items = deque()

    def is_empty(self):
        """Checks if the queue is empty. Time complexity: O(1)"""
        return not self.items

    def enqueue(self, item):
        """Adds an item to the back of the queue. Time complexity: O(1)"""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the front item of the queue. Returns None if empty. Time complexity: O(1)"""
        if not self.is_empty():
            return self.items.popleft()
        return None

    def peek(self):
        """Returns the front item of the queue without removing it. Returns None if empty. Time complexity: O(1)"""
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        """Returns the number of items in the queue. Time complexity: O(1)"""
        return len(self.items)

    def display(self):
        """Displays the queue content."""
        print(f"Queue (front to back): {list(self.items)}")


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Queue Demonstration ---")
    q = Queue()

    print(f"Is queue empty? {q.is_empty()}")

    print("\nEnqueuing elements 10, 20, 30:")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    print(f"Queue size: {q.size()}")

    print(f"\nPeek at front element: {q.peek()}")

    print(f"\nDequeuing an element: {q.dequeue()}")
    q.display()

    print(f"\nDequeuing another element: {q.dequeue()}")
    q.display()

    print(f"\nIs queue empty? {q.is_empty()}")

    print(f"\nDequeuing last element: {q.dequeue()}")
    print(f"Dequeuing from an empty queue: {q.dequeue()}")
    q.display()
    print(f"Is queue empty? {q.is_empty()}")
