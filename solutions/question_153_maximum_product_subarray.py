
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = imax = imin = 0
        for n in nums[1:]:
            if n < 0:
                imax, imin = imin, imax
            imax = max(n, n * imax)
            imin = min(n, n * imin)
            r = max(r, imax)
        return r


nums = [2, 3, 4, -1, 2]
Solution().maxProduct(nums)
