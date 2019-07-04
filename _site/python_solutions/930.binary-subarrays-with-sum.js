/*
 * @lc app=leetcode id=930 lang=javascript
 *
 * [930] Binary Subarrays With Sum
 *
 * https://leetcode.com/problems/binary-subarrays-with-sum/description/
 *
 * algorithms
 * Medium (37.53%)
 * Total Accepted:    8.8K
 * Total Submissions: 23.4K
 * Testcase Example:  '[1,0,1,0,1]\n2'
 *
 * In an array A of 0s and 1s, how many non-empty subarrays have sum S?
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: A = [1,0,1,0,1], S = 2
 * Output: 4
 * Explanation: 
 * The 4 subarrays are bolded below:
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * A.length <= 30000
 * 0 <= S <= A.length
 * A[i] is either 0 or 1.
 * 
 */
/**
 * @param {number[]} A
 * @param {number} S
 * @return {number}
 */
var numSubarraysWithSum = function(A, S) {
    var c = {};
    c[0] = 1;
    var psum = res = 0;
    for (var a of A) {
        psum += a;
        res += (c[psum - S] || 0);
        c[psum] = psum in c ? c[psum] + 1 : 1;
    }
    return res;
};

var A = [1, 0, 1, 0, 1],
    S = 2;
console.log(numSubarraysWithSum(A, S));