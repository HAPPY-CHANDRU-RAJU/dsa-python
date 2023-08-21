"""
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

##### Better  #####
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = (len(nums1)+len(nums2))
        med = [(n//2)-1, (n//2)] if (n%2 == 0) else [n//2]
        nums = nums1+nums2
        nums.sort()
        if len(med) == 1:
            return nums[med[0]]
        else:
            return (nums[med[0]]+nums[med[1]])/2
        

##### Optimal #####

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get(nums, i):
            if i<0:
                return -float('inf')        
            elif i>=len(nums):
                return float('inf')
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
        
        n = (len(nums1)+len(nums2))
        if n%2 == 1 :
            k = (n//2)+1
            return find_kth_number(k, nums1, nums2)
        else:
            k = (n//2)
            ans1 = find_kth_number(k, nums1, nums2)
            ans2 = find_kth_number(k+1, nums1, nums2)
            return (ans1+ans2)/2

