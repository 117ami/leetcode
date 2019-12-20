#
# @lc app=leetcode id=1147 lang=python3
#
# [1147] Longest Chunked Palindrome Decomposition
#
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/
#
# algorithms
# Hard (57.73%)
# Total Accepted:    6.3K
# Total Submissions: 10.9K
# Testcase Example:  '"ghiabcdefhelloadamhelloabcdefghi"'
#
# Return the largest possible k such that there exists a_1, a_2, ..., a_k such
# that:
# 
# 
# Each a_i is a non-empty string;
# Their concatenation a_1 + a_2 + ... + a_k is equal to text;
# For all 1 <= i <= k,  a_i = a_{k+1 - i}.
# 
# 
# 
# Example 1:
# 
# 
# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on
# "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
# 
# 
# Example 2:
# 
# 
# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".
# 
# 
# Example 3:
# 
# 
# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on
# "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
# 
# 
# Example 4:
# 
# 
# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".
# 
# 
# 
# Constraints:
# 
# 
# text consists only of lowercase English characters.
# 1 <= text.length <= 1000
# 
#
class Solution:
    def longestDecomposition(self, text: str) -> int:
        i, j, k = 0, 1, len(text)
        res = 0
        while i < k:
            # print(i, k, text[i:k+1])
            while i + j < k and text[i:i+j] != text[k-j:k]:
                j += 1
            if i + j <= k:
                res += 2 if i + j < k else 1
                i += j 
                k -= j 
                j = 1
        return res 

s = Solution()
text = "antaprezatepzapreanta"
text = "ghiabcdefhelloadamhelloabcdefghi"
text = "merchant"
print(s.longestDecomposition(text))

