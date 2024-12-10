"""
Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6

Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0

Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

LINK : https://leetcode.com/problems/maximum-product-subarray/
"""

# Brute Force
"""
    Time complexity     : (n^3)
    Space complexity    : (1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = float('-inf')
        for i in range(n):
            for j in range(i, n):
                current_prod = reduce(lambda x,y: x*y, nums[i:j+1])
                max_prod = max(current_prod, max_prod)
        return max_prod

# Medium Effort
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = float('-inf')
        for i in range(n):
            current_prod = 1
            for j in range(i, n):
                current_prod *= nums[j]
                max_prod = max(current_prod, max_prod)
        return max_prod

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]

        result = nums[0]
        for num in nums[1:]:
            if num < 0:
                min_prod, max_prod = max_prod, min_prod
            
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            result = max(result, max_prod)

        return result


"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float("-inf")
        prefix = 1
        suffix = 1

        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n-i-1]

            result = max(result, max(prefix, suffix))
        return result