'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.
Example:
Input:[100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        ans = 0
        for n in nums:
            if n in d: continue
            else:
                v = d.get(n - 1, 0) + d.get(n + 1, 0) + 1
                d[n], d[n - d.get(n - 1, 0)], d[n + d.get(n + 1, 0)] = v, v, v
                ans = max(ans, v)
        return ans


nums = [1, 0, 1, 2, 4, 3]
print(Solution().longestConsecutive(nums))
