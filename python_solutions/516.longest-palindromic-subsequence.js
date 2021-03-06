/*
 * @lc app=leetcode id=516 lang=javascript
 *
 * [516] Longest Palindromic Subsequence
 *
 * https://leetcode.com/problems/longest-palindromic-subsequence/description/
 *
 * algorithms
 * Medium (46.30%)
 * Total Accepted:    58.1K
 * Total Submissions: 125.5K
 * Testcase Example:  '"bbbab"'
 *
 * 
 * Given a string s, find the longest palindromic subsequence's length in s.
 * You may assume that the maximum length of s is 1000.
 * 
 * 
 * Example 1:
 * Input: 
 * 
 * "bbbab"
 * 
 * Output: 
 * 
 * 4
 * 
 * One possible longest palindromic subsequence is "bbbb".
 * 
 * 
 * Example 2:
 * Input:
 * 
 * "cbbd"
 * 
 * Output:
 * 
 * 2
 * 
 * One possible longest palindromic subsequence is "bb".
 * 
 */
/**
 * @param {string} s
 * @return {number}
 */
var longestPalindromeSubseq = function(s) {
    var cur = new Array(s.length).fill(0);
    for (var i = s.length - 1; i >= 0; i--) {
        var pre = cur.slice();
        cur[i] = 1;
        for (var j = i + 1; j < s.length; j++) {
            cur[j] = s[i] == s[j] ? 2 + pre[j - 1] : Math.max(pre[j], cur[j - 1]);
        }
    }
    return cur[cur.length - 1];
};


s = "abbc"
longestPalindromeSubseq(s)