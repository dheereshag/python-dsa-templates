class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the AVL tree. Time: O(log n), Space: O(log n)."""
        self.root = self._insert(self.root, key)

    def _insert(self, current, key):
        if current is None:
            return Node(key)
        if key < current.key:
            current.left = self._insert(current.left, key)
        else:
            current.right = self._insert(current.right, key)
        current.height = 1 + max(self._height(current.left), self._height(current.right))
        balance = self._balance(current)
        if balance > 1:
            if key < current.left.key:
                return self._right_rotate(current)
            return self._left_right_rotate(current)
        if balance < -1:
            if key > current.right.key:
                return self._left_rotate(current)
            return self._right_left_rotate(current)
        return current

    def delete(self, key):
        """Delete a key from the AVL tree. Time: O(log n), Space: O(log n)."""
        self.root = self._delete(self.root, key)

    def _delete(self, current, key):
        if current is None:
            return None
        if key < current.key:
            current.left = self._delete(current.left, key)
        elif key > current.key:
            current.right = self._delete(current.right, key)
        else:
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            successor = self._min_node(current.right)
            current.key = successor.key
            current.right = self._delete(current.right, successor.key)

        if current is None:
            return None
        current.height = 1 + max(self._height(current.left), self._height(current.right))
        balance = self._balance(current)
        if balance > 1:
            if self._balance(current.left) >= 0:
                return self._right_rotate(current)
            return self._left_right_rotate(current)
        if balance < -1:
            if self._balance(current.right) <= 0:
                return self._left_rotate(current)
            return self._right_left_rotate(current)
        return current

    def search(self, key):
        """Search for a key in the AVL tree. Time: O(log n), Space: O(1)."""
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def _height(self, node):
        return node.height if node is not None else 0

    def _balance(self, node):
        return self._height(node.left) - self._height(node.right) if node is not None else 0

    def _min_node(self, current):
        while current.left is not None:
            current = current.left
        return current

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        right_child.height = 1 + max(self._height(right_child.left), self._height(right_child.right))
        return right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        left_child.height = 1 + max(self._height(left_child.left), self._height(left_child.right))
        return left_child

    def _left_right_rotate(self, node):
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _right_left_rotate(self, node):
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)


# Example usage

avl = AVLTree()
for value in [10, 20, 30, 40, 50]:
    avl.insert(value)
print(avl.search(30).key)
avl.delete(20)
print(avl.search(20))
