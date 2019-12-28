from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
true = True
false = False
#
# @lc app=leetcode id=1177 lang=python3
#
# [1177] Can Make Palindrome from Substring
#
# https://leetcode.com/problems/can-make-palindrome-from-substring/description/
#
# algorithms
# Medium (32.81%)
# Total Accepted:    7.1K
# Total Submissions: 21.6K
# Testcase Example:  '"abcda"\n[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]'
#
# Given a string s, we make queries on substrings of s.
#
# For each query queries[i] = [left, right, k], we may rearrange the substring
# s[left], ..., s[right], and then choose up to k of them to replace with any
# lowercase English letter. 
#
# If the substring is possible to be a palindrome string after the operations
# above, the result of the query is true. Otherwise, the result is false.
#
# Return an array answer[], where answer[i] is the result of the i-th query
# queries[i].
#
# Note that: Each letter is counted individually for replacement so if for
# example s[left..right] = "aaa", and k = 2, we can only replace two of the
# letters.  (Also, note that the initial string s is never modified by any
# query.)
#
#
# Example :
#
#
# Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
# Output: [true,false,false,true,true]
# Explanation:
# queries[0] : substring = "d", is palidrome.
# queries[1] : substring = "bc", is not palidrome.
# queries[2] : substring = "abcd", is not palidrome after replacing only 1
# character.
# queries[3] : substring = "abcd", could be changed to "abba" which is
# palidrome. Also this can be changed to "baab" first rearrange it "bacd" then
# replace "cd" with "ab".
# queries[4] : substring = "abcda", could be changed to "abcba" which is
# palidrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length, queries.length <= 10^5
# 0 <= queries[i][0] <= queries[i][1] < s.length
# 0 <= queries[i][2] <= s.length
# s only contains lowercase English letters.
#
#
#


class Solution:
    def canMakePaliQueries_2(self, s, qs):
        n = len(s)
        res = [False] * len(qs)
        dp = [[0]*26]
        for i in range(1, n+1):
            nxt = dp[i-1][:]
            j = ord(s[i-1]) - 97
            nxt[j] += 1
            dp.append(nxt)

        for i, (l, r, k) in enumerate(qs):
            dl = dp[l]
            dr = dp[r + 1]
            res[i] = (sum((dr[j] - dl[j]) & 1 for j in range(26)) // 2 <= k)
        return res

    def canMakePaliQueries(self, s, qs):
        odds = [0]
        for c in s:
            odds.append(odds[-1] ^ 1 << (ord(c) - ord('a')))
        return [bin(odds[hi + 1] ^ odds[lo]).count('1') // 2 <= k for lo, hi, k in qs] 


s = Solution()

ss, qs = "abcda", [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
ss, qs = "hunu", [[1,1,1],[2,3,0],[3,3,1],[0,3,2],[1,3,3],[2,3,1],[3,3,1],[0,3,0],[1,1,1],[2,3,0],[3,3,1],[0,3,1],[1,1,1]]
ss, qs = "orsrurgtinans", [[0,7,0],[1,4,4],[6,12,3],[10,11,1],[5,7,1],[0,10,6]]
ss, qs = "xebyvmjqbmbs", [[9,9,1],[6,9,3],[11,11,1],[0,3,3],[9,10,0],[10,11,2],[3,3,1],[4,11,8],[1,10,3],[2,9,7],[11,11,1]]
# ss = "abca"
print(s.canMakePaliQueries(ss, qs))
print ([true,true,true,true,false,true,true,true,true,true,true])
# print([true,false,true,true,true,true,true,false,true,false,true,true,true])