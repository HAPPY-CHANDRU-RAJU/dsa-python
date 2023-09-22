"""
Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""

#####  Brute Force  #####
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = [-1] * len(nums1)
        for x in range(len(nums1)):
            num = nums1[x]
            for i in range(len(nums2)):
                if nums2[i] == num:
                    for j in range(i+1, len(nums2)):
                        if num < nums2[j]:
                            nge[x] = nums2[j]
                            break
        return nge

##### Optimal #####
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = [-1] * len(nums1)

        index_dict = {}
        for idx, ele in enumerate(nums2):
            index_dict[ele] = idx


        def next_greater(start, nums):
            for i in range(start+1, len(nums)):
                if nums[i] > nums[start]:
                    return nums[i]
            return -1

        for indx in range(len(nums1)):
            if nums1[indx] in index_dict:
                nge[indx] = next_greater(index_dict[nums1[indx]], nums2)

        return nge
