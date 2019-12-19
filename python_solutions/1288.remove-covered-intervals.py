#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#
# https://leetcode.com/problems/remove-covered-intervals/description/
#
# algorithms
# Medium (57.60%)
# Total Accepted:    2.7K
# Total Submissions: 4.6K
# Testcase Example:  '[[1,4],[3,6],[2,8]]'
#
# Given a list of intervals, remove all intervals that are covered by another
# interval in the list. Interval [a,b) is covered by interval [c,d) if and only
# if c <= a and b <= d.
# 
# After doing so, return the number of remaining intervals.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 1000
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# intervals[i] != intervals[j] for all i != j
# 
# 
#
class Solution:
    def removeCoveredIntervals(self, ivs):
        # ivs.sort(lambda x, y: x[-1] < y[-1] or x[0] > y[0])
        ivs.sort(key = lambda e: (e[1], -e[0]))
        stack = []
        for i in ivs:
            while len(stack) > 0 and stack[-1][0] >= i[0]:
                stack.pop()
            stack.append(i)
        return len(stack)

ivs = [[2, 8], [4, 8], [3, 6]]        
# ivs = [[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]
s = Solution()
print(s.removeCoveredIntervals(ivs))



