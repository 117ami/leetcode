#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (39.19%)
# Total Accepted:    191.5K
# Total Submissions: 486.3K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.dfs(0, target, [], ans, candidates)
        return ans 


    def dfs(self, i, target, combs, ans, candidates):
    	if target < 0: return 
    	if target == 0:
    		ans.append(combs)
    		return 

    	for j in range(i, len(candidates)):
    		c = candidates[j]
    		if j > i and candidates[j - 1] == c: continue 
    		if target < c: break 
    		self.dfs(j + 1, target - c, combs + [c], ans, candidates)


candidates =[10,1,2,7,6,1,5]
target =8
candidates=[2,5,2,1,2]
target=5
print(Solution().combinationSum2(candidates, target))


