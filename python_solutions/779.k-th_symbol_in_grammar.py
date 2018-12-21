"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].

"""


class Solution:
    def kthGrammar(self, n, k):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        m = n
        flag = 0
        while m > 1:
            if k > 2 ** (m - 2):
                k -= 2 ** (m - 2)
                flag += 1
            m -= 1
        return flag % 2
        

    def kthGrammar1(self, n, k):
        if k == 1 or n == 1:
            return 0
        if k <= 3:
            return 1
        if k > 2 ** (n - 2):
            return 1 - self.kthGrammar(n - 1, k - 2 ** (n - 2))
        else:
            return self.kthGrammar(n - 1, k)


s = Solution()
for i in range(1, 17):
    print(s.kthGrammar(5, i), end="")
