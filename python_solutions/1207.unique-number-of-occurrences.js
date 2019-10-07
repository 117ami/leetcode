/*
 * @lc app=leetcode id=1207 lang=javascript
 *
 * [1207] Unique Number of Occurrences
 *
 * https://leetcode.com/problems/unique-number-of-occurrences/description/
 *
 * algorithms
 * Easy (74.36%)
 * Total Accepted:    12.1K
 * Total Submissions: 16.3K
 * Testcase Example:  '[1,2,2,1,1,3]'
 *
 * Given an array of integers arr, write a function that returns true if and
 * only if the number of occurrences of each value in the array is unique.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [1,2,2,1,1,3]
 * Output: true
 * Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
 * values have the same number of occurrences.
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [1,2]
 * Output: false
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
 * Output: true
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 1000
 * -1000 <= arr[i] <= 1000
 * 
 * 
 */
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    let brr = Array(2001).fill(0);
    for (var i of arr) brr[i + 1000] += 1;

    let m = {};
    for (let i = 0; i < 2001; i++) {
        if (brr[i] > 0 && brr[i] in m) return false;
        m[brr[i]] = 0;
    }
    return true;
};

let arr = [1, 2, 3, 1, 2];
console.log(uniqueOccurrences(arr))