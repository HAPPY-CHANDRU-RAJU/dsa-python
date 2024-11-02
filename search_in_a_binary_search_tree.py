"""
Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: [] 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107

LINK : https://leetcode.com/problems/search-in-a-binary-search-tree/description/
"""

# Brute Force
"""
    Time complexity     : O(h)  where h is the height of the tree.
                           - O(log n) in the average case for balanced trees.
                           - O(n) in the worst case for unbalanced trees (degenerate).
    Space complexity    : O(h) due to the recursive call stack.
                           - O(log n) in the average case.
                           - O(n) in the worst case.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)


# Optimal
"""
    Time complexity     : O(h), where h is the height of the tree.
                           - O(log n) for balanced trees.
                           - O(n) for unbalanced trees (degenerate).
    Space complexity    : O(1), since no extra stack space is used for recursion.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            root = root.left if root.val > val else root.right
        return None
