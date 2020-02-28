/*
 * @lc app=leetcode id=1281 lang=rust
 *
 * [1281] Subtract the Product and Sum of Digits of an Integer
 *
 * https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
 *
 * algorithms
 * Easy (84.52%)
 * Total Accepted:    41.3K
 * Total Submissions: 48.9K
 * Testcase Example:  '234'
 *
 * Given an integer number n, return the difference between the product of its
 * digits and the sum of its digits.
 * 
 * Example 1:
 * 
 * 
 * Input: n = 234
 * Output: 15 
 * Explanation: 
 * Product of digits = 2 * 3 * 4 = 24 
 * Sum of digits = 2 + 3 + 4 = 9 
 * Result = 24 - 9 = 15
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 4421
 * Output: 21
 * Explanation: 
 * Product of digits = 4 * 4 * 2 * 1 = 32 
 * Sum of digits = 4 + 4 + 2 + 1 = 11 
 * Result = 32 - 11 = 21
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 10^5
 * 
 * 
 */
impl Solution {
    pub fn subtract_product_and_sum(n: i32) -> i32 {
        let (mut p, mut s, mut _n) = (1_i32, 0_i32, n) ; 
        while _n > 0 {
            p *= _n % 10; 
            s += _n % 10; 
            _n /= 10; 
        }
        p - s 
    }
}
// pub structSolution; 
