"""
Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where:
    0 <= i < j < nums.length and
    nums[i] > 2 * nums[j].
"""

# Brute Force
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > 2*nums[j]:
                    cnt += 1

        return cnt

# Optimal
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort( low, high):
            if low >= high:
                return 0
            
            mid = (low+high)//2
            count = mergeSort(low, mid) + mergeSort( mid+1, high)

            i = low
            j = mid+1

            while i <= mid  and j <= high:
                if nums[i] > 2*nums[j]:
                    j += 1
                    count += (mid-i+1)
                else:
                    i += 1 

            nums[low:high + 1] = sorted(nums[low:high + 1])
            return count
        return mergeSort(0, len(nums)-1)
    