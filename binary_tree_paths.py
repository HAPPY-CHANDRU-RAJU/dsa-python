"""
Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

LINK : https://leetcode.com/problems/binary-tree-paths/description/
"""

"""
    Time complexity     : (n)
    Space complexity    : (n)
"""

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        result = []
        def get_path(node, path):
            path += str(node.val)

            if not node.left and not node.right:
                result.append(path)
            else:
                if node.left:
                    get_path(node.left, path+"->")
                if node.right:
                    get_path(node.right, path+"->")
                
        get_path(root, "")
        return result

