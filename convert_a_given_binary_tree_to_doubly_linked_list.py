"""
Convert A Given Binary Tree To Doubly Linked List

Given a Binary Tree, convert this binary tree to a Doubly Linked List.

A Binary Tree (BT) is a data structure in which each node has at most two children.
A Doubly Linked List contains a previous pointer, along with the next pointer and data.
The order of nodes in Doubly Linked List must be the same as Inorder of the given Binary Tree.
The doubly linked list should be returned by taking the next pointer as right and the previous pointer as left.
You need to return the head of the Doubly Linked List.

Note :
You are not required to print the expected output, and it has already been taken care of. Just implement the function.

Sample Input 1 :
2
3 1 5 -1 2 -1 -1 -1 -1
9 6 10 4 7 -1 11 -1 -1 -1 -1 -1 -1

Sample Output 1 :
1 2 3 5 
4 6 7 9 10 11

Explanation of Input 1 :
Here we have 2 test cases; hence there are 2 binary trees.

Test Case 1 : 
We can see that the inorder traversal of the given tree is: 1 2 3 5.

Test Case 2 : 
We can see that the inorder traversal of the given tree is: 4 6 7 9 10 11.

Sample Input 2 :
2
4 6 -1 5 -2 -1 -1 -1 -1
1 2 3 4 4 -1 4 -1 -1 -1 -1 -1 -1

Sample Output 2 :
5 6 -2 4 
4 2 4 1 3 4

Constraints :
1 <= T <= 100
0 <= N <= 3000
-10 ^ 6 <= data <= 10 ^ 6 and data != -1

where 'N' is the number of nodes in the tree, 'T' represents the number of test cases and "data" denotes data contained in the node of the binary tree.
Duplicate elements can be in the right subtree or left subtree.

Time Limit: 1 sec.

LINK : https://www.naukri.com/code360/problems/convert-a-given-binary-tree-to-doubly-linked-list_893106
"""

# Binary Tree - Inorder Traversal
"""
    Time complexity     : (n)
    Space complexity    : (h)
"""
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def BTtoDLL(root):
    head = None
    curr = None

    if not root:
        return None  

    def inorder_traversal(node):
        """
        Perform in-order traversal of the binary tree
        and construct the doubly linked list.
        """
        nonlocal head, curr
        if not node:
            return

        inorder_traversal(node.left)

        if not head:
            head = DLLNode(node.data)
            curr = head
        else:
            temp = DLLNode(node.data)
            curr.right = temp
            temp.left = curr
            curr = temp  

        inorder_traversal(node.right)

    inorder_traversal(root)
    return head
