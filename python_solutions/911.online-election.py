from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#
# https://leetcode.com/problems/online-election/description/
#
# algorithms
# Medium (48.83%)
# Total Accepted:    17.9K
# Total Submissions: 36.6K
# Testcase Example:  '["TopVotedCandidate","q","q","q","q","q","q"]\n' +
#   '[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]'
#
# In an election, the i-th vote was cast for persons[i] at time times[i].
#
# Now, we would like to implement the following query function:
# TopVotedCandidate.q(int t) will return the number of the person that was
# leading the election at time t.  
#
# Votes cast at time t will count towards our query.  In the case of a tie, the
# most recent vote (among tied candidates) wins.
#
#
#
#
# Example 1:
#
#
# Input: ["TopVotedCandidate","q","q","q","q","q","q"],
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation:
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the
# most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
#
#
#
#
# Note:
#
#
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].
#
#
#
#


class TopVotedCandidate:

    def __init__(self, persons, times):
        self.votes = [0] * len(persons)
        curmax = 0
        cter = defaultdict(int)
        self.times = times
        for i, p in enumerate(persons):
            cter[p] += 1
            if cter[p] >= curmax:
                curmax = cter[p]
                self.votes[i] = p
            else:
                self.votes[i] = self.votes[i - 1]

    def q(self, t: int) -> int:
        i = bisect_right(self.times, t)
        if i == 0:
            return self.votes[0]
        return self.votes[i - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
persons, times = [0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]
obj = TopVotedCandidate(persons, times)
print(obj.votes)
qs = [3, 12, 25, 15, 24, 8, 32]
for qi in qs:
    print(qi, obj.q(qi))
# param_1 = obj.q(t)
