#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#
# https://leetcode.com/problems/count-vowels-permutation/description/
#
# algorithms
# Hard (51.18%)
# Total Accepted:    5.7K
# Total Submissions: 11.1K
# Testcase Example:  '1'
#
# Given an integer n, your task is to count how many strings of length n can be
# formed under the following rules:
#
#
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
#
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
#
#
# Example 2:
#
#
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
# "iu", "oi", "ou" and "ua".
#
#
# Example 3: 
#
#
# Input: n = 5
# Output: 68
#
#
# Constraints:
#
#
# 1 <= n <= 2 * 10^4
#
#
#


class Solution:
    cache = [[1, 1, 1, 1, 1]]
    MOD = pow(10, 9) + 7

    def countVowelPermutation(self, n: int) -> int:
        if n <= len(Solution.cache):
            return sum(Solution.cache[n - 1]) % Solution.MOD
        for _ in range(len(Solution.cache), n):
            a, e, i, o, u = Solution.cache[-1]
            Solution.cache.append([e + i + u, a + i, e + o, i, i + o])
        return sum(Solution.cache[n - 1]) % Solution.MOD


argn = 158
s = Solution()
print(s.countVowelPermutation(argn))
print(s.countVowelPermutation(3))
# print(s.countVowelPermutation(argn - 100))

# exit(0)


# def valid(s):
#     for i in range(len(s) - 1):
#         if s[i] == 'a' and s[i + 1] != 'e':
#             return False
#         if s[i] == 'e' and (s[i + 1] != 'a' and s[i + 1] != 'i'):
#             return False
#         if s[i] == 'i' and s[i + 1] == 'i':
#             return False
#         if s[i] == 'o' and (s[i + 1] != 'i' and s[i + 1] != 'u'):
#             return False
#         if s[i] == 'u' and s[i + 1] != 'a':
#             return False
#     return True


# a = set([s for s in itertools.product('aeiou', repeat=argn) if valid(s)])
# print(a)
# print(len(a))
# arr = [0] * 26
# for s in a:
#     arr[ord(s[-1]) - 97] += 1

# arr = [e for e in arr if e]
# print(arr)
