
# Breadth-First Search (BFS) in Tree and Graph

BFS is an algorithm for traversing or searching tree or graph data structures. It starts at the root node (for trees) and explores all neighbors at the present depth level before moving on to nodes at the next depth level.

## Visual Representation (Tree):
```
        10
       /   \     
     5     15
    / \      \    
   3   7      20
```

## Applications:
- **Shortest Path**: BFS can find the shortest path in an unweighted graph.
- **Level-order Traversal**: BFS is ideal for traversing a tree level by level.

## Code Snippet for Tree:

```python
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_tree(root):
    if root is None:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
bfs_tree(root)
```

### Explanation:
This code demonstrates BFS traversal in a binary tree. It uses a queue to explore nodes level by level.

### When to Use:
- BFS is optimal for finding the shortest path in an unweighted graph or performing level-order traversal in trees.

### Interview Tip:
BFS is commonly used in problems related to finding the shortest path in graphs. Ensure you understand how BFS works with both trees and graphs.
