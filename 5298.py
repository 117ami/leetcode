true = True 
false = False 
from functools import reduce

class Solution:
    def isSolvable(self, ws, re):
        digits = set (range(10))
        chars = set(list(re))
        for w in words:
            chars.update(list(w))

        def getsum(expr, amap):
            return reduce(lambda a, b: a * 10 + b, map(lambda c: amap[c], re))
        
        def valid(amap):
            return getsum(re, amap) == sum([getsum(ss, amap) for ss in ws])
    
        # amap = {'M':0, 'O':8, 'N':3, 'E':2, 'Y':1}
        # print(valid(amap))

        def dfs(restchars, restdigits, amap):
            if not restchars:
                print(amap, restdigits)
                if valid(amap): return true 
                return false 
            
            c = restchars.pop()
            for d in restdigits:
                restdigits.remove(d)
                print(restdigits)
                nextmap = amap.copy()
                nextmap[c] = d 
                if dfs(restchars, restdigits, nextmap):
                    return true 
                del nextmap[c]
                restdigits.add(d)
            
            return false 

        restchars = sorted(list(chars))
        return dfs(restchars, digits, {})

        


sol = Solution()
words, result = ["SEND","MORE"], "MONEY"
print(sol.isSolvable(words, result))