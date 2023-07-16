"""
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
"""
# Brute 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return False
            if target in matrix[i]:
                return True
        return False
                    

# Optimal
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        i = 0 
        while matrix[i][0] <= target:
            if matrix[i][0] == target:
                return True
            i += 1
            if i == n:
                break
        
        lis = matrix[i-1].copy()
        def binarySearch(left, right):
            if left > right:
                return False
            
            mid = (left+right)//2
            if lis[mid] > target:
                return binarySearch(left, mid-1)
            elif lis[mid] < target:
                return binarySearch(mid+1, right)
            return True
        
        return binarySearch(0, m-1)

