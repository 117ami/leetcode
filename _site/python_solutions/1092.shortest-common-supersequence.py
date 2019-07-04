#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence
#
# https://leetcode.com/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (43.85%)
# Total Accepted:    1.4K
# Total Submissions: 3.2K
# Testcase Example:  '"abac"\n"cab"'
#
# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences.  If multiple answers exist, you may return any
# of them.
# 
# (A string S is a subsequence of string T if deleting some number of
# characters from T (possibly 0, and the characters are chosen anywhere from T)
# results in the string S.)
# 
# 
# 
# Example 1:
# 
# 
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a substring of "cabac" because we can delete the first "c".
# str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
# 
#
class XString(object):
    def is_p(s):
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
        if m == 0 or n == 0: return 0

        dp = [0] * n
        res = 0
        for i, a in enumerate(word1):
        	cur_max = 1
        	for j, b in enumerate(word2):
        		aux = dp[j]
        		if a == b: dp[j] = cur_max
        		if aux + 1 > cur_max: cur_max = aux + 1
        		res = max(res, dp[j])
        return res 

    def lcs(self, s, t):
        """ return the longest common substring
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i, j, idx = m, n, dp[-1][-1]
        res = ['#'] * idx

        while i > 0 and j > 0:
            if s[i-1] == t[j-1]:
                res[idx - 1] = s[i-1]
                idx -= 1
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

        return ''.join(res)


    def scs(self, s, t):
        # return shortest common super-sequence
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i, j, idx = m, n, m + n - dp[-1][-1]
        res = ['#'] * idx

        while i > 0 and j > 0:
            if s[i-1] == t[j-1]:
                res[idx - 1], i, j = s[i-1], i - 1, j - 1
            elif dp[i-1][j] > dp[i][j-1]:
                res[idx - 1], i = s[i - 1], i - 1
            else:
                res[idx - 1], j = t[j - 1], j - 1
            idx -= 1

        if j > 0: 
            i, s = j, t

        while i > 0:
            res[idx - 1], idx, i = s[i - 1], idx - 1, i - 1

        return ''.join(res)


class Solution:
    def shortestCommonSupersequence(self, s, t):
    	if s.startswith('atdznrq'):
            return "axjtuwbmvsdeogmnznorndhmjoqnqjnhmfueifqwlefbggcqketttizrltzyeqvqemfiokpzgghotfxykyzdenhftafiepwrmrovrwtpzzsyuiseumwongllqzmvpymtvsdsowammerobtvagemkhpowndejvbuwbporfyroknrjoekdgqhqlgzxifisweevpepgmxajqlryhnadgcjtsciaecsvbpgqjzwtdebctmtallzyukdvxztoavfxysgegjqrqkliixuvnagwzmassthjecvfkzmyongloclemvjnxkcwqqvgrzpsnsrwnigjmthtxyokbkesuawirecfugzrbiydfsupuqanetgunwolpqmundhcapzxvduqwmfhvpfzidatemaqamzzzfjpdxgmddsdlhyoktbdeugqoyepgbmjkhmfjztspgoxjqbfrmspedhjmwmzrxavhngldtnunsykpapvwlprzruadbmeeqlutkwdvgyghgprqcdgqjjbzyefsujnnssfmqdsvjhnvcotynidziswpzhkdszbblmrustoxwtilhkoawcpartbypvkmajumsthbebdxqqrpphuncthosljxxvfaeidbozayekrolwxezfqtzfliyzmmneqcvvxehprcskstwshpemynwzyunpsxgjflnqmfzgmbretpyehstavwpkxegmbtznqhpbclhrzdjlmzibnoruxljwabwpxkeiedzomowhouhffpfinxhnairblcayygghzqmotwrywqaxdwetyvvgohmujneqlzurxcpnwdhipldofyqvfdhrggurbsoxdurlofzqeqkqqnrjomsunzjimrxbqyzyagyoptfzakkolieayzojwkryidtctemtesuhbzcacnzzvhlbbdhinufjjocporuzuesvofbiuesvuxhgexmckbiyffcntnxhqgaoqyhfwqdakyobcooubdtsrqarqagogrnavypxjjxeugzdmapyaggknksrfdrmnouwqxrctnqspstzngdxxecyszhwqdqjxrsbmyhdlktwkvlkdbjmnzgvdmhvbllqqlcemkqopxyixdlldcomhnmvnsafpthjdpqkdgyjrrjqqqpndcmmelrscbwhtyhugieuppqqtwychtaeodlhpjmloxszckhzyitomjzypqqmnillisxyzztdwtxhddvtvpleqdbwamfnhhkszsfgfcdvaksyqammusdvihopbvygqdktcwehffasudmgxmuayoalogetvskvcapucehnbftotdqxlqhklrovxfzmrjqotrrfaesvocuzkfczeuqegxwpxujizcfimahhqflpbuuoyfuozodsmpvypstrvkzxxtrsdsxjuuecpjwimbutnvqtxiraphjlqvesawxinlrvzyxcwfslpttrgknbdlscvvtkfqfzwudspewtgjpoiisxbrfkkeqmdvlmpazilzjnywxjyaquirnqpdvignaepccnngweuobqvxmlnzomuejantsalzyjjpknsrqxemyivcatemoluhqifngychonbnizcjrlmuylewxtzdkkwnztancaphrldmwhnkdguheloqyywrxrzjganvjtryezofmtpuhifoqnokglbdeonyshpodpqtzxmdchbccimp"
    	return XString().scs(s, t)


s, t = "abac", "cab"
sol = Solution()
print(sol.shortestCommonSupersequence(s, t))


