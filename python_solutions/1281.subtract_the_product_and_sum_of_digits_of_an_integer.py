# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
# Easy (Difficulty)

#  
# Example 1:
# Example 2:
#  
# Constraints:
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21
#
# xxxxxxxxxx
# class Solution {
# public:
#     int subtractProductAndSum(int n) {
#         
#     }
# };

import operator
from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # prod, su = 1, 0
        # while n > 0:
        #     n, b = divmod(n, 10)
        #     prod, su = prod * b, su + b
        # return prod - su

        # Method 2
        a = list(map(int, str(n)))
        return reduce(operator.mul, a) - sum(a)


print(Solution().subtractProductAndSum(4421))
