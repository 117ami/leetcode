/*
 * @lc app=leetcode id=917 lang=javascript
 *
 * [917] Reverse Only Letters
 *
 * https://leetcode.com/problems/reverse-only-letters/description/
 *
 * algorithms
 * Easy (55.98%)
 * Total Accepted:    22.7K
 * Total Submissions: 40.7K
 * Testcase Example:  '"ab-cd"'
 *
 * Given a string S, return the "reversed" string where all characters that are
 * not a letter stay in the same place, and all letters reverse their
 * positions.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "ab-cd"
 * Output: "dc-ba"
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "a-bC-dEf-ghIj"
 * Output: "j-Ih-gfE-dCba"
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "Test1ng-Leet=code-Q!"
 * Output: "Qedo1ct-eeLg=ntse-T!"
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * S.length <= 100
 * 33 <= S[i].ASCIIcode <= 122 
 * S doesn't contain \ or "
 * 
 * 
 * 
 * 
 * 
 */
/**
 * @param {string} S
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    let i = 0, j = s.length - 1; 
    var s = s.split('')
    var isletter = function(c) {return c.match(/[a-z]/i) != null }; 
    while (i < j ) {
    	while (i < j && ! isletter(s[i])) i += 1;
    	while (i < j && ! isletter(s[j])) j -= 1;    	
    	t = s[j]; 
    	s[j] = s[i]; 
    	s[i] = t; 
    	i += 1; 
    	j -= 1; 
    }
    // console.log(s)
    return s.join(''); 
};

console.log(reverseOnlyLetters("Test1ng-Leet=code-Q!"))

str = "abc"
console.log(str.split(''))

