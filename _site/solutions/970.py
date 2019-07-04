
from math import log


class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ibound = 1 if x == 1 else int(log(bound, x))
        jbound = 1 if y == 1 else int(log(bound, y))
        res = set()
        for i in range(ibound + 1):
            for j in range(jbound + 1):
                tn = x ** i + y ** j
                if tn > bound:
                    break
                res.add(tn)

        return list(res)


x = 1
y = 2
bound = 100
print(Solution().powerfulIntegers(x, y, bound))
