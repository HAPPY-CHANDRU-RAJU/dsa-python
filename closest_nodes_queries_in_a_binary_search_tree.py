"""
Closest Nodes Queries in a Binary Search Tree

You are given the root of a binary search tree and an array queries of size n consisting of positive integers.
Find a 2D array answer of size n where answer[i] = [mini, maxi]:
    mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
    maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.

Return the array answer.


Example 1:
Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
Output: [[2,2],[4,6],[15,-1]]

Explanation: We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].

Example 2:
Input: root = [4,null,9], queries = [3]
Output: [[-1,4]]

Explanation: The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
1 <= Node.val <= 106
n == queries.length
1 <= n <= 105
1 <= queries[i] <= 106

LINK : https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/
"""

# Medium Effort
"""
    Time Complexity:    O(m * h) = O(m * n)     (worst case, skewed tree)
    Space Complexity:   O(n)                    (worst case, skewed tree)
"""

class Solution:
    def findCeilFloor(self, root, key):
        ceil, floor = None, None

        curr = root
        while curr:
            if curr.val == key:
                return [curr.val, curr.val]
            elif curr.val > key:
                ceil = curr.val
                curr = curr.left
            else:
                floor = curr.val
                curr = curr.right
        
        return [
           floor if floor else -1,
           ceil if ceil else -1
        ]    

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        result = []
        for query in queries:
            result.append(self.findCeilFloor(root, query))
        return result


# Optimal
"""
    Time Complexity:    O(n + m * log n)
    Space Complexity:   O(n + m)                (or O(n) for the stack in a skewed tree)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from bisect import bisect_right, bisect_left

class Solution:
    def inorderList(self, root, sorted_val):
        if not root:
            return 
        
        self.inorderList(root.left, sorted_val)
        sorted_val.append(root.val)
        self.inorderList(root.right, sorted_val)
    
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sorted_val = []
        self.inorderList(root, sorted_val)
        
        result = []
        for query in queries:
            ceil_index = bisect_left(sorted_val, query)
            floor_index = bisect_right(sorted_val, query)-1

            ceil = sorted_val[ceil_index] if ceil_index < len(sorted_val) else -1
            floor = sorted_val[floor_index] if floor_index >= 0 else -1
            result.append([floor, ceil])
        return result