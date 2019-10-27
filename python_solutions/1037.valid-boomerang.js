/*
 * @lc app=leetcode id=1037 lang=javascript
 *
 * [1037] Valid Boomerang
 *
 * https://leetcode.com/problems/valid-boomerang/description/
 *
 * algorithms
 * Easy (37.36%)
 * Total Accepted:    11.1K
 * Total Submissions: 29.8K
 * Testcase Example:  '[[1,1],[2,3],[3,2]]'
 *
 * A boomerang is a set of 3 points that are all distinct and not in a straight
 * line.
 * 
 * Given a list of three points in the plane, return whether these points are a
 * boomerang.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [[1,1],[2,3],[3,2]]
 * Output: true
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [[1,1],[2,2],[3,3]]
 * Output: false
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * points.length == 3
 * points[i].length == 2
 * 0 <= points[i][j] <= 100
 * 
 * 
 * 
 * 
 * 
 */
/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function(points) {
    var a = points[0], b = points[1], c = points[2];
    return (a[0] - b[0]) * (c[1] - b[1]) != (c[0] - b[0]) * (a[1] - b[1])    ;
};
