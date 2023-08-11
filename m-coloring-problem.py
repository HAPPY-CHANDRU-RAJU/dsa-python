"""
M-Coloring Problem

Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

Example 1:

Input:
N = 4
M = 3
E = 5
Edges[] = {(0,1),(1,2),(2,3),(3,0),(0,2)}

Output: 1

Explanation: It is possible to colour the
given graph using 3 colours.

"""

##### Optimal #####

def graphColoring(graph, k, V):
    color = [0]*V
    
    def  isSafe(graph, color, node, n, col):
        for k in range(n):
            if k != node and color[k] == col and graph[k][node] == 1:
                return False
        return True
    
    def solve(graph, color, node, m,  n):
        if node == n:
            return True
        
        for col in range(1, m+1):
            if isSafe(graph, color, node, n, col):
                color[node] = col
                if solve(graph, color, node+1, m , n) == True:
                    return True
                color[node] = 0
                
        return False
    return solve(graph, color, 0, k, V)
    