
# Tree Data Structure

A tree is a hierarchical data structure consisting of nodes connected by edges. It has a root node, from which all other nodes are descendants.

## Properties:
- A tree has a root node.
- Every node has zero or more child nodes.
- There are no cycles in a tree.

## Visual Representation:
```
          Root
       /         \  
    Child1      Child2
   /   \           \
Child3  Child4     Child5
```

## Applications:
- **File Systems**: Representing directories and files.
- **Hierarchical Data Representation**: In cases where there is a natural hierarchical structure, such as organizational charts.

## Code Snippet:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Example usage:
root = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")

root.add_child(child1)
root.add_child(child2)

# Traversing the tree
def traverse_tree(node):
    print(node.data)
    for child in node.children:
        traverse_tree(child)

traverse_tree(root)
```

### Explanation:
This example creates a simple tree with a root node and two child nodes. It uses a recursive function to traverse and print the tree nodes.

### When to Use:
- Use a tree when you need to represent hierarchical relationships like family trees, organizational charts, or document structures.

### Interview Tip:
Understanding trees and their traversal methods (like pre-order, in-order, and post-order) is essential for solving problems that involve hierarchical data.
