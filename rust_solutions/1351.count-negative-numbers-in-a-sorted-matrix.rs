/*
 * @lc app=leetcode id=1351 lang=rust
 *
 * [1351] Count Negative Numbers in a Sorted Matrix
 *
 * https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
 *
 * algorithms
 * Easy (81.18%)
 * Total Accepted:    16.4K
 * Total Submissions: 20.5K
 * Testcase Example:  '[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]'
 *
 * Given a m * n matrix grid which is sorted in non-increasing order both
 * row-wise and column-wise. 
 * 
 * Return the number of negative numbers in grid.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
 * Output: 8
 * Explanation: There are 8 negatives number in the matrix.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: grid = [[3,2],[1,0]]
 * Output: 0
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: grid = [[1,-1],[-1,-1]]
 * Output: 3
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: grid = [[-1]]
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 100
 * -100 <= grid[i][j] <= 100
 * 
 */
impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut res = 0; 
        for row in grid {
            res += row.iter().filter(|n| **n < 0).collect::<Vec<_>>().len() as i32;
        }
        res as i32 
    }
}
// pub structSolution; 
