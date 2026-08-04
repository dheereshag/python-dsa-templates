class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the stack. Time: O(1), Space: O(1)."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item. Time: O(1), Space: O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it. Time: O(1), Space: O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty. Time: O(1), Space: O(1)."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack. Time: O(1), Space: O(1)."""
        return len(self.items)


# Example usage

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())
print(stack.pop())
print(stack.size())
