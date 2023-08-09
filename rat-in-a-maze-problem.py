"""
Rat in a Maze Problem - I

Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
         
Output:
DDRDRR DRDDRR

Explanation:
The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR  and DDRDRR, when printed in sorted order  we get DDRDRR DRDDRR.
"""


##### Optimal #####

class Solution:
    def findPath(self, m, n):
        def is_valid_move(x, y, n, visited):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and not visited[x][y]
        
        def solve(x, y, n, path, visited):
            if x == n - 1 and y == n - 1:
                ans.append(path)
                return
            
            directions = ['D', 'L', 'R', 'U']
            dx = [1, 0, 0, -1]
            dy = [0, -1, 1, 0]
            
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                
                if is_valid_move(new_x, new_y, n, visited):
                    visited[new_x][new_y] = True
                    solve(new_x, new_y, n, path + directions[i], visited)
                    visited[new_x][new_y] = False
        
        visited = [[False] * n for _ in range(n)]
        ans = []
        
        if m[0][0] == 1:
            visited[0][0] = True
            solve(0, 0, n, '', visited)
        
        return ans


