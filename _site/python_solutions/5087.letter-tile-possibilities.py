#
# @lc app=leetcode id=5087 lang=python3
#
# [5087] Letter Tile Possibilities
#
# https://leetcode.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (76.77%)
# Total Accepted:    2K
# Total Submissions: 2.6K
# Testcase Example:  '"AAB"'
#
# You have a set of tiles, where each tile has one letter tiles[i] printed on
# it.  Return the number of possible non-empty sequences of letters you can
# make.
#
#
#
# Example 1:
#
#
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
#
#
#
# Example 2:
#
#
# Input: "AAABBC"
# Output: 188
#
#
#
#
#
# Note:
#
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
#
#
#
import collections
import string


class Solution:
    def dfs(self, cter):
        mus = 0
        for c in string.ascii_uppercase:
            if cter[c] > 0:
                cter[c] -= 1
                mus += 1 + self.dfs(cter)
                cter[c] += 1
        return mus

    def numTilePossibilities(self, tiles):
        c = collections.Counter(tiles)
        return self.dfs(c)


s = Solution()
print(s.numTilePossibilities('AAB'))
