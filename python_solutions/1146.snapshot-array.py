from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
true = True
false = False
#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#
# https://leetcode.com/problems/snapshot-array/description/
#
# algorithms
# Medium (34.82%)
# Total Accepted:    12.9K
# Total Submissions: 36.9K
# Testcase Example:  '["SnapshotArray","set","snap","set","get"]\n[[3],[0,5],[],[0,6],[0,0]]'
#
# Implement a SnapshotArray that supports the following interface:
# 
# 
# SnapshotArray(int length) initializes an array-like data structure with the
# given length.  Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to
# val.
# int snap() takes a snapshot of the array and returns the snap_id: the total
# number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we
# took the snapshot with the given snap_id
# 
# 
# 
# Example 1:
# 
# 
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return
# 5
# 
# 
# Constraints:
# 
# 
# 1 <= length <= 50000
# At most 50000 calls will be made to set, snap, and get.
# 0 <= index < length
# 0 <= snap_id < (the total number of times we call snap())
# 0 <= val <= 10^9
# 
# 
#
class SnapshotArray:
    def __init__(self, length: int):
        self.list = [[[-1, 0]] for _ in range(length)]
        self.cur = [0] * length
        self.sid = 0 
        
    def set(self, index: int, val: int) -> None:
        self.list[index].append([self.sid, val])


    def snap(self) -> int:
        self.sid += 1
        return self.sid - 1

    def get(self, index: int, snap_id: int) -> int:
        # print(self.list[index])
        i = bisect_right(self.list[index], [snap_id + 1]) - 1
        return self.list[index][i][1]
        
# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(5)
obj.set(0, 4)
obj.set(0, 16)
obj.set(0, 13)
param_2 = obj.snap()
p3 = obj.get(0, 0)
print(p3)

a = [1,3,4,4,4,6]
print(bisect_right(a, 4))