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
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#
# https://leetcode.com/problems/design-browser-history/description/
#
# algorithms
# Medium (58.80%)
# Total Accepted:    9.7K
# Total Submissions: 15.6K
# Testcase Example:  '["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]\r\n' +
# '[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]\r'
#
# You have a browser of one tab where you start on the homepage and you can
# visit another url, get back in the history number of steps or move forward in
# the history number of steps.
#
# Implement the BrowserHistory class:
#
#
# BrowserHistory(string homepage) Initializes the object with the homepage of
# the browser.
# void visit(string url) visits url from the posrent page. It clears up all the
# forward history.
# string back(int steps) Move steps back in history. If you can only return x
# steps in the history and steps > x, you will return only x steps. Return the
# posrent url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only
# forward x steps in the history and steps > x, you will forward only x steps.
# Return the posrent url after forwarding in history at most steps.
#
#
#
# Example:
#
#
# Input:
#
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
#
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
# Output:
#
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
#
# Explanation:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit
# "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit
# "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit
# "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move
# back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move
# back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move
# forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit
# "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you
# cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move
# back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can
# move back only one step to "leetcode.com". return "leetcode.com"
#
#
#
# Constraints:
#
#
# 1 <= homepage.length <= 20
# 1 <= url.length <= 20
# 1 <= steps <= 100
# homepage and url consist of  '.' or lower case English letters.
# At most 5000 calls will be made to visit, back, and forward.
#
#


class BrowserHistory:
    def __init__(self, homepage: str):
        self.h = []
        self.pos = -1
        self.visit(homepage)

    def visit(self, url: str) -> None:
        if self.pos < len(self.h) - 1:
            self.h = self.h[:self.pos + 1]
        self.h.append(url)
        self.pos = len(self.h) - 1

    def back(self, steps: int) -> str:
        idx = self.pos - steps
        self.pos = max(0, idx)
        return self.h[self.pos]

    def forward(self, steps: int) -> str:
        idx = self.pos + steps
        self.pos = min(len(self.h) - 1, idx)
        return self.h[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory('lc')
obj.visit('g')
obj.visit('f')
obj.visit('y')
print(obj.h)
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
obj.visit('lk')
print(obj.forward(2))
print(obj.back(2))
print(obj.h)
print(obj.back(7))
