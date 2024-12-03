"""
Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
 
Constraints:

1 <= n <= 19

LINK : https://leetcode.com/problems/unique-binary-search-trees/description/?envType=problem-list-v2&envId=binary-search-tree
"""

# Optimal
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
class Solution:
    def numTrees(self, n: int) -> int:
        unique_tree = [0]*(n+1)
        unique_tree[0] = unique_tree[1] = 1 

        for node in range(2, n+1):
            total = 0
            for root in range(1, node+1):
                left = root - 1  # Nodes on the left subtree
                right = node - root  # Nodes on the right subtree
                total += unique_tree[left] * unique_tree[right]
            unique_tree[node] = total

        return unique_tree[n]