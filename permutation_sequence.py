"""
Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123" 

Constraints:

1 <= n <= 9
1 <= k <= n!

LINK : https://leetcode.com/problems/permutation-sequence/description/
"""

# Brute Force
"""
    Time complexity     : (n!)
    Space complexity    : (n!)
"""
from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        str_ = "".join(list(map(str,range(1,n+1))))
        kthPermutation = list(permutations(str_))[k-1]
        return "".join(kthPermutation)


# Medium Effort
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        number = []
        for i in range(1, n):
            number.append(i)
            fact = fact*i
        number.append(n)

        ans = ""
        k = k-1
        for _ in range(n):
            index = k//int(fact)
            ans += str(number.pop(index))     # worst case is (n) otherwise is (1)

            k = k%fact
            fact = fact//len(number)
        return ans
    

# Optimal
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [i for i in range(1, n+1)]
        k -= 1

        res = []
        for i in range(n, 0, -1):
            index, k = divmod(k, math.factorial(i-1))
            res.append(str(numbers.pop(index)))
            
        return "".join(res)