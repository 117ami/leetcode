from collections import Counter

class Solution:
    def x(self, s):
        st = []
        for c in s:
            if c == '#':
                if len(st) > 0:
                    st.pop()
            else:
                st.append(c)
        return ''.join(st)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.x(S) == self.x(T)

S = "a##c"
T = "#a#c" 
print(Solution().backspaceCompare(S, T))