"""
Minimum Spanning Tree

You are given an undirected, connected and weighted graph G(V, E), consisting of V number of vertices (numbered from 0 to V-1) and E number of edges.
Find and print the total weight of the Minimum Spanning Tree (MST) using Kruskal's algorithm.
By definition, a minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

Sample Input 1 :
4 4
0 1 3
0 3 5
1 2 1
2 3 8
Sample Output 1 :
9

Explanation for Sample Input 1:
The edge (2,3) having weight 8 will be excluded from the MST. The total weight of the MST then will be 1 + 3 + 5 = 9.

Sample Input 2:
4 4
1 2 6
2 3 2
1 3 2
1 0 2
Sample Output 2:
6

Constraints :
2 <= V <= 10^5
1 <= E <= 3 * 10^5
0 <= X < N
0 <= Y < N
1 <= W <= 10^4

where V and E represent the number of vertices and edges respectively.
X and Y represent the vertices between which there is an edge.
W is the weight of the edge.

Time limit: 1sec


LINK : https://www.naukri.com/code360/problems/minimum-spanning-tree_631769?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : (v * log E)
    Space complexity    : (v^2)
"""

from collections import defaultdict
import heapq

# Edge class for storing the Edges of thee graph
class Edge:
    def __init__(self, start, end, weight) :

        self.start = start
        self.end = end
        self.weigth = weight

def minimumSpanningTree(edges, V, E):
    adj_list = defaultdict(list)
    for edge in edges:
        adj_list[edge.start].append((edge.end, edge.weigth))
        adj_list[edge.end].append((edge.start, edge.weigth))
    
    priority_queue = []
    visited = [False]*V

    total_sum = 0
    mst = []

    heapq.heappush(priority_queue, (0, 0, -1))
    while priority_queue:
        weight, current_node, parent = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue
        
        visited[current_node]= True

        if parent != -1:
            total_sum += weight
            mst.append((parent, current_node))
        
        for neighbour, wt in adj_list[current_node]:
            heapq.heappush(priority_queue, (wt, neighbour, current_node))
    
    return total_sum

