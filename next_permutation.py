"""
Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

LINK : https://leetcode.com/problems/next-permutation/description/
"""

# Brute Force
"""
    Time complexity     :  (n!)
    Space complexity    :  (n!)
"""
from itertools import permutations

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        permutation_lst = sorted(set(map(tuple, permutations(nums))))
        
        current_perm_index = permutation_lst.index(tuple(nums))
        
        next_perm_index = (current_perm_index + 1) % len(permutation_lst)
        next_perm = permutation_lst[next_perm_index]
        
        for i in range(len(nums)):
            nums[i] = next_perm[i]
        

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""

##### Intuition #####
"""
Step 1: traversal reverse if a[i] < a[i+1] then take i as ind
Step 2: if ind == -1 then step 5
Step 3: traversal reverse if a[i] > a[ind] then take i as ind2
Step 4: swap ind, ind2 values of list
Step 5: reverse from ind+1 values of list
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind1 , ind2 = -1, -1
        n = len(nums)

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind1 = i
                break
        
        if ind1 == -1:
            nums.reverse()
            return 

        for j in range(n-1, ind1, -1):
            if nums[j] > nums[ind1]:
                ind2 = j 
                break
        
        nums[ind2], nums[ind1] = nums[ind1], nums[ind2]
    
        nums[ind1+1:] = reversed(nums[ind1+1:])


        