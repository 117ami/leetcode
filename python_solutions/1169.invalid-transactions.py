Copyright © 2019 LeetCode Help Center  |  Jobs  |  Bug Bounty  |  Terms  |  Privacy Policy       United Statesfrom collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce 
import string
true = True
false = False
#
# @lc app=leetcode id=1169 lang=python3
#
# [1169] Invalid Transactions
#
# https://leetcode.com/problems/invalid-transactions/description/
#
# algorithms
# Medium (29.29%)
# Total Accepted:    8K
# Total Submissions: 27.2K
# Testcase Example:  '["alice,20,800,mtv","alice,50,100,beijing"]'
#
# A transaction is possibly invalid if:
# 
# 
# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with
# the same name in a different city.
# 
# 
# Each transaction string transactions[i] consists of comma separated values
# representing the name, time (in minutes), amount, and city of the
# transaction.
# 
# Given a list of transactions, return a list of transactions that are possibly
# invalid.  You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction
# occurs within a difference of 60 minutes, have the same name and is in a
# different city. Similarly the second one is invalid too.
# 
# Example 2:
# 
# 
# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
# 
# 
# Example 3:
# 
# 
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]
# 
# 
# 
# Constraints:
# 
# 
# transactions.length <= 1000
# Each transactions[i] takes the form "{name},{time},{amount},{city}"
# Each {name} and {city} consist of lowercase English letters, and have lengths
# between 1 and 10.
# Each {time} consist of digits, and represent an integer between 0 and
# 1000.
# Each {amount} consist of digits, and represent an integer between 0 and
# 2000.
# 
# 
#
from collections import defaultdict, deque
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        users = defaultdict(list)
        
        for tran in transactions:
            usr, ts, amt, cty = [_ for _ in tran.split(',')]
            ts = int(ts)
            amt = int(amt)
            
            users[usr].append((ts, amt, cty))
            
        res = []
        
        for usr in users:
            #latest = deque([(float('-inf'), 0, '')])             
            #print latest
            left = right = 0
            users[usr].sort()
            
            i = 0
            for ts, amt, cty in users[usr]:
                #print ts, amt, cty 
                if amt > 1000:
                    res.append(','.join([usr, str(ts), str(amt), cty]))
                    continue
                    
                while ts - users[usr][left][0] > 60:
                    left += 1
                
                while right < len(users[usr]) and users[usr][right][0] - ts < 60:
                    right += 1
                    
                for record in users[usr][left:right]:
                    if cty != record[2]:
                        res.append(','.join([usr, str(ts), str(amt), cty]))
                        break
                i += 1
                
        return res