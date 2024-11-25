"""
Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]

Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []

Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

LINK : https://leetcode.com/problems/clone-graph/
"""

# Optimal
"""
    Time complexity     : O(V + E)
        - V: Number of nodes (vertices)
        - E: Number of edges
        - Each node is visited once, and all its edges are processed once.

    Space complexity    : O(V)
        - BFS queue can hold up to O(V) nodes in the worst case.
        - The `old_to_new` dictionary stores up to O(V) cloned nodes.
"""
from collections import deque
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Map to store original nodes as keys and their clones as values
        old_to_new = {node: Node(node.val)}
        
        # BFS queue
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in old_to_new:
                    # Clone the neighbor and enqueue it
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Link the current node's clone to the neighbor's clone
                old_to_new[current].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]


########################### OR ############################


# Optimal
"""
    Time complexity     : O(V + E)
        - V: Number of nodes (vertices)
        - E: Number of edges
        - Each node is visited once, and all its edges are processed once during the DFS traversal.

    Space complexity    : O(V)
        - Recursive call stack can go up to O(V) in the worst case for a graph with V nodes.
        - The `old_to_new` dictionary stores up to O(V) cloned nodes.
"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            # Create a copy of the current node
            copy = Node(node.val)
            old_to_new[node] = copy

            # Recursively copy all neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node)
