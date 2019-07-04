import heapq

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = nums[0] * nums[1] * nums[-1]
        b = nums[-1] * nums[-2] * nums[-3]
        return max(a, b)

    def maximumProduct2(sort, nums):
        a, b = heapq.nlargest(3, nums),  heapq.nlargest(3, nums)
        return max(a[0] * a[1] * a[2], a[0] * b[1] * b[0])


nums = [2, 3, -1, -2, 9]
print(Solution().maximumProduct(nums))

Solution().maximumProduct2(nums)
