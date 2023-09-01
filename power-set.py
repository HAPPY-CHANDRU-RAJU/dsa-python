"""
Power Set

Given a string S, Find all the possible subsequences of the String in lexicographically-sorted order.

Example 1:

Input : str = "abc"
Output: a ab abc ac b bc c
Explanation : There are 7 subsequences that 
can be formed from abc.
Example 2:

Input: str = "aa"
Output: a a aa
Explanation : There are 3 subsequences that 
can be formed from aa.

"""

##### Optimal #####
#  TC : O(n*2n)
class Solution:
	def AllPossibleStrings(self, s):
	    ans = []
	    def stringUtil(s, n, ind, res):
	        if n == ind:
	            if res != "":
    	            ans.append(res)
	            return 
	        stringUtil(s, len(s), ind+1, res+s[ind])
	        stringUtil(s, len(s), ind+1, res)
	    stringUtil(s, len(s), 0, "")
	    ans.sort()
        return ans
