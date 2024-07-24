"""
Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
    arr.length >= 3 
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104

LINK :  https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
"""

# Solution
"""
    Time complexity     : (n), where n is the length of the arr
    Space complexity    : (1)
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        if n < 3:
            return False
        
        i = 0 
        while i < n-1 and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == n-1:
            return False
        
        while i < n-1 and arr[i] > arr[i+1]:
            i += 1
            
        return i == n-1
        