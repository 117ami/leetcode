from collections import Counter, defaultdict
true = True
false = False
#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (56.38%)
# Total Accepted:    26.4K
# Total Submissions: 46.8K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to
# make two strings equal.
# 
# Example 1:
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# 
# 
# Example 2:
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e]
# to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
# 
# 
# 
# Note:
# 0 < s1.length, s2.length .
# All elements of each string will have an ASCII value in [97, 122]. 
# 
#

class XString(object):
    def is_p(self, s):
        """ is palindrome
        type s: string
        rtype : boolean
        """
        if len(s) <= 1:
            return True
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    def lcslen(self, word1, word2):
        """ longest common substring
        :type word1: str
        :type word2: str
        :rtype: int
        :return the length of longest common substring, e.g, m('1a2b3c4d', 'a5b6c777d88') return 4 (length of 'abcd')
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return 0

        dp = [0] * n
        res = 0
        for i, a in enumerate(word1):
            cur_max = 1
            for j, b in enumerate(word2):
                aux = dp[j]
                if a == b:
                    dp[j] = cur_max
                if aux + 1 > cur_max:
                    cur_max = aux + 1
                res = max(res, dp[j])
        return res

    def lcs(self, s, t):
        """ return the longest common substring
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j, idx = m, n, dp[-1][-1]
        res = ['#'] * idx

        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                res[idx - 1] = s[i - 1]
                idx -= 1
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return ''.join(res)

    def find_all_lcs(self, s, t):
        """ Find all lcs whether there are multiple choices
        return type: set<string>
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        memo = {}
        
        def helper(i, j):
            if (i, j) in memo: return memo[(i, j)]

            res = set()
            if i == 0 or j == 0:
                res.add("")
                return res

            if s[i - 1] == t[j - 1]:
                tmp = helper(i - 1, j - 1)
                for rs in tmp:
                    res.add(rs + s[i - 1])
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    res.update(helper(i - 1, j))

                if dp[i - 1][j] <= dp[i][j - 1]:
                    res.update(helper(i, j - 1))
            
            memo[(i, j)] = res 
            return res

        return helper(m, n)

xs = XString()

class Solution:
    def minimumDeleteSum_dp(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j - 1])
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        
        return dp[m][n]
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [0] * (n+1)
        for j in range(1, n + 1):
            dp[j] = dp[j-1] + ord(s2[j - 1])
        
        for i in range(1, m + 1):
            tmp = dp[:]
            dp[0] += ord(s1[i-1])
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j-1]:
                    dp[j] = tmp[j - 1]
                else:
                    dp[j] = min(tmp[j] + ord(s1[i-1]), dp[j-1] + ord(s2[j-1]))
        
        return dp[n]
        
s = Solution()
s1, s2 = 'delete', 'leet'
# s1, s2 = 'ap#-ba', 'bp*a+b'
# s1, s2 = 'eat', 'sea'
s1 = "igijekdtywibepwonjbwykkqmrgmtybwhwjiqudxmnniskqjfbkpcxukrablqmwjndlhblxflgehddrvwfacarwkcpmcfqnajqfxyqwiugztocqzuikamtvmbjrypfqvzqiwooewpzcpwhdejmuahqtukistxgfafrymoaodtluaexucnndlnpeszdfsvfofdylcicrrevjggasrgdhwdgjwcchyanodmzmuqeupnpnsmdkcfszznklqjhjqaboikughrnxxggbfyjriuvdsusvmhiaszicfa"
s2 = "ikhuivqorirphlzqgcruwirpewbjgrjtugwpnkbrdfufjsmgzzjespzdcdjcoioaqybciofdzbdieegetnogoibbwfielwungehetanktjqjrddkrnsxvdmehaeyrpzxrxkhlepdgpwhgpnaatkzbxbnopecfkxoekcdntjyrmmvppcxcgquhomcsltiqzqzmkloomvfayxhawlyqxnsbyskjtzxiyrsaobbnjpgzmetpqvscyycutdkpjpzfokvi"
print(s.minimumDeleteSum(s1, s2))
print(s.minimumDeleteSum2(s1, s2))
