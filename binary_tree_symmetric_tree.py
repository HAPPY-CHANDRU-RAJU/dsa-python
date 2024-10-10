"""
Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 
Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 
Follow up: Could you solve it both recursively and iteratively?

LINK : https://leetcode.com/problems/symmetric-tree/description/?envType=problem-list-v2&envId=binary-tree
"""

# Medium Effort
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def symmetric(t1, t2):
            if not t1 and not t2:
                return True
            
            if not t1 or not t2:
                return False
            
            return (
                (t1.val == t2.val) 
                and symmetric(t1.right, t2.left)
                and symmetric(t2.right, t1.left)
            )

        return symmetric(root.left, root.right)

# Optimal
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root.right, root.left])
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()

            if not t1 and not t2:
                continue
            
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t2.left)
            queue.append(t1.right)
       
        return True