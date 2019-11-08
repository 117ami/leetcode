#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#
# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (49.83%)
# Total Accepted:    4.4K
# Total Submissions: 8.5K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# Given an array of integers nums and an integer k. A subarray is called nice
# if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and
# [1,2,1,1].
#
#
# Example 2:
#
#
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.
#
#
# Example 3:
#
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
#
#
#


class Solution:
    def numberOfSubarrays(self, nums, k):
        def atMostK(k):
            res = i = 0
            for j in range(len(nums)):
                k -= nums[j] % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                res += j - i + 1
            return res
        return atMostK(k) - atMostK(k - 1)


s = Solution()
nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
print(s.numberOfSubarrays(nums, k))
