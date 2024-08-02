"""
Find Nth Root Of M

You are given two positive integers 'n' and 'm'. 
You have to return the 'nth' root of 'm', i.e. 'm(1/n)'. 
If the 'nth root is not an integer, return -1.

Note:
'nth' root of an integer 'm' is a number, which, when raised to the power 'n', gives 'm' as a result.


Example:
Input: ‘n’ = 3, ‘m’ = 27
Output: 3

Explanation: 
3rd Root of 27 is 3, as (3)^3 equals 27.

LINK : https://www.naukri.com/code360/problems/nth-root-of-m/
"""

# Brute Force
"""
    Time complexity     : (n*m)
    Space complexity    : (1)
"""
def NthRoot(n: int, m: int) -> int:
    for i in range(1, m + 1):
        if i**n == m:
            return i
    return -1


# Optimal
"""
    Time complexity     : (n log m)
    Space complexity    : (log n)
"""
def myPow(x, n):
    if n == 0:
        return 1
    
    if n < 0:
        n = -n
        x = 1/x
    
    ans = myPow(x, n//2)
    if n%2 == 0:
        return ans*ans
    return ans*ans*x

def NthRoot(n: int, m: int) -> int:
    low, high = 0, m
    while low <= high:
        mid = (low+high)//2
        pow_ = myPow(mid, n)
        if pow_ == m:
            return mid
        elif pow_ > m:
            high = mid-1
        else:
            low = mid+1
    return -1