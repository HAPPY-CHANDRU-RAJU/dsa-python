"""
Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:
Input: x = 4
Output: 2

Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
Constraints:
0 <= x <= 231 - 1

LINK : https://leetcode.com/problems/sqrtx/description/
"""

# Medium effort
"""
    Time complexity     : (log x)
    Space complexity    : (1)
"""
# Newton-Raphson method 
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        guess = x
        tolerance = 0.000000001
        while (guess*guess-x) > tolerance:
            guess = (guess + x/ guess) /2
        return int(guess)

# Optimal
"""
    Time complexity     : (log x)
    Space complexity    : (1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0

        low, high = 0, x
        while low <= high:
            mid = (low+high)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                low = mid+1
            else:
                high = mid-1
        return high
            