"""
Path In A Tree

You are given a binary tree with ‘N’ number of nodes and a node ‘X’. Your task is to print the path from the root node to the given node ‘X’.
A binary tree is a hierarchical data structure in which each node has at most two children.

Sample Input 1 :
2
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
7
3 2 1 -1 -1 -1 -1
1

Sample output 1 :
1 3 7
3 1

Explanation For Sample Output 1: For the first test case, the tree will be: 
Here, for ‘X ’= 7, the output will be 1 3 7.

For the second test case, the tree will be: Here, for ‘X ’= 1, the output will be 3 1.

Sample Input 2 :
2
1 3 -1 -1 4 2 -1 -1 -1
1
4 -1 1 2 -1 -1 3 -1 -1
1

Sample output 2 :
1
4 1 

Constraints:
1 <= T <= 10
1 <= N <= 10000
1 <= X <= N
All the node values will be in a range from 1 to N.

Time limit: 1 sec.


LINK : https://www.naukri.com/code360/problems/path-in-a-tree_3843990?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class TreeNode:   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathInATree(root: TreeNode, x: int) -> List[int]:
    result = []

    def hasRootPath(root, result, x):
        if not root:
            return False
        
        result.append(root.data)

        if root.data == x:
            return True

        if hasRootPath(root.left, result, x) or hasRootPath(root.right, result, x):
            return True

        result.pop(-1)
        return False
    
    if hasRootPath(root, result, x):
        return result
    return []

############################ OR ########################  

class TreeNode:   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathInATree(root: TreeNode, x: int) -> List[int]:
    if not root:
        return []

    if root.data == x:
        return [root.data]

    left_path = pathInATree(root.left, x)
    if left_path:
        return [root.data] + left_path

    right_path = pathInATree(root.right, x)
    if right_path:
        return [root.data] + right_path

    return []
