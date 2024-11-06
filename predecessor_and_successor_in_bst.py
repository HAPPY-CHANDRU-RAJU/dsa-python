"""
Predecessor And Successor In BST

You have been given a binary search tree of integers with ‘N’ nodes. You are also given 'KEY' which represents data of a node of this tree.

Your task is to return the predecessor and successor of the given node in the BST.

Note:
1. The predecessor of a node in BST is that node that will be visited just before the given node in the inorder traversal of the tree. If the given node is visited first in the inorder traversal, then its predecessor is NULL.
2. The successor of a node in BST is that node that will be visited immediately after the given node in the inorder traversal of the tree. If the given node is visited last in the inorder traversal, then its successor is NULL.
3. The node for which the predecessor and successor will not always be present. If not present, you can hypothetically assume it's position (Given that it is a BST) and accordingly find out the predecessor and successor.
4. A binary search tree (BST) is a binary tree data structure which has the following properties.
     • The left subtree of a node contains only nodes with data less than the node’s data.
     • The right subtree of a node contains only nodes with data greater than the node’s data.
     • Both the left and right subtrees must also be binary search trees.

Sample Input 1:
15 10 20 8 12 16 25 -1 -1 -1 -1 -1 -1 -1 -1
10

Sample output 1:
8 12

Explanation of Sample output 1:
The inorder traversal of this tree will be 8 10 12 15 16 20 25.
Since the node with data 8 is on the immediate left of the node with data 10 in the inorder traversal, the node with data 8 is the predecessor.
Since the node with data 12 is on the immediate right of the node with data 10 in the inorder traversal, the node with data 12 is the successor.

Sample Input 2:
10 5 -1 -1 -1
5

Sample output 2:
-1 10

Constraint :
1 <= N <= 10^4
1 <= data <= 10^7

Time Limit: 1 sec

LINK : https://www.naukri.com/code360/problems/_893049?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : 
    Space complexity    : 
"""
# Max of left tree
def findPredecessor(node):
    if not node:
        return
    while node.right:
        node = node.right
    return node.data

# Min of right tree
def findSuccessor(node):
    if not node:
        return
    while node.left:
        node = node.left
    return node.data

def predecessorSuccessor(root, key):
    pred=-1
    succ=-1
 
    curr=root
    while curr:
        if curr.data == key:
            if curr.left:
                pred=findPredecessor(curr.left)

            if curr.right:
                succ=findSuccessor(curr.right)
            break
        elif curr.data > key:
            succ=curr.data
            curr=curr.left
        else:
            pred=curr.data
            curr=curr.right

    return [pred,succ]
