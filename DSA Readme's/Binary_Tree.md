
# Binary Tree

A binary tree is a tree in which each node has at most two children, referred to as the left and right child.

## Properties:
- Every node has at most two children.
- The children are usually referred to as the left and right child.

## Visual Representation:
```
        10
       /   \  
      5     15
    / \      \   
   3   7      20
```

## Applications:
- **Expression Parsing**: Used in evaluating expressions (e.g., arithmetic expressions).
- **Decision Trees**: Used in machine learning for classification and regression tasks.
- **Binary Search**: Used for efficient searching.

## Code Snippet:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

# Traversing the binary tree (In-order Traversal)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

inorder_traversal(root)
```

### Explanation:
This code demonstrates the construction of a binary tree and traverses it in in-order, printing each node's value.

### When to Use:
- A binary tree is optimal when you need to efficiently search, insert, or delete elements, especially when the data is sorted.

### Interview Tip:
Binary trees are foundational in many interview questions. Make sure to practice traversals and understand their time complexity (O(n) for traversals).
