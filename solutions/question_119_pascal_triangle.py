'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a = [0] * (rowIndex + 3)
        a[1] = 1
        b = [0] * (rowIndex + 3)
        for i in range(rowIndex):
            j = 1
            while j < rowIndex + 3:
                b[j] = a[j] + a[j - 1]
                j += 1
            a, b = b, a

        _, *res, _ = a
        return res

    def getRow2(self, rowIndex):
        res = [1]
        for i in range(rowIndex):
            res = (list(map(lambda x, y: x + y, [0] + res, res + [0])))
        return res


Solution().getRow(3)
Solution().getRow2(3)
