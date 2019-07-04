/*
 * @lc app=leetcode id=273 lang=javascript
 *
 * [273] Integer to English Words
 *
 * https://leetcode.com/problems/integer-to-english-words/description/
 *
 * algorithms
 * Hard (24.20%)
 * Total Accepted:    100K
 * Total Submissions: 413K
 * Testcase Example:  '123'
 *
 * Convert a non-negative integer to its english words representation. Given
 * input is guaranteed to be less than 231 - 1.
 * 
 * Example 1:
 * 
 * 
 * Input: 123
 * Output: "One Hundred Twenty Three"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 12345
 * Output: "Twelve Thousand Three Hundred Forty Five"
 * 
 * Example 3:
 * 
 * 
 * Input: 1234567
 * Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
 * Seven"
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: 1234567891
 * Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty
 * Seven Thousand Eight Hundred Ninety One"
 * 
 * 
 */
/**
 * @param {number} num
 * @return {string}
 */
var numberToWords = function(num) {
    if (num == 0) return 'Zero';

    var below19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(' '),
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(' '),
        ks = 'Thousand Million Billion'.split(' ');
    var words = function(n, idx) {
        if (n == 0) return [];
        if (n < 20) return [below19[n - 1]];
        if (n < 100) return [tens[Math.floor(n / 10) - 2]].concat(words(n % 10, idx));
        if (n < 1000) return [below19[Math.floor(n / 100) - 1]].concat(['Hundred'], words(n % 100, idx));
        var m = Math.floor(n / 1000),
            r = n % 1000;
        var space = m % 1000 == 0 ? [] : [ks[idx]];
        return words(m, idx + 1).concat(space, words(r, idx));
    }

    return words(num, 0).join(' ');
};


console.log(numberToWords(123));