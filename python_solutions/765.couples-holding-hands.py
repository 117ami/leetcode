#
# @lc app=leetcode id=765 lang=python
#
# [765] Couples Holding Hands
#
# https://leetcode.com/problems/couples-holding-hands/description/
#
# algorithms
# Hard (49.92%)
# Total Accepted:    10.8K
# Total Submissions: 21.7K
# Testcase Example:  '[0,2,1,3]'
#
#
# N couples sit in 2N seats arranged in a row and want to hold hands.  We want
# to know the minimum number of swaps so that every couple is sitting side by
# side.  A swap consists of choosing any two people, then they stand up and
# switch seats.
#
# The people and seats are represented by an integer from 0 to 2N-1, the
# couples are numbered in order, the first couple being (0, 1), the second
# couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
#
# The couples' initial seating is given by row[i] being the value of the person
# who is initially sitting in the i-th seat.
#
# Example 1:
# Input: row = [0, 2, 1, 3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2])
# person.
#
#
# Example 2:
# Input: row = [3, 2, 0, 1]
# Output: 0
# Explanation: All couples are already seated side by side.
#
#
#
# Note:
# ⁠
# ⁠len(row) is even and in the range of [4, 60].
# ⁠row is guaranteed to be a permutation of 0...len(row)-1.
#
#


class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        res = 0
        v2index = {k: v for v, k in enumerate(row)}

        for i in range(0, len(row), 2):
            a, b = row[i], row[i + 1]
            if a // 2 == b // 2:  # form a couple
                continue
            couple = a - 1 if a & 1 else a + 1
            couple_id = v2index[couple]
            row[i + 1], row[couple_id] = row[couple_id], row[i + 1]
            v2index[couple] = i + 1
            v2index[b] = couple_id
            res += 1

        return res


row = [3, 0, 1, 5, 2, 4]
print(Solution().minSwapsCouples(row))
