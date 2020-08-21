
class Solution:
    """ Given a string S and a string T, find the minimum window in S which will
    contain all the characters in T in complexity O(n).
    """
    def minWindow(self, s: str, t: str) -> str:
        cc = Counter(t)  # Hash table to store char frequency
        unmatched_cnt = len(t)  # Total number of unmatched chars from t.
        start, end, left = 0, math.inf, 0

        for j, char in enumerate(s):
            if cc[char] > 0:
                unmatched_cnt -= 1
            cc[char] -= 1
            if unmatched_cnt == 0:  # All chars were matched
                # Remove chars not from t to find the real start. On existing
                # while loop, the code must stops on some letter c from t, as
                # for any c' in s - t, cc[c'] <= 0, and it equals 0 only
                # when s[i] in t.
                while left < j and cc[s[left]] < 0:
                    cc[s[left]] += 1
                    left += 1
                if j - left < end - start:  # Update window
                    start, end = left, j

        return s[start:end + 1] if end < math.inf else ""

