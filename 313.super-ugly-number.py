#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (41.44%)
# Total Accepted:    60.5K
# Total Submissions: 145.8K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
#
# Example:
#
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12
# ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
#
# Note:
#
#
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
#
#
#
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1] * n
        factors = primes[:]
        idx = [0] * len(primes)
        for i in range(1, n):
            ugly[i] = min(factors)
            for j in range(len(primes)):
                if factors[j] == ugly[i]:
                    idx[j] += 1
                    factors[j] = primes[j] * ugly[idx[j]]
            print(ugly, factors, idx)
        return ugly[-1]


s = Solution()
primes = [2, 7, 13, 19]
# for n in range(1,10):
n = 4
print(s.nthSuperUglyNumber(n, primes))
