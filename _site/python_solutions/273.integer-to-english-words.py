#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (24.20%)
# Total Accepted:    100K
# Total Submissions: 413K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
#
# Input: 123
# Output: "One Hundred Twenty Three"
#
#
# Example 2:
#
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
#
#
# Example 4:
#
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
#
#
#


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        below19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(
            ' ')
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(
            ' ')
        ks = 'Thousand Million Billion'.split(' ')

        def words(n, idx=0):
            if n == 0:
                return []
            elif n < 20:
                return [below19[n - 1]]
            elif n < 100:
                return [tens[n // 10 - 2]] + words(n % 10)
            elif n < 1000:
                return [below19[n // 100 - 1], 'Hundred'] + words(n % 100)
            else:
                m, r = divmod(n, 1000)
                space = [] if m % 1000 == 0 else [ks[idx]]
                return words(m, idx + 1) + space + words(r, idx)

        return ' '.join(words(num, 0))


# print(Solution().numberToWords(123))
