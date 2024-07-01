"""
Count Inversions

For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.
An inversion is defined for a pair of integers in the array/list when the following two conditions are met.

A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:
    1. 'ARR[i] > 'ARR[j]' 
    2. 'i' < 'j'

Where 'i' and 'j' denote the indices ranging from [0, 'N').

Input:
3
3 2 1

Output:
3

Explanation:
We have a total of 3 pairs which satisfy the condition of inversion. (3, 2), (2, 1) and (3, 1).


Input:
5
2 5 1 3 4

Output:
4

Explanation:
We have a total of 4 pairs which satisfy the condition of inversion. (2, 1), (5, 1), (5, 3) and (5, 4).

Constraints :
1 <= N <= 10^5 
1 <= ARR[i] <= 10^9

Where 'ARR[i]' denotes the array element at 'ith' index.


LINK : https://www.naukri.com/code360/problems/count-inversions_615
"""

# Brute Force
"""
    Time complexity     : O(N^2)
    Space complexity    : O(1)
"""

def getInversions(arr, n):
    totalInversions = 0
    for i in range(n) :
        for j in range (i+1, n) :
            if (arr[i] > arr[j]) :
                totalInversions += 1

    return totalInversions

# Optimal
"""
    Time complexity     : O(N*logN)
    Space complexity    : O(N)
"""

""" Merge Sort Algorithm """
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1

    cnt = 0
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            cnt += (mid-left+1)     # Logic 
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]

    return cnt

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high: 
        return cnt
    mid = floor((low+high)/2)
    cnt += mergeSort(arr, low, mid)
    cnt += mergeSort(arr, mid+1, high)
    cnt += merge(arr, low, mid, high)
    return cnt

def getInversions(arr, n) :
    return mergeSort(arr, 0, n-1)
