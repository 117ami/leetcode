from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#
# https://leetcode.com/problems/design-underground-system/description/
#
# algorithms
# Medium (60.09%)
# Total Accepted:    8.7K
# Total Submissions: 14.5K
# Testcase Example:  '["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]\n' +
# '[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]'
#
# Implement the class UndergroundSystem that supports three methods:
#
# 1. checkIn(int id, string stationName, int t)
#
#
# A customer with id card equal to id, gets in the station stationName at time
# t.
# A customer can only be checked into one place at a time.
#
#
# 2. checkOut(int id, string stationName, int t)
#
#
# A customer with id card equal to id, gets out from the station stationName at
# time t.
#
#
# 3. getAverageTime(string startStation, string endStation) 
#
#
# Returns the average time to travel between the startStation and the
# endStation.
# The average time is computed from all the previous traveling from
# startStation to endStation that happened directly.
# Call to getAverageTime is always valid.
#
#
# You can assume all calls to checkIn and checkOut methods are consistent. That
# is, if a customer gets in at time t1 at some station, then it gets out at
# time t2 with t2 > t1. All events happen in chronological order.
#
#
# Example 1:
# Input
#
#
#
# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
#
# [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
#
# Output
#
# [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
#
# Explanation
# UndergroundSystem undergroundSystem = new UndergroundSystem();
# undergroundSystem.checkIn(45, "Leyton", 3);
# undergroundSystem.checkIn(32, "Paradise", 8);
# undergroundSystem.checkIn(27, "Leyton", 10);
# undergroundSystem.checkOut(45, "Waterloo", 15);
# undergroundSystem.checkOut(27, "Waterloo", 20);
# undergroundSystem.checkOut(32, "Cambridge", 22);
# undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return
# 14.00000. There was only one travel from "Paradise" (at time 8) to
# "Cambridge" (at time 22)
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return
# 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with
# id=45 from time=3 to time=15 and a customer with id=27 from time=10 to
# time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
# undergroundSystem.checkIn(10, "Leyton", 24);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return
# 11.00000
# undergroundSystem.checkOut(10, "Waterloo", 38);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return
# 12.00000
#
#
# Example 2:
# Input
#
#
#
# ["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
#
# [[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]
#
# Output
# [null,null,null,5.00000,null,null,5.50000,null,null,6.66667]
#
# Explanation
# UndergroundSystem undergroundSystem = new UndergroundSystem();
# undergroundSystem.checkIn(10, "Leyton", 3);
# undergroundSystem.checkOut(10, "Paradise", 8);
# undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.00000
# undergroundSystem.checkIn(5, "Leyton", 10);
# undergroundSystem.checkOut(5, "Paradise", 16);
# undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.50000
# undergroundSystem.checkIn(2, "Leyton", 21);
# undergroundSystem.checkOut(2, "Paradise", 30);
# undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 6.66667
#
#
#
# Constraints:
#
#
# There will be at most 20000 operations.
# 1 <= id, t <= 10^6
# All strings consist of uppercase, lowercase English letters and digits.
# 1 <= stationName.length <= 10
# Answers within 10^-5 of the actual value will be accepted as correct.
#
#
#


class UndergroundSystem:
    def __init__(self):
        self.ids = {}
        self.sts = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s1, t1 = self.ids[id]
        s_pair = (s1, stationName)
        if s_pair not in self.sts:
          self.sts[s_pair] = (t - t1, 1)
        else:
          t_sum, cnt = self.sts[s_pair]
          self.sts[s_pair] = (t_sum + t - t1, cnt + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t, c = self.sts[(startStation, endStation)]
        # print(t / c)
        return t / c 

# undergroundSystem = UndergroundSystem()
# undergroundSystem.checkIn(10, "Leyton", 3)
# undergroundSystem.checkOut(10, "Paradise", 8)
# undergroundSystem.getAverageTime("Leyton", "Paradise")  # return 5.00000
# undergroundSystem.checkIn(5, "Leyton", 10)
# undergroundSystem.checkOut(5, "Paradise", 16)
# undergroundSystem.getAverageTime("Leyton", "Paradise")  # return 5.50000
# undergroundSystem.checkIn(2, "Leyton", 21)
# undergroundSystem.checkOut(2, "Paradise", 30)
# undergroundSystem.getAverageTime("Leyton", "Paradise")  # return 6.66667

# undergroundSystem.checkIn(45, "Leyton", 3);
# undergroundSystem.checkIn(32, "Paradise", 8);
# undergroundSystem.checkIn(27, "Leyton", 10);
# undergroundSystem.checkOut(45, "Waterloo", 15);
# undergroundSystem.checkOut(27, "Waterloo", 20);
# undergroundSystem.checkOut(32, "Cambridge", 22);
# undergroundSystem.getAverageTime("Paradise", "Cambridge");       # return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          # return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
# undergroundSystem.checkIn(10, "Leyton", 24);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          # return 11.00000
# undergroundSystem.checkOut(10, "Waterloo", 38);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          # return 12.00000
