"""
subarray-with-given-xor
 
Given an array of integers A and an integer B.
Find the total number of subarrays having bitwise XOR of all elements equals to B.
"""

# Brute Force
def solve(arr, s):
    n = len(arr)
    cnt = 0
    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor ^= arr[j] 
            if xor == s:
                cnt += 1
    return cnt


# Optimal
class Solution:
    def solve(self, A, B):
        from collections import defaultdict
        hs=defaultdict(bool)
        hs[0]=1
        count=0
        curSum=0
        for i in A:
            curSum^=i
            remove = curSum^B
            count+=hs[remove]
            hs[curSum]+=1
        return(count)