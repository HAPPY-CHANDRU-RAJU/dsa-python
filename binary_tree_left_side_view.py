"""
Left View Of Binary Tree

You have been given a Binary Tree of 'n' nodes, where the nodes have integer values
Print the left view of the binary tree.

Sample Input 1 :
2 35 10 2 3 5 2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 1 :
2 35 2

Explanation of Sample Input 1 :
The test case is explained in the problem statement.


Sample Input 2 :
1 2 3 4 5 -1 7 -1 -1 -1 -1 -1 -1 

Sample Output 2 :
1 2 4

Explanation of Sample Input 2 :
The Tree looks as follows:
            1
          /   \
         2     3
       /   \     \
      4     5     7

Expected time complexity:
The expected time complexity is O(n).

Constraints :
0 <= 'n' <= 10^5
1 <= 'data' <= 10^5

Where ‘n’ is the total number of nodes in the binary tree, and 'data' is the value of the binary tree node.

Time limit: 1sec

LINK : https://www.naukri.com/code360/problems/left-view-of-binary-tree_625707?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
from collections import deque

# Following is the structure of Tree Node:
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def leftView(root: BinaryTreeNode) -> None:
    if not root:
        return 

    queue = deque([root])
    while queue:
        n = len(queue)
        i = 0
        for _ in range(n):
            curr = queue.popleft()
            if i == 0:
                print(curr.data, end=" ")
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
            
            i += 1
    return 
