"""
Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

LINK : https://leetcode.com/problems/add-binary/description/
"""

# in-built Function
"""
    Time complexity     : (1)
    Space complexity    : (1)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_a = int(a, 2)
        bin_b = int(b, 2)

        total = bin_a + bin_b

        return bin(total)[2:]

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for i in range(max_len-1, -1, -1):
            curr_a = int(a[i])
            curr_b = int(b[i])

            total = curr_a + curr_b + carry
            carry = total//2
            result.append(str(total%2))

        if carry:
            result.append("1")
        
        return "".join(result[::-1])