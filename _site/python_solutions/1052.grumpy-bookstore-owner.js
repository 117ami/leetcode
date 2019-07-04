/*
 * @lc app=leetcode id=1052 lang=javascript
 *
 * [1052] Grumpy Bookstore Owner
 *
 * https://leetcode.com/problems/grumpy-bookstore-owner/description/
 *
 * algorithms
 * Medium (48.54%)
 * Total Accepted:    3K
 * Total Submissions: 6.2K
 * Testcase Example:  '[1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3'
 *
 * Today, the bookstore owner has a store open for customers.length minutes.
 * Every minute, some number of customers (customers[i]) enter the store, and
 * all those customers leave after the end of that minute.
 * 
 * On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
 * grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the
 * bookstore owner is grumpy, the customers of that minute are not satisfied,
 * otherwise they are satisfied.
 * 
 * The bookstore owner knows a secret technique to keep themselves not grumpy
 * for X minutes straight, but can only use it once.
 * 
 * Return the maximum number of customers that can be satisfied throughout the
 * day.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
 * Output: 16
 * Explanation: The bookstore owner keeps themselves not grumpy for the last 3
 * minutes. 
 * The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 +
 * 5 = 16.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= X <= customers.length == grumpy.length <= 20000
 * 0 <= customers[i] <= 1000
 * 0 <= grumpy[i] <= 1
 * 
 */
/**
 * @param {number[]} customers
 * @param {number[]} grumpy
 * @param {number} X
 * @return {number}
 */
var maxSatisfied = function(customers, grumpy, x) {
    var sum = customers.reduce((a, b) => a + b, 0),
        lost = 0,
        res = 0;
    for (var i = x; i < customers.length; i++)
        lost += grumpy[i] * customers[i];
    res = sum - lost;

    for (var i = 1; i <= customers.length - x; i++) {
        lost += grumpy[i - 1] * customers[i - 1] - grumpy[i + x - 1] * customers[i + x - 1];
        res = Math.max(res, sum - lost);
    }
    return res;
};

var print = function(a) {
    console.log(a);
}