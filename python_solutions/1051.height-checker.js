/*
 * @lc app=leetcode id=1051 lang=javascript
 *
 * [1051] Height Checker
 *
 * https://leetcode.com/problems/height-checker/description/
 *
 * algorithms
 * Easy (68.73%)
 * Total Accepted:    3.1K
 * Total Submissions: 4.5K
 * Testcase Example:  '[1,1,4,2,1,3]'
 *
 * Students are asked to stand in non-decreasing order of heights for an annual
 * photo.
 * 
 * Return the minimum number of students not standing in the right positions.
 * (This is the number of students that must move in order for all students to
 * be standing in non-decreasing order of height.)
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,1,4,2,1,3]
 * Output: 3
 * Explanation: 
 * Students with heights 4, 3 and the last 1 are not standing in the right
 * positions.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= heights.length <= 100
 * 1 <= heights[i] <= 100
 * 
 */
/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    var heights_copy = heights.slice();
    heights.sort((a, b) => (a - b));
    // print(heights);
    var res = 0;
    for (var i = 0; i < heights.length; i++)
        if (heights[i] != heights_copy[i])
            res += 1;
    return res;
};

var print = function(a) {
    console.log(a);
}

var heights = [1, 1, 4, 2, 1, 3];
heights = [10, 6, 6, 10, 10, 9, 8, 8, 3, 3, 8, 2, 1, 5, 1, 9, 5, 2, 7, 4, 7, 7];
print(heightChecker(heights));