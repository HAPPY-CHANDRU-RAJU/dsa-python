"""
Top View Of Binary Tree

You are given a Binary Tree of 'n' nodes.

The Top view of the binary tree is the set of nodes visible when we see the tree from the top.
Find the top view of the given binary tree, from left to right.

Sample Input 1:
1 2 3 4 5 -1 6 -1 7 -1 -1 8 -1 9 -1 -1 11 10 -1 -1 -1 -1 -1

Sample Output 1:
10 4 2 1 3 6

Explanation of Sample Output 1:
The binary tree is:

Consider the vertical lines in the figure. The top view contains the topmost node from each vertical line.
In test case 1,


Sample Input 2:
1 2 3 4 5 6 7 8 9 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 2:
8 4 2 1 3 7

Explanation of Sample Output 2:
The binary tree is:

From left to right, the top view of the tree will be [8,4,2,1,3,7], where 9, 5 and 6 will be hidden when we see from the top of the tree.

Expected time complexity :
The expected time complexity is O(n * log(n)).

Constraints:
1 <= 'n' <= 10000
1 <= data in any node <= 10 ^ 6

Time limit: 1 sec

LINK : https://www.naukri.com/code360/problems/top-view-of-the-tree_799401?leftPanelTabValue=PROBLEM
"""

# Medium Effort
"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""
from os import *
from sys import *
from collections import *

class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
    result = {}
    queue = deque([(root, 0)])
    while queue:
        n = len(queue)
        for _ in range(n):
            curr, indx = queue.popleft()

            if indx not in result:
                result[indx] = curr.val

            if curr.left:
                queue.append((curr.left, indx-1))

            if curr.right:
                queue.append((curr.right, indx+1))
    
    sorted_result = dict(sorted(result.items(), key=lambda x: x[0] ))
    return sorted_result.values()



# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
from os import *
from sys import *
from collections import *

class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
    result = {}
    queue = deque([(root, 0)])

    min_hd, max_hd = 0, 0
    while queue:
        n = len(queue)
        for _ in range(n):
            curr, indx = queue.popleft()

            min_hd = min(min_hd, indx)
            max_hd = max(max_hd, indx)

            if indx not in result:
                result[indx] = curr.val

            if curr.left:
                queue.append((curr.left, indx-1))

            if curr.right:
                queue.append((curr.right, indx+1))
    
    sorted_result = [result[i] for i in range(min_hd, max_hd+1)]
    return sorted_result