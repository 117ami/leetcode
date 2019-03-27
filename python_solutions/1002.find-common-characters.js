/*
 * @lc app=leetcode id=1002 lang=javascript
 *
 * [1002] Find Common Characters
 *
 * https://leetcode.com/problems/find-common-characters/description/
 *
 * algorithms
 * Easy (67.79%)
 * Total Accepted:    11.9K
 * Total Submissions: 17.6K
 * Testcase Example:  '["bella","label","roller"]'
 *
 * Given an array A of strings made only from lowercase letters, return a list
 * of all characters that show up in all strings within the list (including
 * duplicates).  For example, if a character occurs 3 times in all strings but
 * not 4 times, you need to include that character three times in the final
 * answer.
 * 
 * You may return the answer in any order.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: ["bella","label","roller"]
 * Output: ["e","l","l"]
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["cool","lock","cook"]
 * Output: ["c","o"]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 100
 * 1 <= A[i].length <= 100
 * A[i][j] is a lowercase letter
 * 
 * 
 * 
 */
/**
 * @param {string[]} A
 * @return {string[]}
 */
var commonChars = function(a) {
    var h = {};
    for (var c of a[0]) h[c] = c in h ? h[c] + 1 : 1;
    var ans = [];
    Object.keys(h).forEach(function(c) {
        for (var w of a)
            h[c] = Math.min(h[c], w.split(c).length - 1);
        for (var i = 0; i < h[c]; i++) ans.push(c);
    });
    return ans;
};

var a = ["bella", "label", "roller"];
console.log(commonChars(a));