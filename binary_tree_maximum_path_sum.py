"""
Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6

Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42

Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

LINK : https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

# Optimal
"""
    Time Complexity     : O(n)
    Space Complexity    : O(h), where h is the height of the tree (which is O(logn) for a balanced tree and O(n) for a skewed tree).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_val = -float('inf')
        def maxSum(node):
            nonlocal max_val

            if not node:
                return 0

            curr_val = node.val
            left_val = maxSum(node.left)
            right_val = maxSum(node.right)

            left_val = max(0, left_val) 
            right_val = max(0, right_val) 
            
            max_val = max(max_val, curr_val+left_val+right_val)
            return curr_val + max(left_val, right_val)

        maxSum(root)
        return max_val
