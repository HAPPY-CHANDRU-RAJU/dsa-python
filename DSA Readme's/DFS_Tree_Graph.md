
# Depth-First Search (DFS) in Tree and Graph

DFS is an algorithm for traversing or searching tree or graph data structures. It starts at the root (or an arbitrary node in the case of a graph) and explores as far as possible along each branch before backtracking.

## Visual Representation (Tree):
```
        10
       /       5     15
    / \         3   7     20
```

## Applications:
- **Topological Sorting**: Used in directed acyclic graphs (DAG) for topological sorting.
- **Cycle Detection**: Used to detect cycles in graphs.
- **Path Finding**: DFS can be used for pathfinding problems.

## Code Snippet for Tree:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_tree(node):
    if node:
        print(node.value, end=" ")
        dfs_tree(node.left)
        dfs_tree(node.right)

# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
dfs_tree(root)
```

### Explanation:
This code demonstrates DFS traversal in a binary tree, where it first explores the left subtree, then the right subtree.

### When to Use:
- DFS is optimal when you need to explore all nodes along a path before backtracking. It is used in problems like solving mazes, topological sorting, and detecting cycles.

### Interview Tip:
DFS is often used in problems that require exploring all possibilities, such as pathfinding or tree/graph traversal problems.
