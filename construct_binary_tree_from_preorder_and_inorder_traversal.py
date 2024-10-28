"""
Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

LINK : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""

# Medium 
"""
    Time complexity     : (n^2)
    Space complexity    : (n^2) 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_value = preorder.pop(0)
        root = TreeNode(root_value)

        root_index = inorder.index(root_value)

        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index+1:])

        return root


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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left, right):
            if left > right:
                return

            root_value = preorder.pop(0)
            root = TreeNode(root_value)

            root_index = inorder_map[root_value]

            root.left = array_to_tree(left, root_index-1)
            root.right = array_to_tree(root_index+1, right)
            
            return root

        inorder_map = { i:indx for indx, i in enumerate(inorder)}
        return array_to_tree(0, len(inorder_map)-1)