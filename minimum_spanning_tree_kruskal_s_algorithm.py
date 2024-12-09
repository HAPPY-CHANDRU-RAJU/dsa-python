"""
Kruskal’s Minimum Spanning Tree Algorithm

A minimum spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices without any cycles and with the minimum possible total edge weight.
A spanning tree’s weight is the sum of the weights of each edge in the spanning tree.

You have been given a connected undirected weighted graph having 'n' vertices, from 1 to 'n', and 'm' edges.
You are given an array 'edges' of size 'm', containing the details of the edges of the graph.

Each element of 'edges' contains three integers, the two vertices that are being connected and the weight of the edge.
Find the weight of the minimum spanning tree of the given graph.

Example :

Input: 'n' = 5, 'm' = 6
'edges' = [[1, 2, 6], [2, 3, 5], [3, 4, 4], [1, 4, 1], [1, 3, 2], [3, 5, 3]]
Output: 11

Explanation: The given graph is:
The minimum spanning tree of the graph is:
And its weight is 1 + 2 + 5 + 3 = 11.

LINK : https://www.naukri.com/code360/problems/kruskal-s-minimum-spanning-tree-algorithm_1082553?leftPanelTabValue=PROBLEM
"""

# Optimal
"""
    Time complexity     : (E log E)
    Space complexity    : ( V + E)
"""

from typing import List

class Disjoint:
    def __init__(self, verties):
        self.parent = {i:i for i in range(verties+1)}
        self.rank = { i:0 for i in range(verties+1)}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        # u is parent, v is child assumption
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u 
            elif self.rank[root_v] > self.rank[root_u]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u 
                self.rank[root_u] += 1

def kruskalMST(n: int, edges: List[List[int]]) -> int:
    """
        KRUSKAL(G)
        Input: Graph G with vertices V and edges E
        Output: Minimum Spanning Tree T

        T ← ∅  (Initialize empty MST)
        Initialize Disjoint Set for vertices V

        Sort edges E by increasing weight

        for each edge (u, v) in E do:
            if FIND(u) ≠ FIND(v) then:  # Check if they belong to different sets
                T ← T ∪ {(u, v)}         # Add edge to MST
                UNION(u, v)             # Merge sets
        
            if |T| == |V| - 1 then:     # Stop when MST has V-1 edges
                break

        Return T
    """
    edges.sort(key=lambda x: x[2])
    
    ds = Disjoint(n)

    mst_total = 0
    mst = []
    for u, v, wt in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u,v,wt))
            mst_total += wt

    return mst_total


