/*
 * @lc app=leetcode id=992 lang=javascript
 *
 * [992] Subarrays with K Different Integers
 *
 * https://leetcode.com/problems/subarrays-with-k-different-integers/description/
 *
 * algorithms
 * Hard (45.89%)
 * Total Accepted:    13.5K
 * Total Submissions: 29.3K
 * Testcase Example:  '[1,2,1,2,3]\n2'
 *
 * Given an array A of positive integers, call a (contiguous, not necessarily
 * distinct) subarray of A good if the number of different integers in that
 * subarray is exactly K.
 * 
 * (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
 * 
 * Return the number of good subarrays of A.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: A = [1,2,1,2,3], K = 2
 * Output: 7
 * Explanation: Subarrays formed with exactly 2 different integers: [1,2],
 * [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: A = [1,2,1,3,4], K = 3
 * Output: 3
 * Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
 * [2,1,3], [1,3,4].
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 20000
 * 1 <= A[i] <= A.length
 * 1 <= K <= A.length
 * 
 */
/**
 * @param {number[]} A
 * @param {number} K
 * @return {number}
 */

var atMostK = function(A, K) {
    let c = {},
        res = 0,
        i = 0;
    for (let j = 0; j < A.length; j += 1) {
        if (!(A[j] in c)) {
            c[A[j]] = 0;
        }

        if (c[A[j]] == 0) K -= 1;

        c[A[j]] += 1;
        while (K < 0) {
            c[A[i]] -= 1
            if (c[A[i]] == 0) {
                K += 1;
            }
            i += 1;
        }
        res += j - i + 1;
    }
    return res;
}


var subarraysWithKDistinct = function(A, K) {
    return atMostK(A, K) - atMostK(A, K - 1);
};

var A = [1, 2, 1, 2, 3],
    K = 2;
console.log(subarraysWithKDistinct(A, K))