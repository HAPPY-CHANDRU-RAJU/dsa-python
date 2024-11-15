"""
Maximum Sum BST in Binary Tree

Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20

Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:
Input: root = [4,3,null,1,2]
Output: 2

Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:
Input: root = [-4,-2,-5]
Output: 0

Explanation: All values are negatives. Return an empty BST.
 

Constraints:

The number of nodes in the tree is in the range [1, 4 * 104].
-4 * 104 <= Node.val <= 4 * 104

LINK : https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
"""

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (h)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def postorder(node):
            nonlocal max_sum
            if not node:
                return True, 0, float('inf'), -float('inf') # is_bst, sum, max, min

            isleft_bst, left_sum, left_min, left_max = postorder(node.left)
            isright_bst, right_sum, right_min, right_max = postorder(node.right)

            if isleft_bst and isright_bst and left_max < node.val < right_min:
                sub_tree_sum = left_sum + right_sum + node.val
                max_sum = max(max_sum, sub_tree_sum)
                print(max_sum)
                return True, sub_tree_sum, min(left_min, node.val), max(right_max, node.val)
            return False, 0, 0, 0

        postorder(root)
        return max_sum