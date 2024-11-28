"""
Detect Cycle In A Directed Graph

You are given a directed graph having ‘N’ nodes. A matrix ‘EDGES’ of size M x 2 is given which represents the ‘M’ edges such that there is an edge directed from node EDGES[i][0] to node EDGES[i][1].
Find whether the graph contains a cycle or not, return true if a cycle is present in the given directed graph else return false.

For Example :
In the following directed graph has a cycle i.e. B->C->E->D->B.

Note :
1. The cycle must contain at least two nodes.
2. It is guaranteed that the given graph has no self-loops in the graph.
3. The graph may or may not be connected.
4. Nodes are numbered from 1 to N.
5. Your solution will run on multiple test cases. If you are using global variables make sure to clear them.

Sample Input 1 :
1
5
6
1 2
4 1
2 4
3 4
5 2
1 3
Sample Output 1 :
true

Explanation For Input 1 :
The given graph contains cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1.

Sample Input 2 :
2
5
4
1 2
2 3
3 4
4 5
2
1
1 2
Sample Output 2 :
false
false

Explanation For Input 2 :
The given graphs don’t contain any cycle.

Constraints :
1 ≤ T ≤ 5
2 <= N <= 100
1 <= M <= min(100,N(N-1)/2)
1 <= EDGES[i][0], EDGES[i][1] <= N

Where 'T' is the number of test cases.

Time Limit: 1 sec

LINK : https://www.naukri.com/code360/problems/detect-cycle-in-a-directed-graph_1062626?leftPanelTabValue=PROBLEM
"""

# Optimal - DFS (Depth-First Search)
"""
    Time complexity     : O(V + E)
    Space complexity    : O(V + E)  
"""
from collections import defaultdict, deque

def detectCycleInDirectedGraph(n, edges):
    adj_matrix = defaultdict(list)
    for x, y in edges:
        adj_matrix[x-1].append(y-1)

    def dfs(node, visited, recursion):
        visited[node] = True
        recursion[node] = True

        for neighbours in adj_matrix[node]:
            if not visited[neighbours]:
                if dfs(neighbours, visited, recursion):
                    return True
            elif recursion[neighbours]:
                return True
    
        recursion[node] = False
        return False
    
    visited = [False]*n
    recursion = [False]*n
    for i in range(n):
        if not visited[i]:
            if dfs(i, visited, recursion):
                return True

    return False