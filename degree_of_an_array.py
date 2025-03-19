"""
Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.


Example 1:

Input: nums = [1,2,2,3,1]
Output: 2

Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6

Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 
Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

LINK : https://leetcode.com/problems/degree-of-an-array/description/
"""

# Medium Effort
"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""
from collections import Counter, defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        temp = defaultdict(list)
        for item in frequency.items():
            temp[item[1]].append(item[0])
        max_frequency_items = sorted(temp.items(), key=lambda x: x[0], reverse=True)[0][1]

        min_degree = float('inf')
        for item in max_frequency_items:
            s, e = None, None
            for i in range(len(nums)):
                if s == None and nums[i] == item:
                    s = i
                if nums[i] == item:
                    e = i+1
            min_degree = min(min_degree, e-s)
        return min_degree


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
from collections import Counter, defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        item_frequency = {}
        for i, num in enumerate(nums):
            if num not in item_frequency:
                item_frequency[num] = [1, i, i]
            else:
                item_frequency[num][0] += 1
                item_frequency[num][-1] = i
        
        freq = [ (item[1][0], item[1][2]-item[1][1]+1 )  for item in item_frequency.items()]
        return sorted(freq, key=lambda x: (x[0], -x[-1]), reverse=True)[0][-1]
