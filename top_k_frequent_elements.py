"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

LINK : https://leetcode.com/problems/top-k-frequent-elements/description/
"""

# Brute Force
"""
    Time complexity     : ( n log n)
    Space complexity    : (n)
"""
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_num = Counter(nums)
        return [ num for num, _ in heapq.nlargest(k, freq_num.items(), key=lambda x: x[1]) ]

# Medium Effort
"""
    Time complexity     : (k log n)
    Space complexity    : (n)
"""
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [ num for num, _ in Counter(nums).most_common(k) ]


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_num = Counter(nums)
        bucket = defaultdict(list)

        # Bucket Sort
        for num, freq in freq_num.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(nums), 0, -1):
            if i in bucket:
                result.extend(bucket[i])
                if len(result) == k:
                    return result[:k]
        