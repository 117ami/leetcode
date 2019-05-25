#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (47.02%)
# Total Accepted:    62.6K
# Total Submissions: 132.9K
# Testcase Example:  '[3,1,5,8]'
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After the
# burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
# Example:
#
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  -->
# []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
#


class Solution:
    def maxCoins(self, nums):
        sz = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for i in range(len(nums))]
        for size in range(1, sz + 1):
            for i in range(1, sz - size + 2):
                j = i + size - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1]
                                   [j] + nums[i - 1] * nums[k] * nums[j + 1])
        # print(dp)
        return int(dp[1][sz])


s = Solution()
nums = [3, 1, 5, 8]
print(s.maxCoins(nums))
