"""
Morris Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

LINK : https://leetcode.com/problems/binary-tree-preorder-traversal/description/
"""

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = curr
                    result.append(curr.val)
                    curr = curr.left
                else:
                    predecessor.right = None
                    curr = curr.right
        return result