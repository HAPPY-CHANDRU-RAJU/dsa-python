"""
Unique Path

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

"""

# Recursion
# Brute Force
class Solution:
    def countPath(self,i,j,n,m,num):
        if i==n-1 or j == m-1:
            return 1
        if i > n-1 or j > m-1:
            return 0
        num =+ self.countPath(i+1,j,n,m,num) + self.countPath(i,j+1,n,m,num)
        return num

    def uniquePaths(self, m: int, n: int) -> int:
        num = 0
        return self.countPath(0,0,n,m,num)


# Better
class Solution:
    def countpath(self,i,j,n,m, dp):
        if i == m-1  or j == n-1:
            return 1
        
        if i > m-1 or j > n-1:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j] 
        else:
            dp[i][j] = self.countpath(i,j+1,n,m,dp) + self.countpath(i+1,j,n,m,dp)
            return dp[i][j]
        
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        return self.countpath(0,0,n,m,dp)

# Optimal
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Time: O(M* N)
        Space: O(M*N)
        '''
        rows = m
        cols = n
        columns = [1] * cols
        grid = [columns for i in range(0, rows)]
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        
        return grid[rows - 1][cols - 1]
        