"""
Remove Duplicates from Sorted Array

"""

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

        
##### Better  #####

##### Optimal #####

