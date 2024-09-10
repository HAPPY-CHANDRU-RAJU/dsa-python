"""
LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
    LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
The functions get and put must each run in O(1) average time complexity.


Example 1:
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

1 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.

LINK : https://leetcode.com/problems/lfu-cache/description/
"""

# Optimal
"""
    Time complexity     : (1)
    Space complexity    : (n)
"""
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Key to (value, frequency)
        self.freq_count = {}  # Frequency to number of keys with that frequency
        self.min_freq = 0  # Minimum frequency of the cache

    def update_key(self, key):
        value, freq = self.cache[key]
        self.cache[key] = [value, freq+1]

        self.freq_count[freq] -= 1
        if self.freq_count[freq] == 0:
            del self.freq_count[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        if freq+1 not in self.freq_count:
            self.freq_count[freq+1] = 0
        self.freq_count[freq+1] += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.update_key(key)
        return self.cache[key][0]
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 

        if key in self.cache:
            self.cache[key] = [value,  self.cache[key][1]]
            self.update_key(key)
        else:
            if len(self.cache) >= self.capacity:
                lfu_key = None
                for k, (v, f) in self.cache.items():
                    if self.min_freq == f:
                        lfu_key = k
                        break
                
                if lfu_key is not None:
                    del self.cache[lfu_key]
                    self.freq_count[self.min_freq] -= 1
                    if self.freq_count[self.min_freq] == 0:
                        del self.freq_count[self.min_freq]
            
            self.cache[key] = [value, 1]
            self.min_freq = 1
            if 1 not in self.freq_count:
                self.freq_count[1] = 0
            self.freq_count[1] += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)