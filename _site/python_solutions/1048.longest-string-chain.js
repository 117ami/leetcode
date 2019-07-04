/*
 * @lc app=leetcode id=1048 lang=javascript
 *
 * [1048] Longest String Chain
 *
 * https://leetcode.com/problems/longest-string-chain/description/
 *
 * algorithms
 * Medium (44.33%)
 * Total Accepted:    4.3K
 * Total Submissions: 9.5K
 * Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
 *
 * Given a list of words, each word consists of English lowercase letters.
 * 
 * Let's say word1 is a predecessor of word2 if and only if we can add exactly
 * one letter anywhere in word1 to make it equal to word2.  For example, "abc"
 * is a predecessor of "abac".
 * 
 * A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
 * 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
 * word_3, and so on.
 * 
 * Return the longest possible length of a word chain with words chosen from
 * the given list of words.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: ["a","b","ba","bca","bda","bdca"]
 * Output: 4
 * Explanation: one of the longest word chain is "a","ba","bda","bdca".
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= words.length <= 1000
 * 1 <= words[i].length <= 16
 * words[i] only consists of English lowercase letters.
 * 
 * 
 * 
 * 
 * 
 */
/**
 * @param {string[]} words
 * @return {number}
 */
var longestStrChain = function(words) {
    words.sort((a, b) => (a.length - b.length));
    var res = {},
        ans = 0;

    words.forEach(function(w) {
        var maxlen = 1;
        for (var i = 0; i < w.length; i++) {
            var nexts = w.substring(0, i) + w.substring(i + 1);
            if (res[nexts])
                maxlen = Math.max(maxlen, res[nexts] + 1);
        }
        res[w] = maxlen;
        ans = Math.max(ans, maxlen);
    });
    // print(res);
    return ans;
};

var print = function(a) {
    console.log(a);
}


var words = ["efghhh", "a", "b", "ba", "bca", "bda", "bdca"];
print(longestStrChain(words))