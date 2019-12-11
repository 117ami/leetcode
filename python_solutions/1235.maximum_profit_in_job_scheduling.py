# https://leetcode.com/problems/maximum-profit-in-job-scheduling
# Hard (Difficulty)

# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
# You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.
# If you choose a job that ends at time X you will be able to start another job that starts at time X.
#  
# Example 1:
#
# Example 2:
#
# Example 3:
#
#  
# Constraints:
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
#
#
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
#
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
#
# xxxxxxxxxx
# class Solution {
# public:
#     int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
#         
#     }
# };

import heapq

class Solution:
    def jobScheduling(self, st, et, p):
        jobs = sorted(zip(st, et, p), key=lambda x: x[0])
        heap = []
        maxprof = 0

        for s, e, p in jobs:
            # Compute the max profit before time s
            while heap and heap[0][0] <= s:
                _, prof = heapq.heappop(heap)
                maxprof = max(maxprof, prof)

            heapq.heappush(heap, (e, maxprof + p))
            print(heap)

        for _, p in heap:
            maxprof = max(maxprof, p)

        return maxprof


st, et, p = [1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]
# st, et, p = [1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]
print(Solution().jobScheduling(st, et, p))
