"""
Bellman Ford

You have been given a directed weighted graph of ‘N’ vertices labeled from 1 to 'N' and ‘M’ edges. Each edge connecting two nodes 'u' and 'v' has a weight 'w' denoting the distance between them.
Your task is to calculate the shortest distance of all vertices from the source vertex 'src'.


Note:
If there is no path between 'src' and 'ith' vertex, the value at 'ith' index in the answer array will be 10^8.
Example :

3 3 1
1 2 2
1 3 2
2 3 -1

In the above graph: 
The length of the shortest path between vertex 1 and vertex 1 is 1->1 and the cost is 0.
The length of the shortest path between vertex 1 and vertex 2 is 1->2 and the cost is 2.
The length of the shortest path between vertex 1 and vertex 3 is 1->2->3 and the cost is 1.
Hence we return [0, 2, 1].

Note :
It's guaranteed that the graph doesn't contain self-loops and multiple edges. Also, the graph does not contain negative weight cycles.

Sample Input 1 :
4 4 1
1 2 4
1 3 3
2 4 7 
3 4 -2

Sample Output 1 :
0 4 3 1

Explanation For Sample Output 1 :

In the above graph: 
The length of the shortest path between vertex 1 and vertex 1 is 1->1 and the cost is 0.
The length of the shortest path between vertex 1 and vertex 2 is 1->2 and the cost is 4.
The length of the shortest path between vertex 1 and vertex 3 is 1->3 and the cost is 3.
The length of the shortest path between vertex 1 and vertex 4 is 1->3->4 and the cost is 1.
Hence we return [0, 4, 3, 1].

Sample Input 2 :
2 1 1
2 1 3

Sample Output 2 :
0 1000000000

Constraints :
1 <= N <= 50
1 <= M <= 300
1 <= src <= N
1 <= u,v <= N
-10^5 <= w <= 10^5

Time Limit: 1 sec

LINK : https://www.naukri.com/code360/problems/bellmon-ford_2041977?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : O(n * m)
    Space complexity    : O(n)
"""
def bellmonFord(n, m, src, edges):
    """
        ### Bellman-Ford Algorithm (Steps)

        #### 1. **Initialization**:
        - Create a distance array initialized to a large value (`∞` or `10**8`) for all vertices, except the source, which is initialized to `0`.

        #### 2. **Relaxation**:
        - Perform relaxation for all edges `(n-1)` times, where `n` is the number of vertices.
        - For each edge `(u, v, weight)`, check if `distance[u] + weight < distance[v]`. If true, update `distance[v]` with `distance[u] + weight`.

        #### 3. **Negative Weight Cycle Detection**:
        - After the `n-1` relaxations, check for any further relaxation. If any distance can still be updated, it indicates the presence of a negative weight cycle in the graph.

        #### 4. **Termination**:
        - The process ends when all edges have been relaxed and no further distance updates are possible.
    """

    dis = [ 10**8 for i in range(n+1) ]
    dis[src] = 0

    for _ in range(n-1):
        for j in range(m):
            u = edges[j][0]
            v = edges[j][1]
            w = edges[j][2]

            # 10 ** 9
            if (dis[u] != 10**9 and dis[v] > (dis[u] + w)):
                dis[v] = dis[u] + w
    
    return dis
