/*
 * @lc app=leetcode id=1033 lang=javascript
 *
 * [1033] Moving Stones Until Consecutive
 *
 * https://leetcode.com/problems/moving-stones-until-consecutive/description/
 *
 * algorithms
 * Easy (28.39%)
 * Total Accepted:    2.5K
 * Total Submissions: 8.9K
 * Testcase Example:  '1\n2\n5'
 *
 * Three stones are on a number line at positions a, b, and c.
 * 
 * Each turn, let's say the stones are currently at positions x, y, z with x <
 * y < z.  You pick up the stone at either position x or position z, and move
 * that stone to an integer position k, with x < k < z and k != y.
 * 
 * The game ends when you cannot make any more moves, ie. the stones are in
 * consecutive positions.
 * 
 * When the game ends, what is the minimum and maximum number of moves that you
 * could have made?  Return the answer as an length 2 array: answer =
 * [minimum_moves, maximum_moves]
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: a = 1, b = 2, c = 5
 * Output: [1, 2]
 * Explanation: Move stone from 5 to 4 then to 3, or we can move it directly to
 * 3.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: a = 4, b = 3, c = 2
 * Output: [0, 0]
 * Explanation: We cannot make any moves.
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= a <= 100
 * 1 <= b <= 100
 * 1 <= c <= 100
 * a != b, b != c, c != a
 * 
 */
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number[]}
 */
var numMovesStones = function(a, b, c) {
    var arr = [a, b, c];
    arr.sort((x, y) => (x - y));
    f = (arr[2] - arr[1] <= 2 || arr[1] - arr[0] <= 2) ? 1 : 2;
    f = (arr[2] - arr[1] == 1 && arr[1] - arr[0] == 1) ? 0 : f;
    return [f, arr[2] - arr[0] - 2];
};

console.log(numMovesStones(5, 2, 1))