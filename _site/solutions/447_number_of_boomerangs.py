'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
Example:
Input:
[[0,0],[1,0],[2,0]]
Output:
2
Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

'''


class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            boom = {}
            for q in points:
                a = p[0] - q[0]
                b = p[1] - q[1]
                d = a * a + b * b
                boom[d] = 1 + boom.get(d, 0)
            for v in boom.values():
                res += v * (v - 1)
        return res


points = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]
s = Solution()
print(s.numberOfBoomerangs(points))
