/*
 * @lc app=leetcode id=905 lang=rust
 *
 * [905] Sort Array By Parity
 *
 * https://leetcode.com/problems/sort-array-by-parity/description/
 *
 * algorithms
 * Easy (73.66%)
 * Total Accepted:    160.9K
 * Total Submissions: 218.5K
 * Testcase Example:  '[3,1,2,4]'
 *
 * Given an array A of non-negative integers, return an array consisting of all
 * the even elements of A, followed by all the odd elements of A.
 * 
 * You may return any answer array that satisfies this condition.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [3,1,2,4]
 * Output: [2,4,3,1]
 * The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 5000
 * 0 <= A[i] <= 5000
 * 
 * 
 * 
 */
impl Solution {
    pub fn sort_array_by_parity(mut a: Vec<i32>) -> Vec<i32> {
        // a.sort_by(|x, y| (x & 1).cmp(&(y & 1)));
        let (mut l, mut r) = (0, a.len() - 1);
        loop {
            if l == r {break; }
            if a[l] & 1 == 1 {
                a.swap(l, r);
                r -= 1 ;
            } else {l += 1;}
        } 
        a 
    }
}
// pub structSolution; 
