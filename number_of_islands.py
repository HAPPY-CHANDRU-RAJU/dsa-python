"""
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

LINK : https://leetcode.com/problems/number-of-islands/description/
"""

# Optimal - DFS (Depth-First Search)
"""
    Time complexity     :  ( m*n )
    Space complexity    :  ( m*n )
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])        
    
        count = 0
        visited = [ [False for _ in range(n) ] for i in range(m)] 

        def dfs(i, j, m, n, visited, grid):
            directions = [
                [-1, 0],
                [0, -1],
                [0, 1],
                [1, 0]
            ]
            for direction in directions:
                new_i = i+direction[0]
                new_j = j+direction[1]

                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == "1" and visited[new_i][new_j] is False:
                    visited[new_i][new_j] = True
                    dfs(new_i, new_j, m, n, visited, grid)

        for i in range(m):
            for j in range(n):
                if (not visited[i][j]) and (grid[i][j] == "1"):
                    visited[i][j] = True
                    count += 1
                    dfs(i, j, m, n, visited, grid)
        return count
                

"""
    Time complexity     : ( m*n )
    Space complexity    : ( min(m, n) )
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])        
    
        count = 0

        def dfs(i, j, m, n, grid):
            grid[i][j] = "0"
            directions = [
                [-1, 0],
                [0, -1],
                [0, 1],
                [1, 0]
            ]
            for direction in directions:
                new_i = i+direction[0]
                new_j = j+direction[1]

                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == "1":
                    grid[i][j] = "0"
                    dfs(new_i, new_j, m, n, grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j, m, n, grid)
        return count



# Optimal - BFS (Breadth-First Search)
"""
    Time complexity     : ( m*n )
    Space complexity    : ( m*n )
"""
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])        
    
        count = 0
        visited = [ [False for _ in range(n) ] for i in range(m)] 

        def bfs(sr, sc, m, n, visited, grid):
            queue = deque([(sr, sc)])

            directions = [
                [-1, 0],
                [0, -1],
                [0, 1],
                [1, 0]
            ]
            while queue:
                i, j = queue.popleft()

                for direction in directions:
                    new_i = i+direction[0]
                    new_j = j+direction[1]

                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == "1" and visited[new_i][new_j] is False:
                        visited[new_i][new_j] = True
                        queue.append((new_i, new_j))
                

        for i in range(m):
            for j in range(n):
                if (not visited[i][j]) and (grid[i][j] == "1"):
                    visited[i][j] = True
                    count += 1
                    bfs(i, j, m, n, visited, grid)
        return count
                

"""
    Time complexity     : ( m*n )
    Space complexity    : ( min(m, n) )
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])        
    
        count = 0

        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = "0"

            directions = [
                [-1, 0],
                [0, -1],
                [0, 1],
                [1, 0]
            ]
            while queue:
                x, y = queue.popleft()
                for di, dj in directions:
                    nx = x+di
                    ny = y+dj

                    if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == "1" :
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count
                