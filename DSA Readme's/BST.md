
# Binary Search Tree (BST)

A Binary Search Tree is a binary tree in which each node follows the property:
- The value of the left child is less than the node’s value.
- The value of the right child is greater than the node’s value.

## Visual Representation:
```
        10
       /       5     15
    / \         3   7     20
```

## Applications:
- **Searching**: Efficient searching of sorted data.
- **Sorting**: Can be used for sorting elements via in-order traversal.
- **Range Queries**: Optimized for finding all values within a given range.

## Code Snippet:

```python
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

# Example usage:
root = BSTNode(10)
root.insert(5)
root.insert(15)
root.insert(7)

# In-order traversal
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

inorder_traversal(root)
```

### Explanation:
This code defines a BST and inserts nodes while maintaining the BST properties. It then performs an in-order traversal to print the tree's values in sorted order.

### When to Use:
- Use a BST when you need fast lookup, insertion, and deletion in a sorted manner. The time complexity of these operations is O(log n) if the tree is balanced.

### Interview Tip:
In BST-related problems, ensure the tree is balanced to achieve optimal performance. Unbalanced trees may degrade to a linked list (O(n)).
