"""
Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

LINK : https://leetcode.com/problems/find-median-from-data-stream/description/
"""

# Brute Force - Array
"""
    Time complexity     : O(n log n) (insertion), O(1) (find median)
    Space complexity    : O(n)
"""
class MedianFinder:
    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.length += 1

    def findMedian(self) -> float:
        med = self.length//2
        if self.length % 2 == 0:
            return (self.arr[med-1] + self.arr[med]) / 2
        else:
            return self.arr[med]

# Medium Effort - Binary Search Tree
"""
    Time complexity     : O(n) (insertion, worst-case), O(log n) (insertion, avg-case), O(n) (find median)
    Space complexity    : O(n)
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if not root:
        return TreeNode(value)

    if root.data < value:
        root.left = insert(root.left, value)
    if root.data >= value:
        root.right = insert(root.right, value)

    return root

class MedianFinder:
    def __init__(self):
        self.root = None
        self.length = 0

    def addNum(self, num: int) -> None:
        self.root = insert(self.root, num)
        self.length += 1
    
    def inorder_traversal(self, node, arr):
        if not node:
            return
        
        self.inorder_traversal(node.left, arr)
        arr.append(node.data)
        self.inorder_traversal(node.right, arr)

    def findMedian(self) -> float:
        med = self.length//2
        arr = []

        self.inorder_traversal(self.root, arr)

        if self.length % 2 == 0:
            return (arr[med-1] + arr[med]) / 2
        else:
            return arr[med]


# Optimal
"""
    Time complexity     : O(log n) (insertion), O(1) (find median)
    Space complexity    : O(n)
"""
class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))

        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        
        return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()