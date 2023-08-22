"""
K-th element of two sorted Arrays

Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. The task is to find the element that would be at the kth position of the final sorted array.
 
Example 1:
Input:
arr1[] = {2, 3, 6, 7, 9}
arr2[] = {1, 4, 8, 10}
k = 5

Output:
6

Explanation:
The final sorted array would be - 1, 2, 3, 4, 6, 7, 8, 9, 10
The 5th element of this array is 6.

"""

##### Better  #####
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        nums = arr1+arr2
        nums.sort()
        return nums[k-1]

##### Optimal #####
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        
        def get(nums, i):
            if i >= len(nums):
                return float('inf')
            elif i < 0:
                return -float('inf')
            else:
                return nums[i]
        
        def find_kth_number(k, nums1, nums2): 
            low, high = 0, len(nums1)-1
            while low <= high:
                median = (low+high) // 2
                if get(nums2, k-median-2) <= nums1[median] <= get(nums2, k-median-1):
                    return nums1[median]
                elif get(nums2, k-median-2) <= nums1[median]:
                    high = median-1
                else:
                    low = median+1
            return  find_kth_number(k, nums2, nums1)
        
        return find_kth_number(k, arr1, arr2)
        
