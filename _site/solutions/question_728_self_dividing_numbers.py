
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        r = []
        for n in range(left, right+1):
            v = True
            for i in list(str(n)):
                if i == '0' or n % int(i) != 0:
                    v = False
                    break
            if v: r.append(n)
        return r
        
print(Solution().selfDividingNumbers(1, 100))
