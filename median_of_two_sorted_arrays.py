"""
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000

Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000

Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

LINK : https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""

# Brute Force
"""
    Time complexity     : (m+n)
    Space complexity    : (m+n)
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        p1, p2 = m-1, n-1
        p = m+n
        temp = [-1]*p
        p -= 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                temp[p] = nums1[p1]
                p1 -= 1
            else:
                temp[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p1 >= 0:
            temp[p] = nums1[p1]
            p1 -= 1
            p -= 1

        while p2 >= 0:
            temp[p] = nums2[p2]
            p2 -= 1
            p -= 1
        
        p = len(temp)
        if p%2 == 0:
            p = (p//2)-1
            return sum(temp[p:p+2])/2
        return temp[p//2]


# Optimal
"""
    Time complexity     : (log(min(n,m)))
    Space complexity    : (log(min(n,m)))
"""
class Solution:
    def get(self, nums,i):
        if i < 0:
            return -float('inf')
        elif i >= len(nums):
            return float('inf')
        else:
            return nums[i]

    def find_kth_number(self, k, nums1, nums2):
        low, high = 0, len(nums1)-1

        while low <= high:
            mid = (low+high)//2
            if self.get(nums2, k-mid-2) <= nums1[mid] <= self.get(nums2, k-mid-1):
                return nums1[mid]
            elif self.get(nums2, k-mid-2) <= nums1[mid]:
                high = mid-1
            else:
                low = mid+1
        return self.find_kth_number(k, nums2, nums1)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1) + len(nums2)
        k = (n // 2) 
        if n % 2 == 1:
            k += 1
            return self.find_kth_number(k, nums1, nums2)
        else:
            ans1 = self.find_kth_number(k, nums1, nums2)
            ans2 = self.find_kth_number(k + 1, nums1, nums2)
            return (ans1 + ans2) / 2

