/*
 * @lc app=leetcode id=1266 lang=rust
 *
 * [1266] Minimum Time Visiting All Points
 *
 * https://leetcode.com/problems/minimum-time-visiting-all-points/description/
 *
 * algorithms
 * Easy (79.29%)
 * Total Accepted:    26K
 * Total Submissions: 32.8K
 * Testcase Example:  '[[1,1],[3,4],[-1,0]]'
 *
 * On a plane there are n points with integer coordinates points[i] = [xi, yi].
 * Your task is to find the minimum time in seconds to visit all points.
 * 
 * You can move according to the next rules:
 * 
 * 
 * In one second always you can either move vertically, horizontally by one
 * unit or diagonally (it means to move one unit vertically and one unit
 * horizontally in one second).
 * You have to visit the points in the same order as they appear in the
 * array.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: points = [[1,1],[3,4],[-1,0]]
 * Output: 7
 * Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3]
 * -> [1,2] -> [0,1] -> [-1,0]   
 * Time from [1,1] to [3,4] = 3 seconds 
 * Time from [3,4] to [-1,0] = 4 seconds
 * Total time = 7 seconds
 * 
 * Example 2:
 * 
 * 
 * Input: points = [[3,2],[-2,2]]
 * Output: 5
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * points.length == n
 * 1 <= n <= 100
 * points[i].length == 2
 * -1000 <= points[i][0], points[i][1] <= 1000
 * 
 * 
 */
impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut p = &points[0];
        points.iter().fold(0, |acc, pi| {
            let (dx, dy) = (p[0] - pi[0], p[1] - pi[1]); 
            p = pi ; 
            acc + std::cmp::max(dx.abs(), dy.abs())
        })
        // for i in 1..points.len() {
        //     let (i, j, k, l) = (points[i-1][0], points[i-1][1], points[i][0], points[i][1]);
        //     res += std::cmp::max((k - i).abs(), (l - j).abs());
        // }
        // res 
    }
}
pub struct Solution; 
