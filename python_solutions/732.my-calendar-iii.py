import heapq
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
true = True
false = False
#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#
# https://leetcode.com/problems/my-calendar-iii/description/
#
# algorithms
# Hard (57.64%)
# Total Accepted:    16.7K
# Total Submissions: 28.9K
# Testcase Example:  '["MyCalendarThree","book","book","book","book","book","book"]\n' +  '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# Implement a MyCalendarThree class to store your events. A new event can
# always be added.
#
# Your class will have one method, book(int start, int end). Formally, this
# represents a booking on the half open interval [start, end), the range of
# real numbers x such that start <= x < end.
#
# A K-booking happens when K events have some non-empty intersection (ie.,
# there is some time that is common to all K events.)
#
# For each call to the method MyCalendar.book, return an integer K representing
# the largest integer such that there exists a K-booking in the calendar.
# Your class will be called like this: MyCalendarThree cal = new
# MyCalendarThree(); MyCalendarThree.book(start, end)
#
# Example 1:
#
#
# MyCalendarThree();
# MyCalendarThree.book(10, 20); // returns 1
# MyCalendarThree.book(50, 60); // returns 1
# MyCalendarThree.book(10, 40); // returns 2
# MyCalendarThree.book(5, 15); // returns 3
# MyCalendarThree.book(5, 10); // returns 3
# MyCalendarThree.book(25, 55); // returns 3
# Explanation:
# The first two events can be booked and are disjoint, so the maximum K-booking
# is a 1-booking.
# The third event [10, 40) intersects the first event, and the maximum
# K-booking is a 2-booking.
# The remaining events cause the maximum K-booking to be only a 3-booking.
# Note that the last event locally causes a 2-booking, but the answer is still
# 3 because
# eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
#
#
#
#
# Note:
#
#
# The number of calls to MyCalendarThree.book per test case will be at most
# 400.
# In calls to MyCalendarThree.book(start, end), start and end are integers in
# the range [0, 10^9].
#
#
#
#


class MyCalendarThree:
    def __init__(self):
        self.d = {}
        self.timeline = []
        self.max = 0

    def book(self, s, e):
        if s in self.d:
            self.d[s] += 1
        else:
            self.d[s] = 1
            # i = bisect_left(self.timeline, s)
            self.timeline.append(s)

        if e in self.d:
            self.d[e] -= 1
        else:
            self.d[e] = -1
            self.timeline.append(e)
            # i = bisect_left(self.timeline, e)
            # self.timeline.insert(i, e)

        x = 0
        # print(self.timeline, self.d)
        self.timeline.sort()
        for t in self.timeline:
            x += self.d[t]
            self.max = max(self.max, x)
        return self.max
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

c = MyCalendarThree()
for i, j in [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]:
    print(c.book(i, j))


# print(c.book(3, 10))
# print(c.book(4, 11))
