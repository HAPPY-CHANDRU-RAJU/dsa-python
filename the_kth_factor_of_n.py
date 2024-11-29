"""
The kth Factor of n

You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
 
Example 1:
Input: n = 12, k = 3
Output: 3

Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

Example 2:
Input: n = 7, k = 2
Output: 7

Explanation: Factors list is [1, 7], the 2nd factor is 7.

Example 3:
Input: n = 4, k = 4
Output: -1

Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
 
Constraints:
1 <= k <= n <= 1000

Follow up:
Could you solve this problem in less than O(n) complexity?

LINK : https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
"""

# Brute Force
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []
        for i in range(1, n+1):
            if n % i == 0:
                factor.append(i)
        
        return factor[k-1] if k <= len(factor) else -1

# Medium Effort
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1

            if count == k:
                return i
        return -1

# Optimal
"""
    Time complexity     : O(√n log n)
    Space complexity    : O(√n)
"""
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                # Added Smallest Number
                factors.append(i)

                # Added Corresponding Larger Number
                if i != n // i:
                    factors.append(n//i)
            
        factors.sort()
        return factors[k-1]  if k <= len(factors) else -1