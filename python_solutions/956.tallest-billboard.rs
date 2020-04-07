/*
 * @lc app=leetcode id=956 lang=rust
 *
 * [956] Tallest Billboard
 *
 * https://leetcode.com/problems/tallest-billboard/description/
 *
 * algorithms
 * Hard (38.71%)
 * Total Accepted:    6K
 * Total Submissions: 15.4K
 * Testcase Example:  '[1,2,3,6]'
 *
 * You are installing a billboard and want it to have the largest height.  The
 * billboard will have two steel supports, one on each side.  Each steel
 * support must be an equal height.
 * 
 * You have a collection of rods which can be welded together.  For example, if
 * you have rods of lengths 1, 2, and 3, you can weld them together to make a
 * support of length 6.
 * 
 * Return the largest possible height of your billboard installation.  If you
 * cannot support the billboard, return 0.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,3,6]
 * Output: 6
 * Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the
 * same sum = 6.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [1,2,3,4,5,6]
 * Output: 10
 * Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the
 * same sum = 10.
 * 
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [1,2]
 * Output: 0
 * Explanation: The billboard cannot be supported, so we return 0.
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 0 <= rods.length <= 20
 * 1 <= rods[i] <= 1000
 * The sum of rods is at most 5000.
 * 
 * 
 */
// pub struct Solution(); 

impl Solution {
    pub fn tallest_billboard(rods: Vec<i32>) -> i32 {
        let _sum: i32 = rods.iter().sum();
        let mut dp: Vec<i32> = vec![-1; _sum as usize + 1];
        dp[0] = 0; 
        
        for r in &rods{
            let cur = dp.to_vec(); 
            for i in 0.._sum {
                if cur[i as usize] == -1 { continue; }
                if i + r <= _sum { dp[(r + i) as usize] = std::cmp::max(dp[(r+i) as usize], cur[i as usize]); }
                dp[(r-i).abs() as usize] = std::cmp::max(dp[(r-i).abs() as usize], cur[i as usize] + std::cmp::min(i, *r));
            }
        }
        dp[0]
    }
}


