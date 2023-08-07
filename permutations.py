"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""

##### Optimal #####

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(ind):
            if ind >= n:
                ans.append(nums[:])
                return 

            for i in range(ind, n):
                nums[ind] , nums[i] = nums[i] , nums[ind]
                backtrack(ind+1)
                nums[ind] , nums[i] = nums[i] , nums[ind]

        backtrack(0)
        return ans
