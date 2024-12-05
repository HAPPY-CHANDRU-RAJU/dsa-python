
# 12 Essential Design Patterns for Solving DSA Problems

## 1. Sliding Window Pattern
**Use Case**: Problems involving subarrays or substrings with specific properties (sum, length, unique characters).  
**Example**: Maximum sum of subarray of size `k`, Longest substring without repeating characters.  
**Explanation**: Use a window (subset of the array) that moves along the input. Adjust window size dynamically.  
**Time Complexity**: O(n)  
**Space Complexity**: O(1)

---

## 2. Two Pointers Pattern
**Use Case**: Finding pairs or triplets in sorted arrays or lists.  
**Example**: Pair with target sum, 3Sum problem, Container with most water.  
**Explanation**: Use two pointers, one starting from the beginning and one from the end, and move them towards each other.  
**Time Complexity**: O(n)  
**Space Complexity**: O(1)

---

## 3. Fast and Slow Pointers (Tortoise and Hare)
**Use Case**: Detecting cycles in linked lists or arrays.  
**Example**: Detect a cycle in a linked list, Find the middle of a linked list.  
**Explanation**: Use two pointers that move at different speeds to find intersections.  
**Time Complexity**: O(n)  
**Space Complexity**: O(1)

---

## 4. Merge Intervals Pattern
**Use Case**: Problems involving overlapping intervals.  
**Example**: Merge overlapping intervals, Insert an interval into a sorted list.  
**Explanation**: Sort intervals by start time and merge overlapping intervals.  
**Time Complexity**: O(n log n)  
**Space Complexity**: O(n)

---

## 5. Cyclic Sort Pattern
**Use Case**: Sorting problems with a known range of numbers.  
**Example**: Find missing number, Find all duplicates in an array.  
**Explanation**: Place elements at their correct indices in the array.  
**Time Complexity**: O(n)  
**Space Complexity**: O(1)

---

## 6. In-place Reversal of Linked List
**Use Case**: Reversing sub-parts of a linked list.  
**Example**: Reverse a linked list, Reverse nodes in k-group.  
**Explanation**: Use a pointer to reverse links one node at a time.  
**Time Complexity**: O(n)  
**Space Complexity**: O(1)

---

## 7. Two Heaps Pattern
**Use Case**: Finding the median or k-th largest/smallest element.  
**Example**: Median of a stream, Kth largest element in a stream.  
**Explanation**: Use a max-heap and min-heap to maintain balance.  
**Time Complexity**: O(log n) per insertion  
**Space Complexity**: O(n)

---

## 8. Breadth-First Search (BFS)
**Use Case**: Shortest path in unweighted graphs, level-order traversal in trees.  
**Example**: Level order traversal, Shortest path in a maze.  
**Explanation**: Use a queue to explore nodes level by level.  
**Time Complexity**: O(V + E)  
**Space Complexity**: O(V)

---

## 9. Depth-First Search (DFS)
**Use Case**: Traversing or searching tree/graph structures.  
**Example**: All paths in a graph, Check if a graph is connected.  
**Explanation**: Use recursion or a stack to explore nodes deeply.  
**Time Complexity**: O(V + E)  
**Space Complexity**: O(V)

---

## 10. Backtracking
**Use Case**: Exploring all possibilities and undoing decisions when necessary.  
**Example**: N-Queens problem, Sudoku solver, Subsets and permutations.  
**Explanation**: Use recursion to explore and backtrack when a path is invalid.  
**Time Complexity**: O(2^n) in worst case  
**Space Complexity**: O(n)

---

## 11. Dynamic Programming (DP)
**Use Case**: Problems with overlapping subproblems and optimal substructure.  
**Example**: Fibonacci series, 0/1 Knapsack, Longest common subsequence.  
**Explanation**: Break the problem into subproblems and store their solutions.  
**Time Complexity**: O(n^2) for most problems  
**Space Complexity**: O(n)

---

## 12. Binary Search Pattern
**Use Case**: Searching in sorted data structures or optimization problems.  
**Example**: Binary search in a sorted array, Find the peak element, Search in rotated sorted array.  
**Explanation**: Repeatedly divide the search space in half.  
**Time Complexity**: O(log n)  
**Space Complexity**: O(1)

---
