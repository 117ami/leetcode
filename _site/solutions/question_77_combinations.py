
class Solution:
    def loop(self, arr, k):
        if k > len(arr):
            return []
        elif k == len(arr):
            return [arr]
        elif k == 1:
            return [[i] for i in arr]
        else:
            r = []
            for i in range(len(arr)):
                for e in self.loop(arr[i+1:], k - 1):
                    r.append([arr[i]] + e)
            return r
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        a = list(range(1, n + 1))
        print(self.loop(a, k))
        


Solution().combine(6, 2)

