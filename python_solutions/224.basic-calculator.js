/*
 * @lc app=leetcode id=224 lang=javascript
 *
 * [224] Basic Calculator
 *
 * https://leetcode.com/problems/basic-calculator/description/
 *
 * algorithms
 * Hard (32.49%)
 * Total Accepted:    105.1K
 * Total Submissions: 323K
 * Testcase Example:  '"1 + 1"'
 *
 * Implement a basic calculator to evaluate a simple expression string.
 * 
 * The expression string may contain open ( and closing parentheses ), the plus
 * + or minus sign -, non-negative integers and empty spaces  .
 * 
 * Example 1:
 * 
 * 
 * Input: "1 + 1"
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: " 2-1 + 2 "
 * Output: 3
 * 
 * Example 3:
 * 
 * 
 * Input: "(1+(4+5+2)-3)+(6+8)"
 * Output: 23
 * Note:
 * 
 * 
 * You may assume that the given expression is always valid.
 * Do not use the eval built-in library function.
 * 
 * 
 */
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
	var res = 0, sign = 1, stack = [], number = 0; 
	for (var c of s)    {
		if (!isNaN(parseInt(c, 10))){
			number = number * 10 + parseInt(c);
		} else if (c == '+') {
			res += number * sign; 
			number = 0; 
			sign = 1; 
		} else if (c == '-') {
			res += number * sign; 
			number = 0; 
			sign = -1;
		} else if (c == '(') {
			stack.push(res); 
			stack.push(sign);
			res = 0; 
			sign = 1; 
		} else if (c == ')') {
			res += number * sign; 
			res *= stack.pop(); 
			res += stack.pop(); 
			number = 0; 
		}
	}
	return res + number * sign;
};


var s = "(1-(2-3))"
console.log(calculate(s))