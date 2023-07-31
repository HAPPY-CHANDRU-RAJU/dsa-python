"""
Remove Duplicates from Sorted Array
"""

##### Better  #####
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 :
            return 0
        i = 0
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1


#####  Brute Force  #####
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_ = list()
        for i in nums:
            if i not in set_:
                set_.append(i)
        k = len(set_)
        for i in range(k):
            nums[i] = set_[i]
        return k

        


