"""
Subset Sums


Given a list arr of N integers, print sums of all subsets in it.

Example 1:

Input:
N = 2
arr[] = {2, 3}

Output:
0 2 3 5

Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.
"""

#####  Brute Force  #####
"""
    Powerset problem
"""

##### Optimal #####
def subsetSums(self, arr, N):
    ans = []
    def subsetSumUtil(arr, n, ind, sum_):
        if n == ind:
            ans.append(sum_)
            return
        subsetSumUtil(arr, n, ind+1, sum_+arr[ind])
        subsetSumUtil(arr, n, ind+1, sum_)
    subsetSumUtil(arr, len(arr), 0, 0)
    ans.sort()
    return ans
