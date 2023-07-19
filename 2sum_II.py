"""
Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

"""

# Brute Force
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            com = target - numbers[i]
            for j in range(i+1,n):
                if com == numbers[j]:
                    return [i+1, j+1]

# Better
class Solution:
    def binarySearch(self,nums,value):
        low = 0
        high = len(nums)-1
        while high >= low:
            mid = (low+high)//2
            if nums[mid] > value:
                high = mid-1
            elif nums[mid] <  value:
                low = mid+1
            else:
                return mid
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            com = target - numbers[i]
            res = self.binarySearch(numbers[i+1:],com )
            if res >= 0:
                return [i+1, i+res+2]


# Optimal
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left]+numbers[right] < target:
                left += 1
            else:
                right -= 1
        
