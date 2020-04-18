import string
from typing import List

class KMP():
    def get_lps(self, t: str) -> List[int]:
        '''Compute the length of longest proper prefix-suffix for each t[:i], i \in [1..len(t)],
        where a prefix-suffix of t is a substring, u, of t s.t., t.startswith(u) and t.endswith(u).
        And proper means, len(u) < len(t), i.e., u != t
        '''
        n, i, pre_len = len(t), 1, 0
        lps = [0] * n
        while i < n:
            if t[i] == t[pre_len]:
                pre_len += 1
                lps[i] = pre_len
                i += 1
            else:
                if pre_len == 0:
                    lps[i] = 0
                    i += 1
                else:
                    pre_len = lps[pre_len - 1]
                    # Note that we do not increment i here
        return lps

    def pattern_search(self, s: str, t: str) -> List[int]:
        """KMP (Knuth Morris Pratt) Pattern Searching
        Return a list of indexes i, such that t occurs in s starting from i.
        """
        i, j, m, n = 0, 0, len(s), len(t)
        lps = self.get_lps(t)
        res = []
        while i < m:
            if s[i] == t[j]:
                i, j = i + 1, j + 1
            if j == n:
                res.append(i - n)
                j = lps[j - 1]

            elif i < m and s[i] != t[j]:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
        return res


s = "AABAACAABAA"
t = "AB"
kmp = KMP()
print(kmp.pattern_search(s, t))

t = "abcdabx"
print(kmp.get_lps(t))
