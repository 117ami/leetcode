#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
# https://leetcode.com/problems/find-and-replace-pattern/description/
#
# algorithms
# Medium (72.39%)
# Total Accepted:    40K
# Total Submissions: 55.3K
# Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
#
# You have a list of words and a pattern, and you want to know which words in
# words matches the pattern.
#
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
#
# (Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.)
#
# Return a list of the words in words that match the given pattern. 
#
# You may return the answer in any order.
#
#
#
#
# Example 1:
#
#
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation,
# since a and b map to the same letter.
#
#
#
# Note:
#
#
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20
#
#
#
#


class Solution:
    def findAndReplacePattern(self, sw, p):
        def imap(w):
            i = 0
            memo = {}
            res = ""
            for c in w:
                if c not in memo:
                    memo[c] = '#' + str(i)
                    i += 1
                res += memo[c]
            return res

        return [e for e in sw if imap(e) == imap(p)]


s = Solution()
ws, p = ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"
print(s.findAndReplacePattern(ws, p))
