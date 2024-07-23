"""
Subset Sums

Given a list arr of n integers, return sums of all subsets in it. Output sums can be printed in any order.

Example 1:
Input:
n = 2
arr[] = {2, 3}
Output:
0 2 3 5

Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.

Example 2:
Input:
n = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8

Your Task:  
You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes a list/vector and an integer n as an input parameter and returns the list/vector of all the subset sums.

Expected Time Complexity: O(2n)
Expected Auxiliary Space: O(2n)

Constraints:
1 <= n <= 15
0 <= arr[i] <= 104

LINK : https://www.geeksforgeeks.org/problems/subset-sums
"""

# Brute Force
"""
    Time complexity     : (n⋅ 2^n)
    Space complexity    : (n⋅ 2^n)
"""
from itertools import combinations

def subsetSums(self, arr, n):
    res = [0]
    for i in range(1, n+1):
        for itr in list(combinations(arr, i)):
            res.append(sum(itr)) 
    return res
    

# Optimal
"""
    Time complexity     : (2^n)
    Space complexity    : (n + 2^n)
"""
def subsetSums(self, arr, N):
    ans = []
    def subsetSumUtil(arr, n, ind, sum_):
        if n == ind:
            ans.append(sum_)
            return
        subsetSumUtil(arr, n, ind+1, sum_+arr[ind])
        subsetSumUtil(arr, n, ind+1, sum_)
    subsetSumUtil(arr, len(arr), 0, 0)
    return ans

################   or    ################

def subsetSums(self, arr, n):
    res = []
    def backtrack(start, curr_sum):
        res.append(curr_sum)
        for i in range(start, n):
            backtrack(i+1, arr[i]+curr_sum)
    backtrack(0, 0)
    return res