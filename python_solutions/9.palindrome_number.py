# https://leetcode.com/problems/palindrome-number
# Easy (Difficulty)

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Example 1:
# Example 2:
# Example 3:
# Follow up:
# Coud you solve it without converting the integer to a string?
# Input: 121
# Output: true
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# xxxxxxxxxx
# class Solution {
# public:
#     bool isPalindrome(int x) {
#         
#     }
# };

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False 
        y, t = 0, x
        while t > 0:
            y = y * 10 + t % 10
            t //= 10
        return y == x

print(Solution().isPalindrome(0))