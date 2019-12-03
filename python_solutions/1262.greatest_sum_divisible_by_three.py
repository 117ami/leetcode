# https://leetcode.com/problems/greatest-sum-divisible-by-three
# Medium (Difficulty)

# Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.
#  
# Example 1:
# Example 2:
# Example 3:
#  
# Constraints:
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
#
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
#
# xxxxxxxxxx
# class Solution {
# public:
#     int maxSumDivThree(vector<int>& nums) {
#         
#     }
# };


class Solution:
    def maxSumDivThree(self, nums):
        rem = sum(nums) % 3
        if rem == 0:
            return sum(nums)

        a1 = sorted(n for n in nums if n % 3 == 1)
        a2 = sorted(n for n in nums if n % 3 == 2)

        if rem == 1:
            if len(a2) < 2:
                return sum(nums) - a1[0]
            else:
                return sum(nums) - min(a1[0], a2[0] + a2[1])
        else:
            if len(a1) < 2:
                return sum(nums) - a2[0]
            else:
                return sum(nums) - min(a2[0], a1[0] + a1[1])


nums = [3, 6, 5, 1, 8]
nums = [1, 2, 3, 4, 4]
print(Solution().maxSumDivThree(nums))
