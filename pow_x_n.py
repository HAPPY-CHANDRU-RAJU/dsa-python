"""
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000

Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1

n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104

LINK : https://leetcode.com/problems/powx-n/description/
"""

# 
"""
    Time complexity     : (1)
    Space complexity    : (1)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

# Brute Force 
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x

        ans = 1
        for _ in range(1, n+1):
            ans = ans*x
            
        return ans 

# Optimal
"""
    Time complexity     : (log n)
    Space complexity    : (1)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 :
            return 1
        
        if n < 0:
            n = -n
            x = 1/x
        
        ans = self.myPow(x, n//2)
        if n%2 ==0:
            return ans*ans
        else:
            return ans*ans*x