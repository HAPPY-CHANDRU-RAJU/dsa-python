"""
Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example :

Input: n = 3, k = 3
Output: "213"

"""

##### Optimal #####

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact  = 1
        number = []
        for i in range(1,n):
            fact = fact*i
            number.append(i)
        number.append(n)
        ans = ""
        k = k-1
        while(True):
            ans += str(number[k//int(fact)])
            number.pop(k//int(fact))
            if len(number) == 0:
                break
            k = k%fact
            fact = fact//len(number)
        return ans