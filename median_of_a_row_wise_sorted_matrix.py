"""
Median in a row-wise sorted Matrix

You are given a row-wise sorted matrix 'mat' of size m x n where 'm' and 'n' are the numbers of rows and columns of the matrix, respectively.
Your task is to find and return the median of the matrix.

Note:
'm' and 'n' will always be odd.

Example:
Input: 'n' = 5, 'm' = 5
'mat' = 
[     [ 1, 5, 7, 9, 11 ],
      [ 2, 3, 4, 8, 9 ],
      [ 4, 11, 14, 19, 20 ],
      [ 6, 10, 22, 99, 100 ],
      [ 7, 15, 17, 24, 28 ]   ]

Output: 10

Explanation: If we arrange the elements of the matrix in the sorted order in an array, they will be like this-
1 2 3 4 4 5 6 7 7 8 9 9 10 11 11 14 15 17 19 20 22 24 28 99 100 

So the median is 10, which is at index 12, which is midway as the total elements are 25, so the 12th index is exactly midway. Therefore, the answer will be 10. 

Expected Time Complexity:
    Try to solve this in O(32 * m * log(n)).          

Constraints:
    1 <= m < 100
    1 <= n < 100
    1 <= mat[i][j] <=10^9

LINK : https://www.naukri.com/code360/problems/median-of-a-row-wise-sorted-matrix
"""

# Medium 
"""
    Time complexity     : ((m×n)log(m×n))
    Space complexity    : (n*m)
"""
def median(matrix: [[int]], m: int, n: int) -> int:
    list1 = [ matrix[i][j] for i in range(m) for j in range(n) ]
    list1.sort()
    return list1[(m*n)//2]


# Optimal
"""
    Time complexity     : (log(max−min)×m×log(n)) 
    Space complexity    : (1)
"""
def binary_search(mat, target, rows, cols):
    count = 0
    for i in range(rows):
        l, r = 0, cols-1
        while l <= r:
            mid = (l+r)//2
            if mat[i][mid] <= target:
                l = mid+1
            else:
                r = mid-1
        count += l
    return count

def median(matrix: [[int]], m: int, n: int) -> int:
    # m is row
    # n is column
    min_val = matrix[0][0]
    max_val = matrix[0][-1]

    for i in range(1, m):
        min_val = min(min_val, matrix[i][0])
        max_val = max(max_val, matrix[i][-1])

    desired = (m*n)//2 + 1
    while min_val < max_val:
        target = (min_val+max_val)//2
        if binary_search(matrix, target, m, n) < desired:
            min_val = target+1
        else:
            max_val = target
    return min_val
        


