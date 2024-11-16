"""
Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

LINK : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

# Optimal
"""
    Time complexity     : O(n)
        - Serialization: Each node is visited once during BFS traversal.
        - Deserialization: Each node and placeholder is processed once.
        - Overall: Proportional to the number of nodes in the tree (n).

    Space complexity    : O(n)
        - Serialization: A queue is used for BFS traversal, and a result list stores serialized values.
        - Deserialization: A queue is used for BFS reconstruction, and a data list stores the input values.
        - Overall: Dominated by the larger of the queue or the list sizes, which scale with the number of nodes.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        result = []
        stack = deque([root])
        while stack:
            node = stack.popleft()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                result.append("#")
        return ",".join(map(str, result))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = deque([root])

        indx = 1
        while queue:
            node = queue.popleft()

            if indx < len(data) and data[indx] != '#':
                node.left = TreeNode(int(data[indx]))
                queue.append(node.left)
            indx += 1

            if indx < len(data) and data[indx] != '#':
                node.right = TreeNode(int(data[indx]))
                queue.append(node.right)
            indx += 1

        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))