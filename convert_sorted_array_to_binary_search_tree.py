"""
Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.


Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]

Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

LINK : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
"""

# Medium 
"""
    Time complexity     : O(n)
    Space complexity    : O(log n) for the recursion stack in a balanced tree
                          O(n) for the space used by the BST itself
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 
        
        def convertBST(left, right):
            if left > right:
                return 
            
            mid = (left+right) // 2
            root = TreeNode(nums[mid])

            root.left = convertBST(left, mid-1)
            root.right = convertBST(mid+1, right)
        
            return root
        return convertBST(0, len(nums)-1)

# Optimal
"""
    Time complexity     : O(n)
    Space complexity    : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid]) 
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root