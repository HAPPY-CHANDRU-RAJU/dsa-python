"""
Count Inversion
Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).

What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].
"""

# Brute Force
from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
    count  = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n
    
arr, n = takeInput()
print(getInversions(arr, n))

# Optimal
from os import *
from sys import *
from collections import *
from math import *

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1

    cnt = 0
     
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left+1)
            right += 1

    while left <= mid :
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

    return cnt


def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    
    mid = floor((low+high)/2)
    cnt += mergeSort(arr, low, mid )
    cnt += mergeSort(arr, mid+1, high)
    cnt += merge(arr, low, mid, high)
    return cnt

def getInversions(arr, n) :
    return mergeSort(arr, 0, n-1)

def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

arr, n = takeInput()
print(getInversions(arr, n))

