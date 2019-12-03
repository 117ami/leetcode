# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
# Hard (Difficulty)

# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).
# Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.
# Since the answer may be too large, return it modulo 10^9 + 7.
#  
# Example 1:
# Example 2:
# Example 3:
#  
# Constraints:
# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
# 
# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
# 
# Input: steps = 4, arrLen = 2
# Output: 8
# 
# xxxxxxxxxx
# class Solution {
# public:
#     int numWays(int steps, int arrLen) {
#         
#     }
# };

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        sz = min(steps // 2 + 1, arrLen) + 2
        pre, cur = [0] * sz, [0] * sz 
        pre[1] = 1
        
        while steps > 0:
            for i in range(1, sz - 1):
                cur[i] = (pre[i] + pre[i-1] + pre[i+1]) % 1000000007
            pre, cur = cur, pre
            steps -= 1
        return pre[1]


print(Solution().numWays(4, 2))        
            