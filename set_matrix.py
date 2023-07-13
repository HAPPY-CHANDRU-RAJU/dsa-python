"""
Set Matrix Zero
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
"""

# Brute Force
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        m = len(matrix)

        row = [0]*m
        col = [0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j]= 0

# Optimal
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        m = len(matrix)

        col = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col = True
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if col:
            for i in range(m):
                matrix[i][0] = 0        
        