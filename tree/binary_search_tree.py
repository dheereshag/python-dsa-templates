class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST. Time: O(h), Space: O(1)."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if current is None:
            return Node(key)
        if key < current.key:
            current.left = self._insert_recursive(current.left, key)
        elif key > current.key:
            current.right = self._insert_recursive(current.right, key)
        return current

    def search(self, key):
        """Search for a key in the BST. Time: O(h), Space: O(1)."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

    def delete(self, key):
        """Delete a key from the BST. Time: O(h), Space: O(1)."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        if current is None:
            return None
        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            successor = self._min_node(current.right)
            current.key = successor.key
            current.right = self._delete_recursive(current.right, successor.key)
        return current

    def _min_node(self, current):
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Return keys in inorder order. Time: O(n), Space: O(h)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current is None:
            return
        self._inorder(current.left, result)
        result.append(current.key)
        self._inorder(current.right, result)

    def preorder_traversal(self):
        """Return keys in preorder order. Time: O(n), Space: O(h)."""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, current, result):
        if current is None:
            return
        result.append(current.key)
        self._preorder(current.left, result)
        self._preorder(current.right, result)

    def postorder_traversal(self):
        """Return keys in postorder order. Time: O(n), Space: O(h)."""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, current, result):
        if current is None:
            return
        self._postorder(current.left, result)
        self._postorder(current.right, result)
        result.append(current.key)


# Example usage

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
print(bst.inorder_traversal())
print(bst.search(30).key)
bst.delete(20)
print(bst.inorder_traversal())
