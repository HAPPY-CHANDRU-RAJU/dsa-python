"""
Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:
0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 
Example 1:
Input: nums = [1,3,2,3,1]
Output: 2

Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:
Input: nums = [2,4,3,5,1]
Output: 3

Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

LINK : https://leetcode.com/problems/reverse-pairs/description/
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]*2:
                    cnt += 1
        return cnt

# Optimal 
"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(low, high):
            if low >= high:
                return 0
            
            mid = (low+high)//2
            cnt = mergeSort(low, mid)+ mergeSort(mid+1, high)

            i = low
            j = mid+1
            while i <= mid and j <= high:
                if nums[i] > nums[j]*2:
                    j += 1
                    cnt  += (mid-i+1)
                else:
                    i += 1
            nums[low:high+1] = sorted(nums[low:high+1])
            return cnt
        return mergeSort(0, len(nums)-1)
