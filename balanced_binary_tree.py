"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 
Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104

LINK : https://leetcode.com/problems/balanced-binary-tree/description/
"""

"""
    Time complexity     : (n)
    Space complexity    : (n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        
        leftSide = self.height(root.left)
        rightSide = self.height(root.right)

        if leftSide < 0 or rightSide < 0 or abs(leftSide - rightSide) > 1:
            return -1
        return max(leftSide, rightSide)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0