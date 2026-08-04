# Python DSA Templates

A compact collection of Python implementations for common data structures and algorithms.

## What is included

- Binary search
- Sorting algorithms:
  - Bubble sort
  - Bucket sort
  - Counting sort
  - Heap sort
  - Insertion sort
  - Merge sort
  - Quick sort
  - Radix sort
  - Selection sort
- Graph algorithms:
  - Bellman-Ford
  - Dijkstra
  - Kruskal's algorithm
  - Prim's algorithm
  - Undirected cycle detection
  - BFS
  - DFS
- Tree implementations:
  - Binary search tree
  - AVL tree
- Linked list implementations:
  - Singly linked list
  - Doubly linked list
  - Circular linked list
- Stack and queue implementations:
  - Stack
  - Queue
  - Deque
- Hashing:
  - Hash table
- Heap implementations:
  - Min heap
  - Max heap

## Repository layout

- `binary_search.py` - binary search implementation
- `sort/` - sorting algorithm implementations
- `graph/` - graph algorithm implementations
- `tree/` - tree algorithm implementations
- `linked_list/` - linked list implementations
- `stack/` - stack implementation
- `queue/` - queue and deque implementations
- `hashing/` - hash table implementation
- `heap/` - heap implementations

## Example usage

Binary search:

```python
from binary_search import binary_search

arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 5))  # 2
```

Quick sort:

```python
from sort.quick_sort import quick_sort

arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
```

## Contributing

Contributions are welcome. If you would like to improve this repository, you can:

- add missing algorithms or variants
- improve existing implementations
- add tests and examples
- improve documentation

Please keep changes focused, readable, and consistent with the existing style of the project.
