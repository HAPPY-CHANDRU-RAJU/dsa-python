"""
BST to sorted DLL

You are provided with a Binary Search Tree (BST), all you have to do is to convert it into the sorted doubly linked list (DLL).

For Example:
Consider the above BST, it will be converted into the below sorted DLL.
Here, 20 is the head node and 80 is the tail node.


Sample Input 1:
2
50 30 70 20 40 60 80 -1 -1 -1 -1 -1 -1 -1 -1
-1

Sample Output 1:
20 30 40 50 60 70 80 -1
-1

Explanation Of Sample Input 1:
For the first test case, the explanation is given in the description. -1 represents the end of DLL.
In the second test case, there is no node in BST and so, there is also no node in DLL.

Sample Input 2:
2
0 -2 -1 -3 -1 -1 -1
1 -1 2 -1 3 -1 -1

Sample Output 2:
-3 -2 0 -1
1 2 3 -1

Explanation Of Sample Input 2:
In the first test case, the sorted DLL formed is [-3, -2, 0].
In the second test case, the sorted DLL formed is [1, 2, 3].

Constraints:
1 <= T <= 10
0 <= N <= 10^4
-10^5 <= DATA <= 10^5

Time Limit: 1sec

LINK : https://www.naukri.com/code360/problems/bst-to-sorted-dll_1263694?leftPanelTabValue=PROBLEM
"""

# DLL 
"""
    Time complexity     : (n)
    Space complexity    : (h)
"""
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bstToSortedDLL(root):
    head = None
    curr = None

    if not root:
        return None 
    
    def inorder_traversal(node):
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

# DLL with circular
"""
    Time complexity     : (n)
    Space complexity    : (h)
"""
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bstToSortedCircularDLL(root):
    head = None
    curr = None
    tail = None

    if not root:
        return None 
    
    def inorder_traversal(node):
        nonlocal head, curr, tail
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
        tail = curr  # Update the tail pointer

        inorder_traversal(node.right)

    inorder_traversal(root)
    
    # Make the DLL circular
    if head and tail:
        head.left = tail
        tail.right = head
    
    return head
