"""
Harshad Number

An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. 
Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.

Example 1:
Input: x = 18
Output: 9

Explanation:
The sum of digits of x is 9. 18 is divisible by 9. So 18 is a Harshad number and the answer is 9.

Example 2:
Input: x = 23
Output: -1

Explanation:
The sum of digits of x is 5. 23 is not divisible by 5. So 23 is not a Harshad number and the answer is -1.


Constraints:
1 <= x <= 100

LINK : https://leetcode.com/problems/harshad-number/description/
"""

# Brute Force
"""
    Time complexity     : (log x)
    Space complexity    : (1)
"""
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x < 10:
            return x

        total = sum([int(num) for num in str(x)])
        return total if (x%total == 0) else -1

# Medium 
"""
    Time complexity     : (log x)
    Space complexity    : (1)
"""
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x < 10:
            return x

        harshad_num = x
        total = 0
        while x != 0:
            total += x%10
            x = x//10
        
        return total if (harshad_num%total == 0) else -1
    