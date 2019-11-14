#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/
#
# algorithms
# Hard (71.63%)
# Total Accepted:    2.7K
# Total Submissions: 3.7K
# Testcase Example:  '["dog","cat","dad","good"]\n' +'["a","a","c","d","d","d","g","o","o"]\n' +'[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]'
#
# Given a list of words, list of  single letters (might be repeating) and score
# of every character.
# 
# Return the maximum score of any valid set of words formed by using the given
# letters (words[i] cannot be used two or more times).
# 
# It is not necessary to use all characters in letters and each letter can only
# be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0],
# score[1], ... , score[25] respectively.
# 
# 
# Example 1:
# 
# 
# Input: words = ["dog","cat","dad","good"], letters =
# ["a","a","c","d","d","d","g","o","o"], score =
# [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with
# a score of 23.
# Words "dad" and "dog" only get a score of 21.
# 
# Example 2:
# 
# 
# Input: words = ["xxxz","ax","bx","cx"], letters =
# ["z","a","b","c","x","x","x"], score =
# [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# Output: 27
# Explanation:
# Score  a=4, b=4, c=4, x=5, z=10
# Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5)
# with a score of 27.
# Word "xxxz" only get a score of 25.
# 
# Example 3:
# 
# 
# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score =
# [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0
# Explanation:
# Letter "e" can only be used once.
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 14
# 1 <= words[i].length <= 15
# 1 <= letters.length <= 100
# letters[i].length == 1
# score.length == 26
# 0 <= score[i] <= 10
# words[i], letters[i] contains only lower case English letters.

import collections, copy

class Solution:
    def maxScoreWords(self, words, letters, score):
        cter = collections.Counter(letters)
        return self.dfs(words, cter, score, 0)


    def dfs(self, words, cter, score, i):
        """i for i-th word that is choose from words
        """
        if i >= len(words): return 0
        next_gain = self.dfs(words, cter, score, i + 1)
        cur_gain = 0
        n_cter = copy.copy(cter)

        for c in words[i]:
            if n_cter[c] > 0: 
                n_cter[c] -= 1
                cur_gain += score[ord(c) - 97]
            else:
                return next_gain

        return max(next_gain, cur_gain + self.dfs(words, n_cter, score, i + 1))


s = Solution()
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
print(s.maxScoreWords(words, letters, score))

print(ord('a'))