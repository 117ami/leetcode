from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007


#
# @lc app=leetcode id=1125 lang=python3
#
# [1125] Smallest Sufficient Team
#
# https://leetcode.com/problems/smallest-sufficient-team/description/
#
# algorithms
# Hard (46.48%)
# Total Accepted:    8.6K
# Total Submissions: 18.5K
# Testcase Example:  '["java","nodejs","reactjs"]\n[["java"],["nodejs"],["nodejs","reactjs"]]'
#
# In a project, you have a list of required skills req_skills, and a list of
# people.  The i-th person people[i] contains a list of skills that person
# has.
#
# Consider a sufficient team: a set of people such that for every required
# skill in req_skills, there is at least one person in the team who has that
# skill.  We can represent these teams by the index of each person: for
# example, team = [0, 1, 3] represents the people with skills people[0],
# people[1], and people[3].
#
# Return any sufficient team of the smallest possible size, represented by the
# index of each person.
#
# You may return the answer in any order.  It is guaranteed an answer
# exists.
#
#
# Example 1:
# Input: req_skills = ["java","nodejs","reactjs"], people =
# [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]
# Example 2:
# Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"],
# people =
# [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]
#
#
# Constraints:
#
#
# 1 <= req_skills.length <= 16
# 1 <= people.length <= 60
# 1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
# Elements of req_skills and people[i] are (respectively) distinct.
# req_skills[i][j], people[i][j][k] are lowercase English letters.
# Every skill in people[i] is a skill in req_skills.
# It is guaranteed a sufficient team exists.
#
#
#
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        len_req, len_people = len(req_skills), len(people)
        skill2index = dict((s, i) for i, s in enumerate(req_skills))
        dp = {0: []}
        for i, p in enumerate(people):
            cur_skill = reduce(lambda a, b: a | (1 << skill2index[b]), p, 0)
            for skill_set in list(dp.keys()):
                need = dp[skill_set]
                hire_him = skill_set | cur_skill
                if hire_him not in dp or len(dp[hire_him]) > len(need) + 1:
                    dp[hire_him] = need + [i]
        print(dp[(1 << len_req) - 1])
        return dp[(1 << len_req) - 1]


sol = Solution()

# req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
req_skills, people = [
    "algorithms", "math", "java", "reactjs", "csharp", "aws"
], [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
    ["java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"],
    ["aws", "java"]]
print(sol.smallestSufficientTeam(req_skills, people))
