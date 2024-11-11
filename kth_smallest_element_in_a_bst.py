"""
Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
 
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

LINK : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Medium Effort
"""
    Time complexity     : O(N), where N is the number of nodes in the tree, since we perform an in-order traversal of all nodes.
    Space complexity    : O(N), due to storing the values of all nodes in the `sortedVal` list.
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        sortedVal = []
        def sortedValBST(node, sortedVal):
            if not node:
                return 
            
            sortedValBST(node.left, sortedVal)
            sortedVal.append(node.val)
            sortedValBST(node.right, sortedVal)

        sortedValBST(root, sortedVal)
        return sortedVal[k-1]

# Optimal
"""
    Time complexity     : O(H + k), where H is the height of the tree. This is because we may need to traverse up to `k` nodes along the in-order path, but the traversal stops early once we find the k-th smallest element.
    Space complexity    : O(H), where H is the height of the tree, due to the recursion stack. In the worst case (an unbalanced tree), this could be O(N), but in a balanced tree, it is O(log N).
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = -1

        def sortedValBST(node):
            if not node or self.result != -1:
                return 

            sortedValBST(node.left )
            self.count += 1
            if self.count == k:
                self.result = node.val
                return 

            sortedValBST(node.right)

        sortedValBST(root)
        return self.result