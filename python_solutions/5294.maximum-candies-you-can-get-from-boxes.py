#
# @lc app=leetcode id=5294 lang=python3
#
# [5294] Maximum Candies You Can Get from Boxes
#
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/
#
# algorithms
# Hard (51.21%)
# Total Accepted:    1.5K
# Total Submissions: 2.7K
# Testcase Example:  '[1,0,1,0]\n[7,5,4,100]\n[[],[],[1],[]]\n[[1,2],[3],[],[]]\n[0]'
#
# Given n boxes, each box is given in the format [status, candies, keys,
# containedBoxes] where:
#
#
# status[i]: an integer which is 1 if box[i] is open and 0 if box[i] is
# closed.
# candies[i]: an integer representing the number of candies in box[i].
# keys[i]: an array contains the indices of the boxes you can open with the key
# in box[i].
# containedBoxes[i]: an array contains the indices of the boxes found in
# box[i].
#
#
# You will start with some boxes given in initialBoxes array. You can take all
# the candies in any open box and you can use the keys in it to open new boxes
# and you also can use the boxes you find in it.
#
# Return the maximum number of candies you can get following the rules
# above.
#
#
# Example 1:
#
#
# Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]],
# containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
# Output: 16
# Explanation: You will be initially given box 0. You will find 7 candies in it
# and boxes 1 and 2. Box 1 is closed and you don't have a key for it so you
# will open box 2. You will find 4 candies and a key to box 1 in box 2.
# In box 1, you will find 5 candies and box 3 but you will not find a key to
# box 3 so box 3 will remain closed.
# Total number of candies collected = 7 + 4 + 5 = 16 candy.
#
#
# Example 2:
#
#
# Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys =
# [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]],
# initialBoxes = [0]
# Output: 6
# Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4
# and 5 and their keys. The total number of candies will be 6.
#
#
# Example 3:
#
#
# Input: status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]],
# containedBoxes = [[],[],[]], initialBoxes = [1]
# Output: 1
#
#
# Example 4:
#
#
# Input: status = [1], candies = [100], keys = [[]], containedBoxes = [[]],
# initialBoxes = []
# Output: 0
#
#
# Example 5:
#
#
# Input: status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes
# = [[],[],[]], initialBoxes = [2,1,0]
# Output: 7
#
#
#
# Constraints:
#
#
# 1 <= status.length <= 1000
# status.length == candies.length == keys.length == containedBoxes.length ==
# n
# status[i] is 0 or 1.
# 1 <= candies[i] <= 1000
# 0 <= keys[i].length <= status.length
# 0 <= keys[i][j] < status.length
# All values in keys[i] are unique.
# 0 <= containedBoxes[i].length <= status.length
# 0 <= containedBoxes[i][j] < status.length
# All values in containedBoxes[i] are unique.
# Each box is contained in one box at most.
# 0 <= initialBoxes.length <= status.length
# 0 <= initialBoxes[i] < status.length
#
#


from collections import defaultdict, Counter


class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        
        if len(initialBoxes) == 0: return 0
        seen = {}
        res = 0
        locked = {}
        keys_at_hand = set()

        while len(initialBoxes) > 0:
            c = initialBoxes.pop(0)
            # print(c, initialBoxes)
            if c in seen: continue 
            res += candies[c]
            
            keys_at_hand.update(keys[c])

            for nc in containedBoxes[c] + list(locked.keys()):
                if status[nc] == 1 or nc in keys_at_hand: # open or has key
                    initialBoxes.append(nc)
                else:
                    locked[nc] = True 

            seen[c] = True

        return res 

s = Solution()
status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]

status = [1,1,1]
candies = [100,1,100]
keys = [[],[0,2],[]]
containedBoxes = [[],[],[]]
initialBoxes = [1]
 
print(s.maxCandies(status, candies, keys, containedBoxes, initialBoxes))