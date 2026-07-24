class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning. Time: O(1), Space: O(1)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end. Time: O(n), Space: O(1)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def delete(self, data):
        """Delete the first node matching data. Time: O(n), Space: O(1)."""
        if self.head is None:
            return
        if self.head.data == data and self.head.next == self.head:
            self.head = None
            return
        current = self.head
        previous = None
        while current.next != self.head and current.data != data:
            previous = current
            current = current.next
        if current.data == data:
            if previous is None:
                last_node = self.head
                while last_node.next != self.head:
                    last_node = last_node.next
                self.head = self.head.next
                last_node.next = self.head
            else:
                previous.next = current.next

    def search(self, data):
        """Search for a node containing data. Time: O(n), Space: O(1)."""
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def traverse(self):
        """Return a list of values in the linked list. Time: O(n), Space: O(n)."""
        if self.head is None:
            return []
        values = []
        current = self.head
        while True:
            values.append(current.data)
            current = current.next
            if current == self.head:
                break
        return values


# Example usage

linked_list = CircularLinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_end(20)
linked_list.insert_at_beginning(5)
print(linked_list.traverse())
print(linked_list.search(20))
linked_list.delete(10)
print(linked_list.traverse())
