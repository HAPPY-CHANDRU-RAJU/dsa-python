"""
Bottom View Of Binary Tree

You are given a 'Binary Tree'.
Return the bottom view of the binary tree.

Note :
1. A node will be in the bottom-view if it is the bottom-most node at its horizontal distance from the root. 
2. The horizontal distance of the root from itself is 0. The horizontal distance of the right child of the root node is 1 and the horizontal distance of the left child of the root node is -1. 
3. The horizontal distance of node 'n' from root = horizontal distance of its parent from root + 1, if node 'n' is the right child of its parent.
4. The horizontal distance of node 'n' from root = horizontal distance of its parent from the root - 1, if node 'n' is the left child of its parent.
5. If more than one node is at the same horizontal distance and is the bottom-most node for that horizontal distance, including the one which is more towards the right.

LINK : https://www.naukri.com/code360/problems/bottom-view-of-binary-tree_893110?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : O(N), where N is the number of nodes in the binary tree. 
                          This is because we visit every node exactly once during the traversal.

    Space complexity    : O(N), where N is the number of nodes in the binary tree.
                          This accounts for both the space used by the result dictionary (which stores nodes for each horizontal distance) and the recursive call stack during the BFS traversal.
"""

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    if not root:
        return []

    result = {}
    def bottomNodes(root, distance, level):
        if not root:
            return 
        
        if (distance not in result) or (result[distance][1] <= level):
            result[distance] = (root.data, level)

        bottomNodes(root.left, distance-1, level+1)
        bottomNodes(root.right, distance+1, level+1)
    
    bottomNodes(root, 0, 0)

    max_indx, min_indx = max(result), min(result)
    return [ result[i][0] for i in range(min_indx, max_indx+1)]
