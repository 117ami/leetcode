'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4

'''

class Solution:
    def maximalSquare(self, matrix):
        if 0 == len(matrix):
            return 0
        ans = 0
        for i in range(1, len(matrix)):
            if '1' == matrix[i][0]: ans = max(ans, 1)
            for j in range(1, len(matrix[0])):
                if '1' == matrix[0][j]: ans = max(ans, 1)
                if int(matrix[i][j]) > 0 and int(matrix[i - 1][j - 1]) > 0:
                    matrix[i][j] = min([
                        int(n) for n in (matrix[i - 1][j - 1],
                                         matrix[i][j - 1], matrix[i - 1][j])
                    ]) + 1
                    ans = max(ans, matrix[i][j])
        return ans * ans

matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0'],
]

print(Solution().maximalSquare(matrix))
