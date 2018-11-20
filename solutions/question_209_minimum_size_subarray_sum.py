

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
        nsum = j = 0
        rmin = 1 << 32
        for i in range(len(nums)):
            if nums[i] >= s: return 1 # Much faster than codes without this line
            nsum += nums[i]
            while nsum >= s:
                rmin = min(rmin, i - j + 1)
                nsum -= nums[j]
                j += 1
        return rmin
        
s = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(s, nums))
