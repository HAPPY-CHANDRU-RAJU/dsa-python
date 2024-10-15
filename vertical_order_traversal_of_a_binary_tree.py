"""
Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
Return the vertical order traversal of the binary tree.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]

Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.


Example 3:
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]

Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000

LINK : https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
"""

# Brute Force - DFS
"""
    Time complexity     : (n log n)
    Space complexity    : (n) call stack recursive
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = {}
        max_indx = 0
        min_indx = 0

        stack = [[root, 0, 0]]
        while stack:
            node, state, level = stack.pop()
            if state not in result:
                temp = dict()
                temp[level] = [node.val]
                result[state] = temp
            elif level not in result[state]:
                result[state][level] = [node.val]
            else:
                result[state][level].append(node.val)

            max_indx = max(max_indx, state)
            min_indx = min(min_indx, state)

            if node.left:
                stack.append([node.left, state-1, level+1])

            if node.right:
                stack.append([node.right, state+1, level+1])
        
        res = []
        for i in range(min_indx, max_indx+1):
            item = result[i]
            temp = []
            for key in sorted(item.keys()):
                temp.extend(sorted(item[key]))
            res.append(temp)
        
        return res

# Medium  - BFS so Recursive risk eliminated
"""
    Time complexity     : (n log n)
    Space complexity    : (n) queue
"""
from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = defaultdict(lambda: defaultdict(list))  
        queue = deque([(root, 0, 0)])
        min_indx, max_indx = 0, 0 
        
        while queue:
            node, col, row = queue.popleft()
            result[col][row].append(node.val)
            
            min_indx = min(min_indx, col)
            max_indx = max(max_indx, col)
            
            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))
        
        res = []
        for col in range(min_indx, max_indx + 1):
            col_nodes = []
            for row in sorted(result[col].keys()):
                col_nodes.extend(sorted(result[col][row]))
            res.append(col_nodes)
        
        return res


# Optimal
"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""
from collections import defaultdict, deque
import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes = []
        queue = deque([(root, 0, 0)])
        min_indx, max_indx = 0, 0
        
        while queue:
            node, col, row = queue.popleft()
            heapq.heappush(nodes, (col, row, node.val))
            
            min_indx = min(min_indx, col)
            max_indx = max(max_indx, col)
            
            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))
        
        result = defaultdict(list)
        while nodes:
            col, row, val = heapq.heappop(nodes) 
            result[col].append(val)
        
        return [result[i] for i in range(min_indx, max_indx + 1)]

######################### OR #########################

"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""
from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes = []
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, col, row = queue.popleft()
            nodes.append((col, row, node.val))
            
            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))
        
        nodes.sort()

        result = defaultdict(list)
        for node in nodes:
            col, row, val = node
            result[col].append(val)
        
        return [result[i] for i in sorted(result.keys())]
