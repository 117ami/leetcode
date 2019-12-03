# https://leetcode.com/problems/palindrome-partitioning-iii
# Hard (Difficulty)

# You are given a string s containing lowercase letters and an integer k. You need to :
# Return the minimal number of characters that you need to change to divide the string.
#  
# Example 1:
# Example 2:
# Example 3:
#  
# Constraints:
# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
#
# Input: s = "aabbc", k = 3
# Output: 0
# Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
# Input: s = "leetcode", k = 8
# Output: 0
#
# xxxxxxxxxx
# class Solution {
# public:
#     int palindromePartition(string s, int k) {
#         
#     }
# };

from functools import lru_cache

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}

        @lru_cache(None)
        def cost(s, i, j):
            r = 0 
            while i < j:
                r += 0 if s[i] == s[j] else 1
                i += 1
                j -= 1
            return r 
        
        @lru_cache(None)
        def dfs(i, k):
            if (i, k) in memo: return memo[(i, k)]
            if n - i == k: return 0
            if k == 1: return cost(s, i, n - 1)
            
            ans = n
            for j in range(i + 1, n - k + 2):
                ans = min(ans, cost(s, i, j - 1) + dfs(j, k - 1))
            memo[(i, k)] = ans 
            return ans 

        return dfs(0, k)


ss, k = "aabbc", 3
ss, k = "abc", 2
ss, k = "oiwwhqjkb", 1
# ss, k = "fyhowoxzyrincxivwarjuwxrwealesxsimsepjdqsstfggjnjhilvrwwytbgsqbpnwjaojfnmiqiqnyzijfmvekgakefjaxryyml", 32
# ss, k = "dlalkdlajflsdjakldjfljfldjsflsdfjlsjfdsbbc", 7
# ss, k = "leetcode", 8
sol = Solution()
print(sol.palindromePartition(ss, k))
