"""
Compare Version Numbers

Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1

Explanation:
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.


Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0

Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".


Example 3:
Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0

Explanation:
version1 has less revisions, which means every missing revision are treated as "0".

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.

LINK : https://leetcode.com/problems/compare-version-numbers/
"""

# Brute Force
"""
    Time complexity     : (max(n, m))
    Space complexity    : (L1 + L2)
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if not version1 or not version2 or version1 == version2:
            return 0
        
        v1 = version1.split(".")
        v2 = version2.split(".")

        if len(v1) != len(v2):
            max_len = max( len(v1), len(v2) )
            if len(v1) == max_len:
                v2.extend(["0"]*(max_len-len(v2)))
            else:
                v1.extend(["0"]*(max_len-len(v1)))

        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            if int(v1[i]) > int(v2[j]):
                return 1
            elif int(v1[i]) < int(v2[j]):
                return -1
            i += 1
            j += 1
    
        return 0

# Medium 
"""
    Time complexity     : (max(n, m))
    Space complexity    : (L1 + L2)
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        m1 = min(len(version1), len(version2))
        for i in range(m1):
            v1 = int(version1[i])
            v2 = int(version2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        version = version1 if len(version1) - m1 > 0 else version2
        v = 1 if len(version1) - m1 > 0 else 2

        for i in range(m1, len(version)):
            if int(version[i]) > 0:
                return 1 if v == 1 else -1
        return 0
