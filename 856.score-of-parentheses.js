/*
 * @lc app=leetcode id=856 lang=javascript
 *
 * [856] Score of Parentheses
 *
 * https://leetcode.com/problems/score-of-parentheses/description/
 *
 * algorithms
 * Medium (55.72%)
 * Total Accepted:    17.1K
 * Total Submissions: 30.6K
 * Testcase Example:  '"()"'
 *
 * Given a balanced parentheses string S, compute the score of the string based
 * on the following rule:
 * 
 * 
 * () has score 1
 * AB has score A + B, where A and B are balanced parentheses strings.
 * (A) has score 2 * A, where A is a balanced parentheses string.
 * 
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "()"
 * Output: 1
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "(())"
 * Output: 2
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "()()"
 * Output: 2
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "(()(()))"
 * Output: 6
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * S is a balanced parentheses string, containing only ( and ).
 * 2 <= S.length <= 50
 * 
 * 
 * 
 * 
 * 
 * 
 */
/**
 * @param {string} S
 * @return {number}
 */
var scoreOfParentheses = function(S) {
    var stack = [];
    for (var c of S) {
        if (c == '(')
            stack.push(c);
        else {
            var n = 0;
            while (stack.length > 0 && stack[stack.length - 1] != '(')
                n += stack.pop();
            n = Math.max(1, n * 2);
            stack[stack.length - 1] = n;
        }
    }
    const add = (a, b) => a + b;
    return stack.reduce(add);
};


console.log(scoreOfParentheses('(()(()))'));