"""
Two Sum IV - Input is a BST

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

LINK : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
"""

# Medium Effort
"""
    Time complexity     : O(n)
    Space complexity    : O(n)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        seen = set()
        def inorderTraversal(node):
            if not node:
                return 
            
            inorderTraversal(node.left)
            seen.add(node.val)
            inorderTraversal(node.right)
        
        inorderTraversal(root)
        
        for i in seen:
            if i != (k-i) and k-i in seen:
                return True
        return False

# Optimal
"""
    Time complexity     : O(n)
    Space complexity    : O(n)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # the Optimal approach is slightly more efficient in practice because 
        # it performs the pair check during the traversal, 
        # allowing for an early exit if a pair is found.
        if not root:
            return False
        
        seen = set()
        def find(node):
            if not node:
                return False
            
            if k - node.val in seen:
                return True

            seen.add(node.val)
            return find(node.left) or find(node.right)
        
        return find(root)