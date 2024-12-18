"""
Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7

Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

LINK : https://leetcode.com/problems/minimum-path-sum/description/
"""

# Brute Force
"""
    Time complexity     : O(2^(n + m)) 
    Space complexity    : O(n + m) 

    - Time complexity: In the brute-force approach, at each cell, you make two recursive calls (right and down), leading to exponential growth in the number of calls, hence O(2^(n + m)).
    - Space complexity: Space complexity is O(n + m) due to the recursive call stack depth, which can go up to the sum of the rows and columns.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        total_sum = 0
        def minimum_sum_path(i, j):
            nonlocal total_sum 

            if i == n-1 and j == m-1:
                return grid[i][j]
            
            if( (i < (n-1)) and ( j < (m-1))):
                current_sum = min(
                    minimum_sum_path(i, j+1),
                    minimum_sum_path(i+1, j)
                )
                total_sum = grid[i][j] + current_sum
            elif i == n-1:
                total_sum = grid[i][j] + minimum_sum_path(i, j+1)
            else:
                total_sum = grid[i][j] + minimum_sum_path(i+1, j)

            return total_sum

        return minimum_sum_path(0, 0)

# Medium Effort
"""
    Time complexity     : O(n * m) 
    Space complexity    : O(n * m) 

    - Time complexity: With memoization, each cell is computed once, leading to O(n * m) complexity.
    - Space complexity: Space is required for the dp table (O(n * m)) and the recursive call stack, which contributes to the overall space complexity.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0 for _ in range(m)] for i in range(n)]
        
        total_sum = 0
        def minimum_sum_path(i, j):
            nonlocal total_sum 

            if i == n-1 and j == m-1:
                return grid[i][j]

            if dp[i][j] != 0:
                return dp[i][j]
            
            if( (i < (n-1)) and ( j < (m-1))):
                current_sum = min(
                    minimum_sum_path(i, j+1),
                    minimum_sum_path(i+1, j)
                )
                dp[i][j] = grid[i][j] + current_sum
            elif i == n-1:
                dp[i][j] = grid[i][j] + minimum_sum_path(i, j+1)
            else:
                dp[i][j] = grid[i][j] + minimum_sum_path(i+1, j)

            return dp[i][j]

        res = minimum_sum_path(0, 0)
        return res

# Optimal - Bottom-Up DP (Iterative)
"""
    Time complexity     : O(n * m) 
    Space complexity    : O(n * m) 

    - Time complexity: Iterating through the grid once and filling the dp table gives O(n * m) time complexity.
    - Space complexity: The space complexity is O(n * m) for the dp table used to store the minimum sum path for each cell.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[float('inf')] * m for _ in range(n)]
        dp[n-1][m-1] = grid[n-1][m-1]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i < n-1:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i+1][j])
                if j < m-1:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j+1])

        return dp[0][0] 

# Optimal - Top-Down DP (Recursive)
"""
    Time complexity     : O(n * m) 
    Space complexity    : O(n * m) 

    - Time complexity: With memoization, each cell is computed once, resulting in O(n * m) time complexity.
    - Space complexity: Space is used by the dp table (O(n * m)) and the recursive call stack, leading to a total space complexity of O(n * m).
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0]*m for _ in range(n)]

        def minimum_sum_path(i, j):
            if i < 0 or j < 0:
                return float('inf')

            if i == 0 and j == 0:
                return grid[i][j]
            
            if dp[i][j] != 0:
                return dp[i][j]

            up =  grid[i][j] + minimum_sum_path(i-1, j)
            right = grid[i][j] + minimum_sum_path(i, j-1)
            dp[i][j] = min(up, right)

            return dp[i][j]

        res = minimum_sum_path(n-1, m-1)
        return res 