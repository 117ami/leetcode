/*
 * @lc app=leetcode id=970 lang=javascript
 *
 * [970] Powerful Integers
 *
 * https://leetcode.com/problems/powerful-integers/description/
 *
 * algorithms
 * Easy (39.62%)
 * Total Accepted:    15.1K
 * Total Submissions: 38.2K
 * Testcase Example:  '2\n3\n10'
 *
 * Given two positive integers x and y, an integer is powerful if it is equal
 * to x^i + y^j for some integers i >= 0 and j >= 0.
 * 
 * Return a list of all powerful integers that have value less than or equal to
 * bound.
 * 
 * You may return the answer in any order.  In your answer, each value should
 * occur at most once.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: x = 2, y = 3, bound = 10
 * Output: [2,3,4,5,7,9,10]
 * Explanation: 
 * 2 = 2^0 + 3^0
 * 3 = 2^1 + 3^0
 * 4 = 2^0 + 3^1
 * 5 = 2^1 + 3^1
 * 7 = 2^2 + 3^1
 * 9 = 2^3 + 3^0
 * 10 = 2^0 + 3^2
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: x = 3, y = 5, bound = 15
 * Output: [2,4,6,8,10,14]
 * 
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= x <= 100
 * 1 <= y <= 100
 * 0 <= bound <= 10^6
 * 
 */
/**
 * @param {number} x
 * @param {number} y
 * @param {number} bound
 * @return {number[]}
 */
var powerfulIntegers = function(x, y, bound) {
    let xup = 1,
        yup = 1,
        tmp = x * x;
    while (x > 1 && tmp <= bound) {
        tmp *= x;
        xup += 1;
    }
    tmp = y * y;
    while (y > 1 && tmp <= bound) {
        tmp *= y;
        yup += 1;
    }
    var res = new Set();
    for (let i = 0; i <= xup; i += 1)
        for (let j = 0; j <= yup; j += 1) {
            tmp = Math.pow(x, i) + Math.pow(y, j);
            if (tmp <= bound)
                res.add(tmp);
        }
    return [...res];
};

console.log(powerfulIntegers(2, 3, 10))