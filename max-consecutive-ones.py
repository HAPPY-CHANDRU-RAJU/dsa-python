"""
Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.


Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

"""

##### Optimal #####

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for i in nums:
            if i == 0:
                cnt = 0
            else:
                cnt += 1
                res = max(res, cnt)
        return res

