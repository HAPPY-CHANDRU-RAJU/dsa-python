"""
Merge two sorted arrays with O(1) extra space

We are given two sorted arrays. We need to merge these two arrays such that the initial numbers (after complete sorting) are in the first array and the remaining numbers are in the second array

Examples: 
Input: ar1[] = {10}, ar2[] = {2, 3}
Output: ar1[] = {2}, ar2[] = {3, 10}  

Input: ar1[] = {1, 5, 9, 10, 15, 20}, ar2[] = {2, 3, 8, 13}
Output: ar1[] = {1, 2, 3, 5, 8, 9}, ar2[] = {10, 13, 15, 20}
"""

"""
# GAP Method
1. First, assume the two arrays as a single array and calculate the gap value i.e. ceil((size of arr1[] + size of arr2[]) / 2).
2. We will perform the following operations for each gap until the value of the gap becomes 0:
    Place two pointers in their correct position like the left pointer at index 0 and the right pointer at index (left+gap).
    Again we will run a loop until the right pointer reaches the end i.e. (n+m). Inside the loop, there will be 3 different cases:
    If the left pointer is inside arr1[] and the right pointer is in arr2[]: We will compare arr1[left] and arr2[right-n] and swap them if arr1[left] > arr2[right-n].
    If both the pointers are in arr2[]: We will compare arr1[left-n] and arr2[right-n] and swap them if arr1[left-n] > arr2[right-n].
    If both the pointers are in arr1[]: We will compare arr1[left] and arr2[right] and swap them if arr1[left] > arr2[right].
3. After the right pointer reaches the end, we will decrease the value of the gap and it will become ceil(current gap / 2). 
4. Finally, after performing all the operations, we will get the merged sorted array.
"""

# Optimal
from typing import *

def swapEle(a, b, indx, indx2):
    if a[indx] > b[indx2]:
        a[indx], b[indx2] = b[indx2], a[indx]
    
def gapCal(gap):
    return (gap//2)+(gap%2)

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    n = len(a)
    m = len(b)
    len_ = n+m
    gap  = gapCal(len_)
    while gap > 0 :
        left = 0
        right = left + gap
        while right < len_:
            if left < n and right >= n:
                swapEle(a, b, left, right-n)
            elif left >= n :
                swapEle(b, b, left-n, right -n)
            else:
                swapEle(a,a,left, right )
            right += 1
            left += 1

        if gap == 1:
            break
        
        gap = gapCal(gap)
    return a+b
