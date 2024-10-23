"""
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5

Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.


LINK : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""

# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def __init__(self):
        self.result = [[], []]

    def hasPathToRoot(self, node, x, indx):
        if not node:
            return False
        
        self.result[indx].append(node.val)
        if node.val == x.val:
            return True
        
        if self.hasPathToRoot(node.left, x, indx) or self.hasPathToRoot(node.right, x, indx):
            return True
        
        self.result[indx].pop(-1)
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.hasPathToRoot(root, p, 0)
        self.hasPathToRoot(root, q, 1)
        
        res = -1
        for ind in range(len(min(self.result))):
            if self.result[0][ind] ==  self.result[1][ind]:
                res = self.result[1][ind]
            else:
                break

        return TreeNode(res)


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""

class Solution:
    """
    This recursive LCA approach (first solution) is more efficient in terms of simplicity and avoids the overhead of explicitly 
    constructing and comparing paths. This method directly finds the LCA without needing to store paths or manage extra lists.
    """
    def lca(self, node, x, y):
        if not node:
            return None
        
        if node == x:
            return x

        if node == y:
            return y

        left_result = self.lca(node.left, x, y)
        right_result = self.lca(node.right, x, y)

        if left_result and right_result:
            return node
        elif not left_result and not right_result:
            return None

        return left_result or right_result

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = self.lca(root, p, q)
        return result