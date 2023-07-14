"""
Next Permutation

find next lexicographically greater permutation 
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).
"""

# Intuition
"""
step 1: traversal reverse if a[i] < a[i+1] then take i as ind
step 2: if ind == -1 then step 5
step 3: traversal reverse if a[i] > a[ind] then take i as ind2
step 4: swap ind, ind2 values of list
step 5: reverse from ind+1 values of list
"""

# Optimal
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        ind, ind2 = -1, -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break
        
        if ind == -1:
            nums.reverse()
            return nums

        for i in range(n-1, ind, -1):
            if nums[i] > nums[ind]:
                ind2 = i
                break
        
        nums[ind2], nums[ind] = nums[ind], nums[ind2]

        nums[ind+1:] = reversed(nums[ind+1:])
        return nums

