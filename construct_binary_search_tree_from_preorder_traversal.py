"""
Construct Binary Search Tree from Preorder Traversal

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

Example 1:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Example 2:
Input: preorder = [1,3]
Output: [1,null,3]
 
Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 1000
All the values of preorder are unique.

LINK : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
"""

# Medium Effort
"""
    Time complexity     : O(n) (Best/Average), O(n^2) (Worst)
    Space complexity    : O(log n) (Best/Average), O(n) (Worst)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def construct_bst(self, preorder, start, end):
        if start > end:
            return 
        
        root = TreeNode(preorder[start])

        index = start + 1
        while index <= end and preorder[index] < root.val:
            index += 1
        
        root.left = self.construct_bst(preorder, start+1, index -1)
        root.right = self.construct_bst(preorder, index, end)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.construct_bst(preorder, 0, len(preorder)-1)

# Optimal
"""
    Time complexity     : O(n) (Best/Average), O(n^2) (Worst)
    Space complexity    : O(n) (for the stack), O(log n) (for balanced tree)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return 
        
        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            node = TreeNode(value)

            if value < stack[-1].val :
                stack[-1].left = node
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = node
            
            stack.append(node)
        return root
