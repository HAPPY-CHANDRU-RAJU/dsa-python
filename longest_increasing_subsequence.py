"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.


Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

LINK : https://leetcode.com/problems/longest-increasing-subsequence/description/
"""

# Medium Effort
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n  

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# Optimal
"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""
class Solution:
    def bs(self, data, key):
        start = 0
        end = len(data)
        while start < end:
            mid = (start + end) // 2
            if data[mid] >= key:
                end = mid
            else:
                start = mid + 1
        return start

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        result = []
        for num in nums:
            index = self.bs(result, num)
            if index == len(result):
                result.append(num)
            else:
                result[index] = num
        
        return len(result)


############################# OR #############################


import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return -1
            
        result = []
        for num in nums:
            index = bisect.bisect_left(result, num)
            if index == len(result):
                result.append(num)
            else:
                result[index] = num
        
        return len(result)