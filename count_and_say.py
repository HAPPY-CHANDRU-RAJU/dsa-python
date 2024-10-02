"""
Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
Given a positive integer n, return the nth element of the count-and-say sequence.

Example 1:
Input: n = 4
Output: "1211"

Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"

Example 2:
Input: n = 1
Output: "1"

Explanation:
This is the base case.


Constraints:
1 <= n <= 30
 

Follow up: Could you solve it iteratively?

LINK : https://leetcode.com/problems/count-and-say/description/
"""

# Medium 
"""
    Time complexity     : (2^n)
    Space complexity    : (2^n)
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        res = self.countAndSay(n-1)

        result = ''
        stack = []

        count  = 0
        i = 0
        while i < len(res):
            if stack and stack[-1] == res[i]:
                i += 1
                count += 1
            elif stack:
                result += f"{count}{stack.pop()}"
                count = 0
            else:
                stack.append(res[i])
                i += 1
                count += 1
        
        if stack:
            result += f"{count}{stack.pop()}"

        return result

###################### OR ######################

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        res = self.countAndSay(n-1)

        result = ''

        count  = 1
        for i in range(1, len(res)):
            if res[i] == res[i-1]:
                count += 1
            else:
                result += f"{count}{res[i-1]}"
                count = 1

        result += f"{count}{res[-1]}"
        return result


# Optimal
"""
    Time complexity     : (2^n)
    Space complexity    : (n)
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        curr_sequence = "1"

        for _ in range(1, n):
            next_sequence = ""
            count  = 1
            for i in range(1, len(curr_sequence)):
                if curr_sequence[i] == curr_sequence[i-1]:
                    count += 1
                else:
                    next_sequence += f"{count}{curr_sequence[i-1]}"
                    count = 1

            next_sequence += f"{count}{curr_sequence[-1]}"
            curr_sequence = next_sequence
        return curr_sequence


