"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    
Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

LINK : https://leetcode.com/problems/valid-sudoku/description/
"""


# Brute Force
"""
    Time complexity     : (1)
    Space complexity    : (1)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row(pos):
            seen = set()
            for i in range(9):
                num = board[pos][i]
                if num != "." and num in seen:
                    return False
                seen.add(num)
            return True

        def is_valid_col(pos):
            seen = set()
            for i in range(9):
                num = board[i][pos]
                if num != "." and num in seen:
                    return False
                seen.add(num)
            return True

        def is_valid_box(row, col):
            seen = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    num = board[i][j]
                    if num != "." and num in seen:
                        return False
                    seen.add(num)
            return True
        
        for i in range(9):
            if (not is_valid_col(i) ) or (not is_valid_row(i)):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid_box(i, j):
                    return False
        return True

# Optimal
"""
    Time complexity     : (1)
    Space complexity    : (1)
"""
class Solution:
    '''
        Time Complexity:
            We iterate over the 9x9 board once (O(81) ≈ O(1), as it's a fixed size).
            Each lookup and insertion in a set takes O(1) time.
            Overall, the time complexity is O(1) (constant time), because 81 operations are negligible in complexity analysis.
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [ set() for _ in range(9)]
        cols = [ set() for _ in range(9)]
        boxs = [ set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                
                box_index =  (i // 3) * 3 + (j // 3) 
                if num in rows[i] or \
                    num in cols[j] or \
                    num in boxs[box_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxs[box_index].add(num)

        return True
