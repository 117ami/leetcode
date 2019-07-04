/*
 * @lc app=leetcode id=5 lang=javascript
 *
 * [5] Longest Palindromic Substring
 *
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (27.16%)
 * Total Accepted:    542.5K
 * Total Submissions: 2M
 * Testcase Example:  '"babad"'
 *
 * Given a string s, find the longest palindromic substring in s. You may
 * assume that the maximum length of s is 1000.
 * 
 * Example 1:
 * 
 * 
 * Input: "babad"
 * Output: "bab"
 * Note: "aba" is also a valid answer.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "cbbd"
 * Output: "bb"
 * 
 * 
 */
/**
 * @param {string} s
 * @return {string}
 */
var reverse = function(str) {
    return [...str].reverse().join('');
}


var longestPalindrome = function(s) {
    if (s == reverse(s)) return s;
    var start = 0,
        maxlen = 1;
    for (var i = 0; i < s.length;) {
        var j = i - 1;
        while (i < s.length && s[i] == s[j + 1]) i += 1;
        var k = i;
        while (j >= 0 && k < s.length && s[j] == s[k]) {
            j -= 1;
            k += 1;
        }

        if (k - j - 1 > maxlen) {
            maxlen = k - j - 1;
            start = j + 1;
        }
    }
    return s.substring(start, start + maxlen);
};


var s = "babad";
console.log(reverse(s))
console.log(longestPalindrome(s));