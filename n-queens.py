"""
N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

"""

#####  Brute Force  #####
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isPlace(row, col):
            for i in range(col):
                if board[row][i] == "Q":
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == "Q":
                    return False
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == "Q":
                    return False
            return True

        def solveNQueensUtils( col , board, ans):
            if col == n :
                ans.append(["".join(i) for i in board])
                return 
            
            for i in range(n):
                if isPlace(i, col):
                    board[i][col] = "Q"
                    solveNQueensUtils(col+1, board, ans)
                    board[i][col] = "."
            return 
        

        board = [['.' for j in range(n)] for i in range(n)]
        ans = []
        solveNQueensUtils(0, board, ans)
        return ans
