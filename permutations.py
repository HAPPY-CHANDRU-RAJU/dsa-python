"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

LINK : https://leetcode.com/problems/permutations/description/
"""

# Brute Force
"""
    Time complexity     : (n!⋅n)
    Space complexity    : (n!⋅n)
"""
from itertools import permutations

def permute(self, nums):
    return list(permutations(nums))

# Medium 
"""
    Time complexity     : (n!⋅n)
    Space complexity    : (n!⋅n)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def permutations(start, a, n):
            if start == n:
                res.append(a.copy())
            else:
                for i in range(start, n):
                    a[i], a[start] = a[start], a[i]
                    permutations(start+1, a, n)
                    a[i], a[start] = a[start], a[i]
        
        permutations(0, nums, n)
        return res


# Optimal
"""
    Time complexity     : (n!⋅n)
    Space complexity    : (n!⋅n)
"""

# Heap's algorithm is often considered optimal due to its minimized number of swaps and more efficient generation of permutations in some practical scenarios.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def permulate(k, a):
            if k == 1:
                res.append(a.copy())
            else:
                permulate(k-1, a)
                for i in range(k-1):
                    if k%2 == 0:
                        a[i], a[k-1] =  a[k-1], a[i]
                    else:
                        a[0], a[k-1] = a[k-1], a[0]
                    permulate(k-1, a) 

        permulate(n, nums)
        res.sort()
        return res