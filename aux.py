#!/user/bin/python3

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

    def lcs(self, word1, word2):
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

