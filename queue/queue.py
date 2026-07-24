class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue. Time: O(1), Space: O(1)."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item. Time: O(1), Space: O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self):
        """Return the front item without removing it. Time: O(1), Space: O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def rear(self):
        """Return the rear item without removing it. Time: O(1), Space: O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]

    def is_empty(self):
        """Return True if the queue is empty. Time: O(1), Space: O(1)."""
        return len(self.items) == 0


# Example usage

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.front())
print(queue.rear())
print(queue.dequeue())
