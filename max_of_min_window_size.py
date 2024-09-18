"""
Maximum of minimum for every window size

You are given an array of ‘N’ integers, you need to find the maximum of minimum for every window size. The size of the window should vary from 1 to ‘N’ only.

Sample Input 1:
2
4
1 2 3 4
5
3 3 4 2 4    

Sample Output 1:
4 3 2 1
4 3 3 2 2

Explanation for sample input 1:
Test case 1:
    Minimums of window size 1 = min(1), min(2), min(3), min(4) = 1,2,3,4
    Maximum among (1,2,3,4)  is 4

    Minimums of window size 2 = min(1,2), min(2,3),   min(3,4) = 1,2,3
    Maximum among (1,2,3) is 3

    Minimums of window size 3 = min(1,2,3), min(2,3,4) = 1,2
    Maximum among (1,2) is 2

    Minimums of window size 4 = min(1,2,3,4) = 1
    Maximum among them is 1

The output array should be [4,3,2,1].

Test case 2:
    Minimums of window size 1 = min(3), min(3), min(4), min(2), min(4) = 3, 3, 4, 2, 4
    Maximum among (3, 3, 4, 2, 4) is 4

    Minimums of window size 2 = min(3,3), min(3,4), min(4,2), min(2,4) = 3, 3, 2, 2
    Maximum among (3, 3, 2, 2) is 3

    Minimums of window size 3 = min(3,3,4), min(3,4,2), min(4,2,4) = 3, 2, 2
    Maximum among (3, 2, 2) is 3

    Minimums of window size 4 = min(3,3,4,2), min(3,4,2,4) = 2, 2
    Maximum among (2, 2) is 2

    Minimums of window size 4 = min(3,3,4,2,4) = 2
    Maximum among them is 2

The output array should be [4,3,3,2,2].

Sample Input 2:
2
5 
45 -2 42 5 -11 
6 
-2 12 -1 1 20 1 

Sample Output 2:
 45 5 -2 -2 -11
 20 1  1 -1 -1 -2

Constraints:
1 <= T <= 100
1 <= N <= 10 ^ 4 
-10 ^ 9 <= ARR[i] <= 10 ^ 9

Where ‘T’ is the number of test cases, ‘N’ is the size of the array and ‘ARR[i]’ is the size of the array elements.

Time Limit: 1 sec

LINK : https://www.naukri.com/code360/problems/max-of-min_982935
"""

# Brute Force
"""
    Time complexity     : (n)
    Space complexity    : (n^3)
"""

def maxMinWindow(arr, n):
    result = []
    for gap in range(1, n+1):
        max_window = -float('inf')
        for i in range(0, n-gap+1):
            max_window = max(max_window, min(arr[i:i+gap]))
        result.append(max_window)
    return result


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
from os import *
from sys import *
from collections import *
from math import *

def maxMinWindow(arr, n):
    next_smaller = [n]*n
    prev_smaller = [-1]*n

    # Prev smaller
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)
    
    # Next smaller
    stack = []
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            next_smaller[i] = stack[-1]
        stack.append(i)
    
    # Result
    result = [-float('inf')]*n
    for i in range(n):
        length = next_smaller[i] - prev_smaller[i] - 1
        result[length-1] = max(result[length-1], arr[i])

    for i in range(n-2, -1, -1):
        result[i] = max(result[i], result[i+1])
    
    return result
    

