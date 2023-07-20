"""
Count All Subarrays With Given Sum

Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""

# Brute Force
def findAllSubarraysWithGivenSum(arr, s):
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            sum_ = sum(arr[i:j+1])
            if sum_ == s:
                cnt += 1
    return cnt


# Better
def findAllSubarraysWithGivenSum(arr, s):
    n = len(arr)
    cnt = 0
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += arr[j] 
            if sum_ == s:
                cnt += 1
    return cnt


# Optimal
def findAllSubarraysWithGivenSum(arr, s):
    from collections import defaultdict 
    hs = defaultdict(int)
    hs[0] = 1
    preSum = 0
    cnt = 0
    for n in arr:
        preSum += n
        remove = preSum - s
        cnt += hs[remove]
        hs[preSum] += 1
    return(cnt) 