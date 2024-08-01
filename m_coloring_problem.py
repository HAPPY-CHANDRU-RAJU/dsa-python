"""
M-Coloring Problem

You are given an undirected graph as an adjacency matrix consisting of 'v' vertices and an integer 'm'.
You need to return 'YES' if you can color the graph using at most 'm' colors so that no two adjacent vertices are the same. Else, return 'NO'.

For example:

Input:

If the given adjacency matrix is:
[0 1 0]
[1 0 1]
[0 1 0] and 'm' = 3.

Output: YES

Explanation:
The given adjacency matrix tells us that 1 is connected to 2 and 2 is connected to 3. We can use three different colors and color all three nodes.
Hence we return true.

Sample Input 1:
3 2
0 1 0
1 0 1
0 1 0

Sample Output 1:
YES

Explanation of Input 1:
The adjacency matrix tells us that 1 is connected to 2, and 2 is connected to 3. We can see that a minimum of 2 colors would be needed to color the graph. So it is possible to color the graph in this case.

Sample Input 2:
3 1
0 1 0
1 0 1
0 1 0

Sample Output 2
NO

Constraints:
1 ≤ v ≤ 20
1 ≤ m ≤ v

Time Limit: 1 sec 


LINK : https://www.naukri.com/code360/problems/m-coloring-problem
"""

# Optimal
"""
    Time complexity     : (m^n)      # The algorithm explores each of the m color options for each of the n vertices
    Space complexity    : (n)
"""
from typing import List

def graphColoring(mat: List[List[int]], m: int) -> str:
    n = len(mat)
    color_matrix = [-1] * n 

    def isSafe(x, color):
        for y in range(n):
            if mat[x][y] == 1 and color_matrix[y] == color:
                return False
        return True
    
    def solver(vertex, n, m, mat, color_matrix):
        if vertex == n:
            return True
        
        for curr_color in range(1, m + 1):
            if isSafe(vertex, curr_color):
                color_matrix[vertex] = curr_color
                if solver(vertex + 1, n, m, mat, color_matrix):
                    return True
                color_matrix[vertex] = -1
        return False

    return "YES" if solver(0, n, m, mat, color_matrix) else "NO"

