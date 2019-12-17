#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (48.75%)
# Total Accepted:    46.9K
# Total Submissions: 96.1K
# Testcase Example:  '13'
#
# Given an integer n, return 1 - n in lexicographical order.
# 
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# 
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
# 
#
class Solution:
    def helper(self, i, n, res):
        if i > n: return 
        res.append(i)
        self.helper(i * 10, n, res)
        if (i % 10) != 9:
            self.helper(i + 1, n, res)

    def lexicalOrder(self, n):
        res = []
        self.helper(1, n, res)
        return res
        # return sorted(range(1, n+1), key=lambda x: str(x))

s = Solution()
print(s.lexicalOrder(13))


