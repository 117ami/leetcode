"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.  You may assume the given string consists of lowercase English letters only and its length  will not exceed 10000. 
Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"
Output: False
Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 1
        true, false = [True, False]
        while i <= len(s) / 2:
            sub = s[0:i]
            j = i
            k = i + i
            while k <= len(s) and sub == s[j:k]:
                j += i
                k += i
            if j == len(s): return true
            i += 1
        return false

    def repeatedSubstringPattern2(self, s):
        return any(s[:i] * int(len(s) / i) == s
                   for i in range(1,
                                  int(len(s) / 2) + 1) if len(s) % i == 0)

    def repeatedSubstringPattern3(self, s):
        return s in (s * 2)[1:-1]


s = "abcabcabcabc"
s = "abaababaab"
print(Solution().repeatedSubstringPattern(s))
print(Solution().repeatedSubstringPattern2(s))
print(Solution().repeatedSubstringPattern3(s))

print(((s + s)[1:-1]))
