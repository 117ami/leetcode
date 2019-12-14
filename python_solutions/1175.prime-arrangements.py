#
# @lc app=leetcode id=1175 lang=python3
#
# [1175] Prime Arrangements
#
# https://leetcode.com/problems/prime-arrangements/description/
#
# algorithms
# Easy (50.25%)
# Total Accepted:    7.7K
# Total Submissions: 15.3K
# Testcase Example:  '5'
#
# Return the number of permutations of 1 to n so that prime numbers are at
# prime indices (1-indexed.)
#
# (Recall that an integer is prime if and only if it is greater than 1, and
# cannot be written as a product of two positive integers both smaller than
# it.)
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1]
# is not because the prime number 5 is at index 1.
#
#
# Example 2:
#
#
# Input: n = 100
# Output: 682289015
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
#
#
#


import math


def sieve_primes(n):
    """ Find all primes under (inclusive) n
    """
    tables = []
    bool_tables = [True] * (1 + n)
    for i in range(2, n + 1):
        if bool_tables[i]:
            tables.append(i)
            for j in range(i << 1, n + 1, i):
                bool_tables[j] = False
    return tables


def isprime(x):
    """Combining sieve_primes to decide whether a
    given number is prime
    """
    n = 1 + int(x ** 0.5)
    tables = []
    bool_tables = [True] * (1 + n)
    for i in range(2, n + 1):
        if bool_tables[i]:
            tables.append(i)
            if x % i == 0:
                return False

            for j in range(i << 1, n + 1, i):
                bool_tables[j] = False
    return True


mod = pow(10, 9) + 7


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        res = 1
        idx = len([i for i in range(1, n + 1) if isprime(i)])
        return (math.factorial(idx) * math.factorial(n - idx)) % mod


s = Solution()
print(s.numPrimeArrangements(100))

# print(isprime(154874579983))
# bound = pow(10, 7) + 9
# print(sieve_primes(bound))
