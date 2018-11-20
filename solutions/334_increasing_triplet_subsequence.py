class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = b = float('inf')
        for n in nums:
            a = min(a, n)
            if n > a: b = min(b, n)
            if n > b: return True
        return False


s = Solution()
res = s.increasingTriplet([1, 2, 8, 4, 5])
print(res)
