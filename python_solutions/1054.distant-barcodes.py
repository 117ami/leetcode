#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#
# https://leetcode.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (32.68%)
# Total Accepted:    2.8K
# Total Submissions: 7.8K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# In a warehouse, there is a row of barcodes, where the i-th barcode is
# barcodes[i].
#
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
# return any answer, and it is guaranteed an answer exists.
#
#
#
# Example 1:
#
#
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
#
#
#
#
# Note:
#
#
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
#
#
#
#
#
#


class Solution:
    def rearrangeBarcodes(self, barcodes):
        import collections
        res = barcodes[:]
        pos = 0
        for k, v in collections.Counter(barcodes).most_common():
            for _ in range(v):
                res[pos] = k
                pos += 2
                if pos >= len(res):
                    pos = 1
        return res


s = Solution()
barcodes = [1, 1, 1, 1, 2, 2, 3, 3]
print(s.rearrangeBarcodes(barcodes))
