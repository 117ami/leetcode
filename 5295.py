class Solution:
    def sumZero(self, n):
        res = []
        i = 1
        while len(res) < n - 1:
            res += [i, -i]
            i += 1
        return res if len(res) == n else res + [0]

sol = Solution()
print(sol.sumZero(4))        

        