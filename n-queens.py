"""
N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9

LINK : https://leetcode.com/problems/n-queens/description/
"""


# Optimal
"""
    Time complexity     : (n!)
    Space complexity    : (n^2)
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(col, n, board, output):
            if col == n:
                output.append([ "".join(row) for row in board])
                return
            for i in range(n):
                if isSafe(board, i, col):
                    board[i][col] = 'Q'
                    helper(col+1, n, board, output)
                    board[i][col] = '.'
        
        def isSafe(board, row, col):
            # same row any queen
            for i in range(col):
                if board[row][i] == 'Q':
                    return False
            # upper left any queen
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            # Lower left any queen
            for i, j in zip(range(row, n), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            return True

        board = [["."]*n for _ in range(n)]
        output = []
        helper(0, n, board, output)
        return output
