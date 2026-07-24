class Deque:
    def __init__(self):
        self.items = []

    def insert_front(self, item):
        """Insert an item at the front. Time: O(1), Space: O(1)."""
        self.items.insert(0, item)

    def insert_rear(self, item):
        """Insert an item at the rear. Time: O(1), Space: O(1)."""
        self.items.append(item)

    def delete_front(self):
        """Remove and return the front item. Time: O(1), Space: O(1)."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)

    def delete_rear(self):
        """Remove and return the rear item. Time: O(1), Space: O(1)."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def is_empty(self):
        """Return True if the deque is empty. Time: O(1), Space: O(1)."""
        return len(self.items) == 0


# Example usage

deque = Deque()
deque.insert_front(10)
deque.insert_rear(20)
print(deque.delete_front())
print(deque.delete_rear())
