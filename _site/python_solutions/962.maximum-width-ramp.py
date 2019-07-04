'''
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

# https://leetcode.com/problems/maximum-width-ramp/description/
# Medium

Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
'''

import bisect


class Solution:
    def maxWidthRamp(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        for j in reversed(range(len(a))):
            if not stack or a[j] > stack[-1][0]:
                stack.append([a[j], j])
            else:
                i = stack[bisect.bisect(stack, [a[j], j])][1]
                res = max(res, i - j)
        return res


a = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
# a = [6, 0, 8, 2, 1, 5]
# a = [6, 7, 8, 8, 6, 5, 5, 8, 2, 2]
print(Solution().maxWidthRamp(a))
