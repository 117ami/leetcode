/*
 * @lc app=leetcode id=1015 lang=javascript
 *
 * [1015] Numbers With Repeated Digits
 *
 * https://leetcode.com/problems/numbers-with-repeated-digits/description/
 *
 * algorithms
 * Hard (33.80%)
 * Total Accepted:    1.8K
 * Total Submissions: 5.3K
 * Testcase Example:  '20'
 *
 * Given a positive integer N, return the number of positive integers less than
 * or equal to N that have at least 1 repeated digit.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: 20
 * Output: 1
 * Explanation: The only positive number (<= 20) with at least 1 repeated digit
 * is 11.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 100
 * Output: 10
 * Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are
 * 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 1000
 * Output: 262
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= N <= 10^9
 * 
 * 
 * 
 * 
 */
/**
 * @param {number} N
 * @return {number}
 */
var numDupDigitsAtMostN = function(N) {
    var digits = (N + 1).toString().split('').map(Number);
    var size = digits.length;
    var perm = function(m, n) {
        return n == 0 ? 1 : perm(m, n - 1) * (m - n + 1);
    }

    var res = 0,
        seen = [];
    for (var i = 1; i < size; i++) res += 9 * perm(9, i - 1);
    // console.log(digits, res);

    for (var i = 0; i < size; i++) {
        var x = digits[i];
        var y = i == 0 ? 1 : 0;
        for (; y < x; y++) {
            if (!seen[y]) res += perm(9 - i, size - i - 1);
        }
        if (seen[x]) break;
        seen[x] = true;
    }
    return N - res;
};

console.log(numDupDigitsAtMostN(1000));