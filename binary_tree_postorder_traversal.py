"""
Binary Tree Postorder Traversal
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

 
Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

LINK : https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

# Medium 
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
    def postorder(self, node, res):
        if not node:
            return 
            
        self.postorder(node.left, res)
        self.postorder(node.right, res)
        res.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorder(root, res)
        return res

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n) (worst case) or (log n) (average case for a balanced tree)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = []
        last_visited_node = None
        curr  = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peer_node = stack[-1]
                if peer_node.right and last_visited_node != peer_node.right:
                    curr = peer_node.right
                else:
                    result.append(peer_node.val)
                    last_visited_node = stack.pop()

        return result