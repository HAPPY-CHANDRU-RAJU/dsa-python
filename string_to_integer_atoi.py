"""
String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:
    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
    Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^


Example 2:
Input: s = " -042"
Output: -42

Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^


Example 3:
Input: s = "1337c0d3"
Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^


Example 4:
Input: s = "0-1"
Output: 0

Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^


Example 5:
Input: s = "words and 987"
Output: 0

Explanation:
Reading stops at the first non-digit character 'w'.

Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

LINK : https://leetcode.com/problems/string-to-integer-atoi/description/
"""

# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -(2**31)
        INT_MAX = (2**31)-1

        signs = ["-", "+"]

        s = s.strip()
        if not s:
            return 0
        
        if s[0] in signs or s[0].isdigit():
            result = ""
            indx = 0
            for char in s.split(" ")[0]:
                if char.isdigit() or ( indx == 0 and  char in signs):
                    indx += 1
                    result += char 
                else:
                    break
            if result :   
                if ( len(result) == 1 and result in signs):
                    return 0
                result = int(result[1:]) if result[0] in ["+"] else int(result)
                if result > INT_MAX:
                    return INT_MAX
                elif result < INT_MIN:
                    return INT_MIN
                return result

        return 0



# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -(2**31)
        INT_MAX = (2**31)-1

        s = s.strip()
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 +int(s[i])
            i += 1
        
        result *= sign
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN

        return result
