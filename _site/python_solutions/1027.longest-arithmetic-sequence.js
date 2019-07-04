/*
 * @lc app=leetcode id=1027 lang=javascript
 *
 * [1027] Longest Arithmetic Sequence
 *
 * https://leetcode.com/problems/longest-arithmetic-sequence/description/
 *
 * algorithms
 * Medium (43.04%)
 * Total Accepted:    4.2K
 * Total Submissions: 9.6K
 * Testcase Example:  '[3,6,9,12]'
 *
 * Given an array A of integers, return the length of the longest arithmetic
 * subsequence in A.
 * 
 * Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0
 * <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is
 * arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length -
 * 1).
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [3,6,9,12]
 * Output: 4
 * Explanation: 
 * The whole array is an arithmetic sequence with steps of length = 3.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [9,4,7,2,10]
 * Output: 3
 * Explanation: 
 * The longest arithmetic subsequence is [4,7,10].
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [20,1,15,3,10,5,8]
 * Output: 4
 * Explanation: 
 * The longest arithmetic subsequence is [20,15,10,5].
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 2 <= A.length <= 2000
 * 0 <= A[i] <= 10000
 * 
 * 
 */
/**
 * @param {number[]} A
 * @return {number}
 */
var longestArithSeqLength = function(A) {
    var dp = {},
        res = 2;
    for (var i = 0; i < A.length; i++)
        for (var j = i + 1; j < A.length; j++) {
            var d = A[j] - A[i];
            if (d in dp) {
                if (i in dp[d]) dp[d][j] = dp[d][i] + 1;
                else dp[d][j] = 2;
            } else {
                dp[d] = {};
                dp[d][j] = 2;
            }
            res = Math.max(res, dp[d][j]);
        }
    return res;
};


a = [20, 1, 15, 3, 10, 5, 8];
console.log(longestArithSeqLength(a));