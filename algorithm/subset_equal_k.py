"""
Given a list (or set) arr and an integer n, find out where there is a 
subarray (not necessarily continuous) whose sum is exactly n ?
Example :  [1,2,3,4,5,6,7,8], 13
Output: true
There are multiple subarrays,[3, 4, 7], [6, 7], [1, 2, 3, 7], ...

This problem is NP-Complete, there is no known polynomial solution to this 
problem. A general way to deal with this type of problem is dynamic programming.

This method creates a 2D array of size (arr.size() + 1) * (target + 1) of type boolean. 
The state DP[i][j] is true if there exists a subset from A[0….i] with sum j. 
The new sum j + 1 is computed following:
1. if A[i] > j: dp[i][j] == dp[i-1][j]
2. else: dp[i][j] == dp[i-1][j] or dp[i-1][j-A[i]]

Time complexity: n * sum
Space complexity: n * sum, or O(sum) if we use a single list
"""
from typing import List

def subset_equal_k(arr: List[int], M: int) -> bool:
    n = len(arr)
    #  dp = [[False] * (M+1) for _ in range(n + 1)]
    dp = [False] * (M + 1)
    dp[0] = True

    for i in range(1, n + 1):
        pre = dp.copy()
        for j in range(1, M + 1):
            if arr[i - 1] > j:
                dp[j] = pre[j]
                # dp[i][j] = dp[i - 1][j]
            else:
                dp[j] = pre[j] or pre[j - arr[i - 1]]
                # dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
    # return dp[-1][-1]
    return dp.pop()


if __name__ == "__main__":
    arr = [1, 3, 4, 27, 23, 12, 8]
    M = 57
    print(subset_equal_k(arr, M))
