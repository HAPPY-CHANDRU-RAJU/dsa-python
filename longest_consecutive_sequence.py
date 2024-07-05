"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109

LINK : https://leetcode.com/problems/longest-consecutive-sequence/description/
"""

# Brute Force
"""
    Time complexity     : (n log n)
    Space complexity    : (1)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return 0

        nums.sort()
        cnt, max_ = 1, 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    cnt += 1
                else:
                    cnt = 1
                max_ = max(cnt, max_)
        return max_


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num+1) in numSet:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest
