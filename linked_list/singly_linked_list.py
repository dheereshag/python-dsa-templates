class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning. Time: O(1), Space: O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end. Time: O(n), Space: O(1)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, data):
        """Delete the first node matching data. Time: O(n), Space: O(1)."""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next
        if current.next is not None:
            current.next = current.next.next

    def search(self, data):
        """Search for a node containing data. Time: O(n), Space: O(1)."""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def traverse(self):
        """Return a list of values in the linked list. Time: O(n), Space: O(n)."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values


# Example usage

linked_list = SinglyLinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_end(20)
linked_list.insert_at_beginning(5)
print(linked_list.traverse())
print(linked_list.search(20))
linked_list.delete(10)
print(linked_list.traverse())
