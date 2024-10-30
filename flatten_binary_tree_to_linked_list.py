"""
Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":
    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.
    

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?

LINK : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

# Recursive Solution
"""
    Time complexity     : O(n)
    Space complexity    : O(h)
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        # Flatten left subtree
        self.flatten(root.left)
        if root.left:
            # Find the rightmost node of the left subtree
            temp = root.left
            while temp.right:
                temp = temp.right
                
            # Attach original right subtree to the end of flattened left subtree
            temp.right = root.right
            root.right = root.left
            root.left = None
        
        # Flatten right subtree
        self.flatten(root.right)


# Iterative Solution (Optimal)
"""
    Time complexity     : O(n)
    Space complexity    : O(1)
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 

        node = root
        while node:
            if node.left:
                # Find the rightmost node in the left subtree
                temp = node.left
                while temp.right:
                    temp = temp.right

                # Attach right subtree to the rightmost node of the left subtree
                temp.right = node.right
                node.right = node.left
                node.left = None
            # Move to the next right node
            node = node.right
