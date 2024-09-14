"""
Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange,
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

LINK : https://leetcode.com/problems/rotting-oranges/description/
"""

# Optimal
"""
    Time complexity     : (n*m)
    Space complexity    : (n*m)
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_count = 0
        rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:   
                   fresh_count += 1
        
        directions = ((0,1), (0, -1), (1,0), (0,1))
        time = 0

        while rotten and fresh_count > 0:
            time += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                        grid[nx][ny]= 2
                        rotten.append((nx, ny))
                        fresh_count -= 1
        
        return time if fresh_count == 0 else -1
