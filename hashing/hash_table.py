class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table. Time: O(1) average, Space: O(1)."""
        position = self._hash(key)
        for index, (existing_key, _) in enumerate(self.table[position]):
            if existing_key == key:
                self.table[position][index] = (key, value)
                return
        self.table[position].append((key, value))

    def delete(self, key):
        """Delete a key from the hash table. Time: O(1) average, Space: O(1)."""
        position = self._hash(key)
        for index, (existing_key, _) in enumerate(self.table[position]):
            if existing_key == key:
                del self.table[position][index]
                return

    def search(self, key):
        """Search for a value by key. Time: O(1) average, Space: O(1)."""
        position = self._hash(key)
        for existing_key, value in self.table[position]:
            if existing_key == key:
                return value
        return None


# Example usage

hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 25)
print(hash_table.search("name"))
hash_table.delete("age")
print(hash_table.search("age"))
