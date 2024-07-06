"""
Count Subarrays with Given XOR

Problem statement
Given an array of integers ‘ARR’ and an integer ‘X’, you are supposed to find the number of subarrays of 'ARR' which have bitwise XOR of the elements equal to 'X'.

Note:
An array ‘B’ is a subarray of an array ‘A’ if ‘B’ that can be obtained by deletion of, several elements(possibly none) from the start of ‘A’ and several elements(possibly none) from the end of ‘A’. 

Input:
2
5 8
5 3 8 3 10
3 7
5 2 9
Output:
2
1

Explanation:
In the first test case, the subarray from index 1 to index 3 i.e. {3,8,3} and the subarray from index 2 to index 2 i.e. {8} have bitwise XOR equal to 8.

Input:
2
6 11
10 1 0 3 4 7
5 4
4 3 1 2 4
Output:
3
4

Explanation:
In the second test case, the subarray from index 0 to index 1 i.e. {5,2} has bitwise XOR equal to 7.

Constraints :
1 <= T <= 10
3 <= N <= 5 * 10 ^ 4
0 <= X <= 10 ^ 9
0 <= ARR[i] <= 10 ^ 9
Where ‘T’ denotes the number of test cases, ‘N’ denotes the number of elements in the array, ‘X’ denotes the required subarray XOR and ARR[i] denotes the 'i-th' element of the given array.


LINK : https://www.naukri.com/code360/problems/count-subarrays-with-given-xor
"""

# Brute Force
"""
    Time complexity     : (n^3)
    Space complexity    : (1)
"""
def subarraysXor(arr, x):
    n = len(arr)
    cnt = 0

    for i in range(n):
        for j in range(i, n):
            xor = 0
            for k in range(i, j+1):
                xor = xor ^ arr[k]

            if xor == x:
                cnt += 1
    return cnt 

# Medium 
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
def subarraysXor(arr, x):
    n = len(arr)
    cnt = 0

    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor = xor ^ arr[j]

            if xor == x:
                cnt += 1
    return cnt 

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
def subarraysXor(arr, x):
    xor_freq = {}
    cnt = 0 

    xor = 0 
    n = len(arr)
    for i in range(n):
        xor = xor^arr[i]

        if xor == x:
            cnt += 1

        if (xor^x) in xor_freq:
            cnt += xor_freq[xor^x]
        
        if xor in xor_freq:
            xor_freq[xor] += 1
        else:
            xor_freq[xor] = 1
        
    return cnt
