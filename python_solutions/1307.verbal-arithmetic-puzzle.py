from itertools import permutations
from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=1307 lang=python3
#
# [1307] Verbal Arithmetic Puzzle
#
# https://leetcode.com/problems/verbal-arithmetic-puzzle/description/
#
# algorithms
# Hard (28.26%)
# Total Accepted:    1.1K
# Total Submissions: 3.9K
# Testcase Example:  '["SEND","MORE"]\n"MONEY"'
#
# Given an equation, represented by words on left side and the result on right
# side.
#
# You need to check if the equation is solvable under the following
# rules:
#
#
# Each character is decoded as one digit (0 - 9).
# Every pair of different characters they must map to different digits.
# Each words[i] and result are decoded as one number without leading zeros.
# Sum of numbers on left side (words) will equal to the number on right side
# (result). 
#
#
# Return True if the equation is solvable otherwise return False.
#
#
# Example 1:
#
#
# Input: words = ["SEND","MORE"], result = "MONEY"
# Output: true
# Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8,
# 'Y'->'2'
# Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
#
# Example 2:
#
#
# Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
# Output: true
# Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1,
# 'W'->'3', 'Y'->4
# Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 =
# 138214
#
# Example 3:
#
#
# Input: words = ["THIS","IS","TOO"], result = "FUNNY"
# Output: true
#
#
# Example 4:
#
#
# Input: words = ["LEET","CODE"], result = "POINT"
# Output: false
#
#
#
# Constraints:
#
#
# 2 <= words.length <= 5
# 1 <= words[i].length, results.length <= 7
# words[i], result contains only upper case English letters.
# Number of different characters used on the expression is at most 10.
#
#


def carproduct(la, lb): return sum(i * j for i, j in zip(la, lb))


class Solution:
    def isSolvable(self, words, result):
        coef = defaultdict(int)
        for sign, word in list(zip([1] * len(words), words)) + [(-1, result)]:
            for i, c in enumerate(reversed(word)):
                coef[c] += sign * pow(10, i)
                if coef[c] == 0:
                    del coef[c]

        hundreds = [n for n in coef.values() if abs(n) % 100 > 0]
        lefts = [n for n in coef.values() if n not in hundreds]

        for p in permutations(range(10), len(hundreds)):
            cp = carproduct(hundreds, p)
            if abs(cp) % 100 > 0:continue
            left_digits = [d for d in range(10) if d not in p]
            for np in permutations(left_digits, len(lefts)):
                if cp + carproduct(lefts, np) == 0:
                    return true
        return false


words, result = ["THIS", "IS", "TOO"], "FUNNY"
# words, result = ["SEND", "MORE"], "MONEY"
# words, result = ["SIX","SEVEN","SEVEN"], "TWENTY"
# words, result = ["LEET", "CODE"], "POINT"
# words, result = ["A", "B", "C", "D", "E", "F", "G", "H", "I"], "Z"
sol = Solution()
print(sol.isSolvable(words, result))
target = (10, 2, -1)
target = (10, -10, -100, 1111)
target = (1, 2, -1)
for i in permutations(range(10), 3):
    if carproduct(target, i) == 0:
        pass
        # print(i)
