# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
# Medium (Difficulty)

# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
# Return the maximum possible length of s.
#  
# Example 1:
# Example 2:
# Example 3:
#  
# Constraints:
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
# Maximum length is 4.
#
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
#
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
#
# xxxxxxxxxx
# class Solution {
# public:
#     int maxLength(vector<string>& arr) {
#         
#     }
# };

class Solution:
    def maxLength(self, arr):
        dp = [set()]
        ans = 0
        for s in arr:
            if len(set(s)) < len(s):
                continue
            s = set(s)
            for c in dp[:]:
                if s & c:
                    continue
                dp.append(s | c)
                ans = max(ans, len(dp[-1]))

        return ans 


arr = ["cha", "r", "act", "ers"]
print(Solution().maxLength(arr))
