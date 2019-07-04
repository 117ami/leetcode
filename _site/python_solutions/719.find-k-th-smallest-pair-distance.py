#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (29.26%)
# Total Accepted:    20.2K
# Total Submissions: 69.1K
# Testcase Example:  '[1,3,1]\n1'
#
# Given an integer array, return the k-th smallest distance among all the
# pairs. The distance of a pair (A, B) is defined as the absolute difference
# between A and B.
#
# Example 1:
#
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
#
#
#
# Note:
#
# 2 .
# 0 .
# 1 .
#
#
#


class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        lo, hi, n = 0, nums[-1] - nums[0], len(nums)
        while lo < hi:
            mid, cnt, i, j = (lo + hi) // 2, 0, 0, 0
            while i < n:
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                cnt += j - i - 1
                i += 1

            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        return lo


s = Solution()
nums = [1, 2, 4, 3, 2]
k = 3
print(s.smallestDistancePair(nums, k))
