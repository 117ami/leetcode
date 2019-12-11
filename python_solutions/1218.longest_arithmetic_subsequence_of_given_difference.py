# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference
# Medium (Difficulty)

# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
#  
# Example 1:
# Example 2:
# Example 3:
#  
# Constraints:
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# Explanation: The longest arithmetic subsequence is any single element.
#
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
# Explanation: The longest arithmetic subsequence is [7,5,3,1].
#
# xxxxxxxxxx
# class Solution {
# public:
#     int longestSubsequence(vector<int>& arr, int difference) {
#         
#     }
# };


class Solution:
    def longestSubsequence(self, arr, d):
        seen = {1e5: 0}
        for n in arr:
            seen[n] = seen.get(n - d, 0) + 1
        return max(seen.values())


arr, d = [1, 5, 7, 8, 5, 3, 4, 2, 1], -2
# arr, d = [1,2,3,4], 1
# arr, d = [1, 5, 7, 10, 8, 9, 7, 7, 5, 7, 6, 5, 3, 4, 2, 1, 0], -2
# arr, d = [], 0
print(Solution().longestSubsequence(arr, d))
