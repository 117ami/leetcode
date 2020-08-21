from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1044 lang=python3
#
# [1044] Longest Duplicate Substring
#
# https://leetcode.com/problems/longest-duplicate-substring/description/
#
# algorithms
# Hard (25.86%)
# Total Accepted:    10.4K
# Total Submissions: 39K
# Testcase Example:  '"banana"'
#
# Given a string S, consider all duplicated substrings: (contiguous) substrings
# of S that occur 2 or more times.  (The occurrences may overlap.)
#
# Return any duplicated substring that has the longest possible length.  (If S
# does not have a duplicated substring, the answer is "".)
#
#
#
# Example 1:
#
#
# Input: "banana"
# Output: "ana"
#
#
# Example 2:
#
#
# Input: "abcd"
# Output: ""
#
#
#
#
# Note:
#
#
# 2 <= S.length <= 10^5
# S consists of lowercase English letters.
#
#
#


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def search(nums, n, m):
            a, h = 26, 0
            for i in range(m):
                h = (h * a + nums[i]) % mod

            seen = {h}
            base = pow(a, m, mod)
            for i in range(n - m):
                h = (h * a - nums[i] * base + nums[i + m]) % mod
                if h in seen:
                    return i + 1
                seen.add(h)
            return -1

        n = len(S)
        mod = 1 << 32
        nums = list(map(ord, S))

        l, r = 1, n
        while l <= r:
            m = l + (r - l) // 2
            if search(nums, n, m) != -1:
                l = m + 1
            else:
                r = m - 1
        start = search(nums, n, r)
        return S[start:start + l - 1]


xxxs = 'banana'
s = "moplvidmaagmsiyyrkchbyhivlqwqsjcgtumqscmxrxrvwsnjjvygrelcbjgbpounhuyealllginkitfaiviraqcycjmskrozcdqylbuejrgfnquercvghppljmojfvylcxakyjxnampmakyjbqgwbyokaybcuklkaqzawageypfqhhasetugatdaxpvtevrigynxbqodiyioapgxqkndujeranxgebnpgsukybyowbxhgpkwjfdywfkpufcxzzqiuglkakibbkobonunnzwbjktykebfcbobxdflnyzngheatpcvnhdwkkhnlwnjdnrmjaevqopvinnzgacjkbhvsdsvuuwwhwesgtdzuctshytyfugdqswvxisyxcxoihfgzxnidnfadphwumtgdfmhjkaryjxvfquucltmuoosamjwqqzeleaiplwcbbxjxxvgsnonoivbnmiwbnijkzgoenohqncjqnckxbhpvreasdyvffrolobxzrmrbvwkpdbfvbwwyibydhndmpvqyfmqjwosclwxhgxmwjiksjvsnwupraojuatksjfqkvvfroqxsraskbdbgtppjrnzpfzabmcczlwynwomebvrihxugvjmtrkzdwuafozjcfqacenabmmxzcueyqwvbtslhjeiopgbrbvfbnpmvlnyexopoahgmwplwxnxqzhucdieyvbgtkfmdeocamzenecqlbhqmdfrvpsqyxvkkyfrbyolzvcpcbkdprttijkzcrgciidavsmrczbollxbkytqjwbiupvsorvkorfriajdtsowenhpmdtvamkoqacwwlkqfdzorjtepwlemunyrghwlvjgaxbzawmikfhtaniwviqiaeinbsqidetfsdbgsydkxgwoqyztaqmyeefaihmgrbxzyheoegawthcsyyrpyvnhysynoaikwtvmwathsomddhltxpeuxettpbeftmmyrqclnzwljlpxazrzzdosemwmthcvgwtxtinffopqxbufjwsvhqamxpydcnpekqhsovvqugqhbgweaiheeicmkdtxltkalexbeftuxvwnxmqqjeyourvbdfikqnzdipmmmiltjapovlhkpunxljeutwhenrxyfeufmzipqvergdkwptkilwzdxlydxbjoxjzxwcfmznfqgoaemrrxuwpfkftwejubxkgjlizljoynvidqwxnvhngqakmmehtvykbjwrrrjvwnrteeoxmtygiiygynedvfzwkvmffghuduspyyrnftyvsvjstfohwwyxhmlfmwguxxzgwdzwlnnltpjvnzswhmbzgdwzhvbgkiddhirgljbflgvyksxgnsvztcywpvutqryzdeerlildbzmtsgnebvsjetdnfgikrbsktbrdamfccvcptfaaklmcaqmglneebpdxkvcwwpndrjqnpqgbgihsfeotgggkdbvcdwfjanvafvxsvvhzyncwlmqqsmledzfnxxfyvcmhtjreykqlrfiqlsqzraqgtmocijejneeezqxbtomkwugapwesrinfiaxwxradnuvbyssqkznwwpsbgatlsxfhpcidfgzrc"
sol = Solution()
print(sol.longestDupSubstring(xxxs))
