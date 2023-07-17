"""
Find the Majority Element that occurs more than N/2 times
Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.
"""

# Better
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count_ = Counter(nums)

        majority = len(nums)//2
        for ele , c in count_.items():
            if c > majority:
                return ele

        
# Moore’s Voting Algorithm 
# Optimal
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        el = None

        for i in range(n):
            if cnt == 0 :
                cnt = 1
                el = nums[i]
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        cnt = 0    
        for i in range(n):
            if el == nums[i]:
                cnt += 1

        if cnt > (n/2):
            return el
        return -1
