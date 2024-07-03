"""
Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3

Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100

LINK : https://leetcode.com/problems/unique-paths/description/
"""

# Medium 
"""
    Time complexity     : (2^(m+n)
    Space complexity    : (m+n)
"""
class Solution:
    def findPath(self, m, n, i, j):
        if i > n-1 or j > m-1:
            return 0
        
        if i == n-1 or j == m-1:
            return 1
    
        return self.findPath(m, n, i+1, j, res) + self.findPath(m, n, i, j+1, res) 

    def uniquePaths(self, m: int, n: int) -> int:
        return self.findPath(m, n, 0, 0)


# Optimal
"""
    Time complexity     : (m*n)
    Space complexity    : (m*n)
"""
class Solution:
    def findPath(self, m, n, i, j, dp):
        if i > n-1 or j > m-1:
            return 0
        
        if i == n-1 or j == m-1:
            return 1

        if dp[i][j] == -1:
            dp[i][j] = self.findPath(m, n, i+1, j, dp) + self.findPath(m, n, i, j+1, dp) 

        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*m for _ in range(n)]
        return self.findPath(m, n, 0, 0, dp)

########################  OR   ########################
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
        