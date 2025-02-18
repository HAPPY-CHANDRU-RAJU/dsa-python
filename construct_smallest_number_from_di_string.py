"""
Construct Smallest Number From DI String

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.
A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
    If pattern[i] == 'I', then num[i] < num[i + 1].
    If pattern[i] == 'D', then num[i] > num[i + 1].

Return the lexicographically smallest possible string num that meets the conditions.


Example 1:
Input: pattern = "IIIDIDDD"
Output: "123549876"

Explanation:
    At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
    At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
    Some possible values of num are "245639871", "135749862", and "123849765".
    It can be proven that "123549876" is the smallest possible num that meets the conditions.

Note that "123414321" is not possible because the digit '1' is used more than once.

Example 2:
Input: pattern = "DDD"
Output: "4321"

Explanation:
    Some possible values of num are "9876", "7321", and "8742".
    It can be proven that "4321" is the smallest possible num that meets the conditions.

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.


LINK : https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
"""

# Brute Force
"""
    Time complexity     : (n+1)! * n
    Space complexity    : (n)!
"""
import itertools

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        digits = list(map(str, range(1, n + 2)))  
        all_permutations = itertools.permutations(digits)
        
        def is_valid(permutation):
            for i in range(n):
                if pattern[i] == 'I' and permutation[i] >= permutation[i + 1]:
                    return False
                if pattern[i] == 'D' and permutation[i] <= permutation[i + 1]:
                    return False
            return True
        
        smallest_valid = None
        for perm in all_permutations:
            if is_valid(perm):
                if smallest_valid is None or ''.join(perm) < smallest_valid:
                    smallest_valid = ''.join(perm)
        
        return smallest_valid if smallest_valid else ""


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        if not pattern:
            return ""

        n = len(pattern)
        stack = []
        result = []

        for i in range(n+1):
            stack.append(i+1)

            if i==n or pattern[i] == "I":
                while stack:
                    result.append(str(stack.pop()))
        
        return "".join(result)