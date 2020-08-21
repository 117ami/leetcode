from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007
#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (34.92%)
# Total Accepted:    472.8K
# Total Submissions: 1.4M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
# Example:
#
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
#
# Constraints:
#
#
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
#


class Solution:
	def dfs(self, board, i, j, word, seen):
		if len(word) == 0:
			return True
		if i >= len(board) or i < 0 or j < 0 or j >= len(
				board[0]) or word[0] != board[i][j] or seen[i][j]:
			return False
		_char = board[i][j]
		board[i][j] = '#'
		seen[i][j] = 1 
		if self.dfs(board, i + 1, j, word[1:], seen) \
				or self.dfs(board, i, j + 1, word[1:], seen) \
		or self.dfs(board, i - 1, j, word[1:], seen) or \
			self.dfs(board, i, j-1, word[1:], seen):
			return True

		board[i][j] = _char
		seen[i][j] = 0
		return False

	def exist(self, board: List[List[str]], word: str) -> bool:
		if not board:
			return false
		seen = [[0] * len(board[0]) for _ in range(len(board))]
		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.dfs(board, i, j, word, seen):
					return true
		return false


sol = Solution()
board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
print(sol.exist(board, "SEE"))
