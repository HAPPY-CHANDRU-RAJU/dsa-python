"""
Tree Traversals

You have been given a Binary Tree of 'N' nodes, where the nodes have integer values.
Your task is to return the ln-Order, Pre-Order, and Post-Order traversals of the given binary tree.

For example :
For the given binary tree:
<Image />
The Inorder traversal will be [5, 3, 2, 1, 7, 4, 6].
The Preorder traversal will be [1, 3, 5, 2, 4, 7, 6].
The Postorder traversal will be [5, 2, 3, 7, 6, 4, 1].


Sample Input 1 :
1 2 3 -1 -1 -1  6 -1 -1
Sample Output 1 :
2 1 3 6 
1 2 3 6 
2 6 3 1
Explanation of Sample Output 1 :
 The given binary tree is shown below:

Inorder traversal of given tree = [2, 1, 3, 6]
Preorder traversal of given tree = [1, 2, 3, 6]
Postorder traversal of given tree = [2, 6, 3, 1]


Sample Input 2 :
1 2 4 5 3 -1 -1 -1 -1 -1 -1

Sample Output 2 :
5 2 3 1 4 
1 2 5 3 4 
5 3 2 4 1

Explanation of Sample Output 2 :
The given binary tree is shown below:

Inorder traversal of given tree = [5, 2, 3, 1, 4]
Preorder traversal of given tree = [1, 2, 5, 3, 4]
Postorder traversal of given tree = [5, 3, 2, 4, 1]


Constraints :

1 <= 'N' <= 10^5
0 <= 'data' <= 10^5     

where 'N' is the number of nodes and 'data' denotes the node value of the binary tree nodes.
Time limit: 1 sec

LINK : https://www.naukri.com/code360/problems/tree-traversal_981269?leftPanelTabValue=SUBMISSION
"""

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    """
        Intuition:
            1. A stack is used to store the nodes along with their current state (0 for Preorder, 1 for Inorder, and 2 for Postorder).
            2. Depending on the current state of the node:
                > Preorder: Append the node's value to the preorder list and push the node back onto the stack with state 1 to process Inorder later. Push the left child onto the stack if it exists.
                > Inorder: Append the node's value to the inorder list and push the node back onto the stack with state 2 to process Postorder later. Push the right child onto the stack if it exists.
                > Postorder: Append the node's value to the postorder list.
    """
    if not root:
        return [], [], []
    

    stack = [[root, 0]]
    preorder, inorder, postorder = [], [], []

    while stack:
        node, state = stack.pop()

        if state == 0:
            # Preorder
            preorder.append(node.data)
            stack.append([node, state+1])
            if node.left:
                stack.append([node.left, 0])
        elif state == 1:
            # Inorder
            inorder.append(node.data)
            stack.append([node, state+1])
            if node.right:
                stack.append([node.right, 0])
        else:
            # Postorder
            postorder.append(node.data)

    return inorder, preorder, postorder

        