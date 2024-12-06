"""
Floyd Warshall ( Multi-source shortest path )

You have been given a directed weighted graph of ‘N’ vertices labeled from 1 to 'N' and ‘M’ edges. Each edge connecting two nodes 'u' and 'v' has a weight 'w' denoting the distance between them.
Your task is to find the length of the shortest path between the ‘src’ and ‘dest’ vertex given to you in the graph using Flloyd warshall’s algorithm. The graph may contain negatively weighted edges.

Example :
3 3 1 3
1 2 2
1 3 2
2 3 -1
In the above graph, the length of the shortest path between vertex 1 and vertex 3 is 1->2->3 with a cost of 2 - 1 = 1.

Note :
It's guaranteed that the graph doesn't contain self-loops and multiple edges. Also the graph does not contain negative weight cycles.

Sample Input 1 :
1    
4 4 1 4
1 2 4
1 3 3
2 4 7 
3 4 -2

Sample Output 1 :
1

Explanation For Sample Output 1 :
The optimal path from source vertex 1 to destination vertex 4 is 1->3->4 with a cost of 3 - 2 = 1.

Sample Input 2 :
1
2 1 1 2
2 1 3

Sample Output 2 :
1000000000

LINK : https://www.naukri.com/code360/problems/floyd-warshall_2041979?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : (vn^3)
    Space complexity    : (n)
"""
def floydWarshall(n, m, src, dest, edges):

    adj_matrix = [[ float('inf') for _ in range(n)] for i in range(n)]
    for u, v, wt in edges:
        adj_matrix[u-1][v-1] = wt
    
    for var in range(n):
        for i in range(n):        
            for j in range(n):
                if i == j:
                    adj_matrix[i][i] = 0
                    continue 
                
                if (adj_matrix[i][var] == float('inf') or adj_matrix[var][j] == float('inf')):
                    continue
                
                adj_matrix[i][j] = min(
                        adj_matrix[i][j],
                        adj_matrix[i][var] + adj_matrix[var][j]
                    )

    result = adj_matrix[src-1][dest-1]
    if result == float('inf'):
        return 1000000000 
    return result
    