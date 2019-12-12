# https://leetcode.com/problems/super-palindromes
# Hard (Difficulty)

# Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.
# Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].
#  
# Example 1:
#  
# Note:
#  
# Input: L = "4", R = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
# xxxxxxxxxx
# class Solution {
# public:
#     int superpalindromesInRange(string L, string R) {
#         
#     }
# };
import itertools
import functools


class Solution:
    def superpalindromesInRange(self, l, r):
        lb, rb = int(l) ** 0.5, int(r) ** 0.5
        ans = 1 if lb <= 3 <= rb  else 0
        for e in itertools.product('012', repeat=5):
            left = str(int(''.join(e)))
            if left == '0':
                continue
            n = 2 * sum(int(i)**2 for i in e)
            if n < 10 and lb <= int(left + left[::-1]) <= rb:
                ans += 1
            n -= int(e[-1]) ** 2
            if n < 10 and lb <= int(left + left[-2::-1]) <= rb:
                ans += 1
        return ans


l, r = "1020762146323", "142246798855636"
l, r = "38455498359", "999999999999999999"
l, r = '4', '1000'
print(Solution().superpalindromesInRange(l, r))
