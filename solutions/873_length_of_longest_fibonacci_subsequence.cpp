#include "aux.cpp"
/**
A sequence X_1, X_2, ..., X_nis fibonacci-like if:
        n >= 3
        X_i + X_{i+1} = X_{i+2}for alli + 2 <= n
Given a strictly increasingarrayA of positive integers forming a sequence, find
the length of the longest fibonacci-like subsequence of A. If one does not
exist, return 0.
(Recall that a subsequence is derived from another sequence A bydeleting any
number ofelements (including none)from A, without changing the order of the
remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7,
8].)

Example 1:
Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:
Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].

Note:
        3 <= A.length <= 1000
        1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
        (The time limit has been reduced by 50% for submissions in Java, C, and
C++.)

 https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int lenLongestFibSubseq(vector<int> &A) {
    int res = 0;
    int xsize = A.size();
    vector<vector<int>> dp(xsize, vector<int>(xsize, 2));
    map<int, int> cache;
    for (int i = 0; i < xsize; i++)
      cache[A[i]] = i;

    for (int i = 1; i < xsize; i++)
      for (int j = i + 1; j < xsize; j++)
        if (cache.find(A[j] - A[i]) != cache.end() && cache[A[j] - A[i]] < i) {
          dp[i][j] = max(dp[i][j], 1 + dp[cache[A[j] - A[i]]][i]);
          res = max(res, dp[i][j]);
        }

    return res > 2 ? res : 0;
  }
};

int main() {
  Solution s;
  vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8};
  arr = {2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50};
  say(s.lenLongestFibSubseq(arr));
}
