"""
Find the Majority Element that occurs more than N/3 times
Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/3 times in the given array. You may consider that such an element always exists in the array.
"""

# Better
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count_ = Counter(nums)

        majority = len(nums)//3
        for ele , c in count_.items():
            if c > majority:
                return ele

# Optimal
def majorityElement(v: [int]) -> [int]:
    n = len(v)
    cnt2, cnt1 = 0, 0
    el1, el2 = None, None

    for i in range(n):
        if cnt1 == 0 and el2 != v[i] :
            cnt1 = 1
            el1 = v[i]
        elif cnt2 == 0 and el1 != v[i]:
            cnt2 = 1
            el2 = v[i]
        elif v[i] == el1:
            cnt1 += 1
        elif v[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = []
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if v[i] == el1:
            cnt1 += 1
        if v[i] == el2:
            cnt2 += 1

    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)

    return ls
