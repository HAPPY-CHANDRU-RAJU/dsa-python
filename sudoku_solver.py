"""
Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.

It is guaranteed that the input board has only one solution.

LINK : https://leetcode.com/problems/sudoku-solver/
"""

# Optimal
"""
    Time complexity     : (N!) or (9^81)
    Space complexity    : (1)
"""
class Solution:
    def solver(self, board, i, j) -> None:
            if j == 9:
                i += 1
                j = 0
            
            if i == 9:
                return True

            if board[i][j] == ".":
                for num in range(1, 10):
                    if self.isRight(board, i, j, str(num)):
                        board[i][j] = str(num)
                        if self.solver(board, i, j+1):
                            return True
                        board[i][j] = "."
                return False                                   # if rollback return False
            else:
                return self.solver(board, i, j+1)
            
    def isRight(self, board, i, j, num) -> bool:
        if ( num in board[i] ):
            return False
        
        if ( num in [ board[row][j] for row in range(9)] ):
            return False

        for r in range((i//3)*3, ((i//3)*3)+3 ): 
            for c in range((j//3)*3, ((j//3)*3)+3 ): 
                if board[r][c] == num:
                    return False
        return True
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solver(board, 0, 0)

        
        