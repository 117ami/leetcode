# https://leetcode.com/problems/valid-perfect-square
# Easy (Difficulty)

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.
# Example 1:
# Example 2:
# Input: 16
# Output: true
# 
# Input: 14
# Output: false
# 
# xxxxxxxxxx
# class Solution {
# public:
#     bool isPerfectSquare(int num) {
#         
#     }
# };
# class Solution {
# public:
#     bool isPerfectSquare(int num) {
#         
#     }
# };

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2 
            if mid * mid < num:
                lo = mid + 1
            else:
                hi = mid 
        
        return lo * lo == num 


# for i in range(1, 101):
#     if Solution().isPerfectSquare(i):
#         print(i)
