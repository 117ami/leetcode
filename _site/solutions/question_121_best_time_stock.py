

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        r = 0
        low = 1 << 32
        for p in prices:
            low = min(low, p)
            r = max(r, p - low)
        return r
