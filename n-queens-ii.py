"""
N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2

Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9

LINK : https://leetcode.com/problems/n-queens-ii/
"""


# Optimal
"""
    Time complexity     : (n!)
    Space complexity    : (n^2)
"""
class Solution:
    def helper(self, col, n, board, output):
        if col == n:
            output.append([ "".join(row) for row in board ])
            return
        for i in range(n):
            if self.isSafe(i, col, n, board):
                board[i][col] = "Q"
                self.helper(col+1, n, board, output)
                board[i][col] = "."
        return

    def isSafe(self, row, col, n, board):
        # Same row
        for i in range(col):
            if board[row][i] == "Q":
                return False
        
        # Upper left
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        # Lower left
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        return True

    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for _ in range(n)]
        output = []
        self.helper(0, n, board, output)
        return len(output)