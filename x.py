
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        if n == 1: return True 
        ds = [int(e) for e in list(str(n))]
        while n != 1:
            n = sum(e * e for e in ds)
            if n in cache:
                return False
            cache.add(n)
            ds = [int(e) for e in list(str(n))]
        return True

n = 82
print(Solution().isHappy(n))


        