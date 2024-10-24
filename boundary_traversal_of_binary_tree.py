"""
Boundary Traversal of Binary Tree

You are given a binary tree having 'n' nodes.
The boundary nodes of a binary tree include the nodes from the left and right boundaries and the leaf nodes, each node considered once.
Figure out the boundary nodes of this binary tree in an Anti-Clockwise direction starting from the root node.

Sample Input 1:
10 5 20 3 8 18 25 -1 -1 7 -1 -1 -1 -1 -1 -1 -1

Sample Output 1:
10 5 3 7 18 25 20

Explanation of Sample Input 1:
The nodes on the left boundary are [10, 5, 3]
The nodes on the right boundary are [10, 20, 25]
The leaf nodes are [3, 7, 18, 25].
Please note that nodes 3 and 25 appear in two places but are considered once.


Sample Input 2:
100 50 150 25 75 140 200 -1 30 70 80 -1 -1 -1 -1 -1 35 -1 -1 -1 -1 -1 -1

Sample Output 2:
100 50 25 30 35 70 80 140 200 150

Constraints:
1 <= n <= 10000

Where 'n' is the total number of nodes in the binary tree.

Time Limit: 1 sec

LINK : https://www.naukri.com/code360/problems/boundary-traversal-of-binary-tree_790725?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from collections import deque

def leftBoundary(node, boundary):
    if node:
        if node.left:
            boundary.append(node.data)
            leftBoundary(node.left, boundary)
        elif node.right:
            boundary.append(node.data)
            leftBoundary(node.right, boundary)
    
def rightBoundary(node, boundary):
    if node:
        if node.right:
            rightBoundary(node.right, boundary)
            boundary.append(node.data)
        elif node.left:
            rightBoundary(node.left, boundary)
            boundary.append(node.data)

def leaveBoundary(node, boundary):
    if node:
        leaveBoundary(node.left, boundary)   
        if not node.left and not node.right:
            boundary.append(node.data)
        leaveBoundary(node.right, boundary)

# Functions to traverse on each part.
def traverseBoundary(root):
    if not root:
        return []

    boundary = []
    boundary.append(root.data)
    leftBoundary(root.left, boundary)

    leaveBoundary(root.left, boundary)
    leaveBoundary(root.right, boundary)

    right_boundary = []
    rightBoundary(root.right, right_boundary)

    boundary.extend(right_boundary)

    return boundary




