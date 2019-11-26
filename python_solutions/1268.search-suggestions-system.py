#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
# https://leetcode.com/problems/search-suggestions-system/description/
#
# algorithms
# Medium (46.79%)
# Total Accepted:    4.2K
# Total Submissions: 8.8K
# Testcase Example:  '["mobile","mouse","moneypot","monitor","mousepad"]\r\n"mouse"\r'
#
# Given an array of strings products and a string searchWord. We want to design
# a system that suggests at most three product names from products after each
# character of searchWord is typed. Suggested products should have common
# prefix with the searchWord. If there are more than three products with a
# common prefix return the three lexicographically minimums products.
#
# Return list of lists of the suggested products after each character of
# searchWord is typed. 
#
#
# Example 1:
#
#
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"],
# searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically =
# ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user
# ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
#
#
# Example 2:
#
#
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
#
#
# Example 3:
#
#
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord =
# "bags"
# Output:
# [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
#
#
# Example 4:
#
#
# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]
#
#
#
# Constraints:
#
#
# 1 <= products.length <= 1000
# There are no repeated elements in products.
# 1 <= Σ products[i].length <= 2 * 10^4
# All characters of products[i] are lower-case English letters.
# 1 <= searchWord.length <= 1000
# All characters of searchWord are lower-case English letters.
#
#
#
import heapq
from bisect import bisect_left


class PriorityQueue(object):
    def __init__(self, li=[]):
        self.queue = []
        for i in li:
            self.push(i)

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for return the size of queue
    def size(self):
        return len(self.queue)

    # for inserting an element in the queue
    def push(self, data):
        insert_idx = bisect_left(self.queue, data)
        self.queue.insert(insert_idx, data)

    # for popping an element based on Priority
    def pop(self):
        return self.queue.pop()

    def tolist(self):
        return self.queue


class Solution:
    def suggestedProducts_1(self, products, sw):
        """ Method 1: Using Priority Queue to store all possible strings sharing
        same profix with sw[:i] for i in 1->len(sw)
        """
        hash = {}
        for p in products:
            for i in range(1, len(p) + 1):
                substr = p[:i]
                if substr not in hash:
                    hash[substr] = PriorityQueue()
                hash[substr].push(p)

        res = []

        for i in range(1, len(sw) + 1):
            substr = sw[:i]
            if substr in hash:
                res.append(hash[substr].tolist()[:3])
            else:
                res.append([])

        return res

    def suggestedProducts_2(self, products, sw):
        """Method 2: sort and match prefix
        """
        products.sort()
        lo, hi = 0, len(products) - 1
        res = []

        for i, c in enumerate(sw):
            while lo <= hi and (
                    len(products[lo]) <= i or products[lo][i] != c):
                lo += 1
            while lo <= hi and (
                    len(products[hi]) <= i or products[hi][i] != c):
                hi -= 1

            if lo > hi:
                res.append([])
            else:
                res.append(products[lo:min(lo + 3, hi + 1)])
        return res


    def suggestedProducts(self, products, sw):
        """ Method 3: simplify method 2. 
        Method 2 is faster. 
        """
        products.sort()
        res, prefix, i = [], '', 0

        for c in sw:
            prefix += c
            i = bisect_left(products, prefix, i)
            res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return res


s = Solution()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
sw = "mouse"
# products = ["havana"]
# sw = "zhavana"
# products = ["bags", "baggage", "banner", "box", "cloths"]
# sw = "bags"
print(s.suggestedProducts(products, sw))
