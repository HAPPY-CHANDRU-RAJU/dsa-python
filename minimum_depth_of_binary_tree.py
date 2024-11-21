"""
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

LINK : https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
"""

# Brute Force
"""
    Time complexity   : O(n)
                        Every node is visited once, resulting in a total time complexity of  O(n), where n is the number of nodes in the tree.

    Space complexity  : O(h)
                        The recursion stack depends on the height of the tree:
                            Balanced tree: O(log n)
                            Skewed tree: O(n)
"""
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Optimal
"""
    Time complexity   : O(n)
                        Every node is visited once, resulting in a total time complexity of  O(n), where n is the number of nodes in the tree.

    Space complexity  : O(n)
                        The space is determined by the maximum number of nodes in the queue at any given level:
                        In the worst case (a complete binary tree), the last level can have O(n) nodes.
                        Therefore, the space complexity is O(n).
"""
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        level = 0

        while queue:
            level += 1
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                if not node.right and not node.left:
                    return level
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return level
