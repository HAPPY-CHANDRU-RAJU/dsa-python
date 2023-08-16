"""
Matrix Median


"""

#####  Brute Force  #####
def getMedian(matrix):
    list_ = []
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            list_.append(matrix[i][j])
    list_.sort()
    return list_[(n*m)//2] 

##### Better  #####
from bisect import bisect_right as upper_bound

MAX = 100;
 
def getMedian(matrix):
    r, c = len(matrix), len(matrix[0])
    
    low, high = matrix[0][0], 0
    for i in range(r):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][-1])
    
    desired = (r*c+1) // 2
    mid = None
    while low < high:
        mid = low + (high - low) // 2

        cnt = 0
        for i in range(r):
            cnt += upper_bound(matrix[i], mid)
        if cnt < desired:
            low = mid+1
        else:
            high = mid
    return low
    
##### Optimal #####

