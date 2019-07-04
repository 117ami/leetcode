

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        r = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                r += prices[i] - prices[i-1]
        return r


prices = [2, 3, 1, 4,2, 5, 1, 6]
print(Solution().maxProfit(prices))
