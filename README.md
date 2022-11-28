# Data Structures and Algorithms
These are completed exercises as part of the Google Udacity course: Introduction to Data Structures and Algorithms in Python

## List-Based Collections (Queues.py, Stacks.py, Linked-List.py)
- Topic covered lists, arrays, Python lists, linked-lists, stacks and queues
- Push and pop runtime is O(1)
- Can be done with a simple Python list or using deque from collections module

## Searching and Sorting (BinarySearch.py, BubbleSort.py, QuickSort.py, Recursion.py)
- Topics covered binary search, recursion, bubble sort, merge sort, quick sort
- Binary search
	- Iterative binary search on a list
	- assumes data is sorted
	- O(log(n)) 
- Bubble Sort
		- O(n^2) runtime, because have to iterate through the list n times
		- Compares left and right elements, moving higher value to end of list
- Merge Sort
	- Divide and conquer algorithm
	- Recursively splits the list in half and then sorts the elements
	- O(nlog(n)) for all cases
- Quick Sort
	- Also divide and conquer, but uses a pivot
	- uses a partition function
	- Average case: O(nlog(n))

## Maps and Hashing (Dictionaries.py, Hashing.py, Hashing.ipynb)
- Topics covered sets, maps, dictionaries, hashing
- Created a python hash table to hash strings
- O(1) lookup time

## Trees (BinarySearchTree.ipynb)
- Topics covered binary search trees, heaps, and self-balancing trees
- Implemented  preorder search and print
- Search for BST is O(logn), the height of the tree
- Self balancing trees - Red-Black trees
- Explored Breadth First Search and Depth First Search
- Heaps are specific kind of tree - elements arranged in increasing or decreasing order

## Graphs (Graphs.ipynb)
- Topics covered graphs, understanding graph terms, coded representations, properties, traversals and paths
- Implemented BFS and DFS (traversal time is O(Vertices + Edges))
- Coded for adjacency list, matrix and edge list
