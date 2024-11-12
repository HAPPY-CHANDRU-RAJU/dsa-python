"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

LINK : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2
"""

# Optimal
"""
    Time Complexity     :   (4^n) — We still generate all possible combinations, which requires O(4^n) time.
    Space Complexity    :   (n * 4^n ) — Space is required to store all combinations, and each combination has length n.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def letter_combinations(index, current):
            if index == len(digits):
                result.append(current)
                return
            
            for char in keypad[digits[index]]:
                letter_combinations(index + 1, current + char)
        
        letter_combinations(0, "")
        return result

###################### OR ######################

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        queue = deque([""])
        for digit in digits:
            letters = keypad[digit]

            queue_length = len(queue)
            for _ in range(queue_length):
                combination = queue.popleft()

                for letter in letters:
                    queue.append(combination+letter)
        
        return list(queue)
