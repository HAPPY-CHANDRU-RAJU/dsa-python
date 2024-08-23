"""
Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:
Input: s = "III"
Output: 3

Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58

Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994

Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

LINK : https://leetcode.com/problems/roman-to-integer/description/
"""

# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = { "I" : 1, "X" : 10, "C" : 100, "V" : 5, "L" : 50, "D" : 500, "M" : 1000 }
        
        indx = 0
        n = len(s)
        sum_ = 0
        while indx < n-1:
            sum_ += roman_to_int[s[indx]]
            if s[indx] == "I":
                if s[indx+1] == "V":
                    sum_ += 3
                    indx += 1
                elif s[indx+1] == "X":
                    sum_ += 8
                    indx += 1
            elif s[indx] == "X":
                if s[indx+1] == "L":
                    sum_ += 30
                    indx += 1
                elif s[indx+1] == "C":
                    sum_ += 80
                    indx += 1
            elif s[indx] == "C":
                if s[indx+1] == "D":
                    sum_ += 300
                    indx += 1
                elif s[indx+1] == "M":
                    sum_ += 800
                    indx += 1
            indx += 1
        
        if indx < n:
            sum_ += roman_to_int[s[indx]]
            indx += 1
        
        return sum_


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        """
            Basic Values:
              >  Roman numerals use seven symbols: I (1), V (5), X (10), L (50), C (100), D (500), and M (1000).

            Additive Rule:
              >  Add values as you move left to right. Example: "VI" = 5 + 1 = 6.

            Subtractive Rule:
              >  If a smaller numeral precedes a larger one, subtract it. Example: "IV" = 5 - 1 = 4.

            Order Matters:
              >  Add when a numeral is followed by an equal or smaller one; subtract when followed by a larger one.
        """
        roman_to_int = { "I" : 1, "X" : 10, "C" : 100, "V" : 5, "L" : 50, "D" : 500, "M" : 1000 }
        
        total = 0
        prev_value = 0

        for i in reversed(s):
            value = roman_to_int[i]

            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
        
        return total
