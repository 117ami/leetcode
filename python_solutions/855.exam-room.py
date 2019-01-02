#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#
# https://leetcode.com/problems/exam-room/description/
#
# algorithms
# Medium (35.42%)
# Total Accepted:    9.4K
# Total Submissions: 26.5K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n[[10],[],[],[],[],[4],[]]'
#
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ...,
# N-1.
#
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person.  If there are multiple such seats, they sit
# in the seat with the lowest number.  (Also, if no one is in the room, then
# the student sits at seat number 0.)
#
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat()
# returning an int representing what seat the student sat in, and
# ExamRoom.leave(int p) representing that the student in seat number p now
# leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a
# student sitting in seat p.
#
#
#
# Example 1:
#
#
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"],
# [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
#
#
# ​​​​​​​
#
# Note:
#
#
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
# all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting
# in seat number p.
#
#
#


class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.n = N
        self.taken = {}

    def seat(self):
        """
        :rtype: int
        """
        if len(self.taken) == 0:
            self.taken[0] = True
            return 0

        tkeys = sorted(list(self.taken.keys()))
        res, maxdist = -1, -1
        for i, n in enumerate(tkeys):
            if i == len(tkeys) - 1:
                break
            if maxdist >= int((tkeys[i + 1] - n) / 2):
                continue
            maxdist = int((tkeys[i + 1] - n) / 2)
            res = n + maxdist

        if maxdist <= tkeys[0]:
            maxdist = tkeys[0]
            res = 0

        if maxdist < self.n - 1 - tkeys[-1]:
            res = self.n - 1

        self.taken[res] = True
        # print(self.taken)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.taken.pop(p, None)


# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(10)
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
# obj.leave(p)
