/*
 * @lc app=leetcode id=1054 lang=javascript
 *
 * [1054] Distant Barcodes
 *
 * https://leetcode.com/problems/distant-barcodes/description/
 *
 * algorithms
 * Medium (32.68%)
 * Total Accepted:    2.8K
 * Total Submissions: 7.8K
 * Testcase Example:  '[1,1,1,2,2,2]'
 *
 * In a warehouse, there is a row of barcodes, where the i-th barcode is
 * barcodes[i].
 * 
 * Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
 * return any answer, and it is guaranteed an answer exists.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,1,1,2,2,2]
 * Output: [2,1,2,1,2,1]
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [1,1,1,1,2,2,3,3]
 * Output: [1,3,1,3,2,1,2,1]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= barcodes.length <= 10000
 * 1 <= barcodes[i] <= 10000
 * 
 * 
 * 
 * 
 * 
 */
/**
 * @param {number[]} barcodes
 * @return {number[]}
 */

var counter = function(array) {
    var dict = {};
    array.forEach(function(e) {
        dict[e] = dict[e] ? dict[e] += 1 : 1;
    });
    return dict;
}


var rearrangeBarcodes = function(barcodes) {
    c = counter(barcodes);
    var pos = 0,
        res = [];
    var keys = Object.keys(c);
    keys.sort((a, b) => (c[b] - c[a])).forEach(function(e) {
        Array(c[e]).fill().forEach(function(v) {
            res[pos] = e;
            pos += 2;
            if (pos >= barcodes.length) pos = 1;
        });
    });
    return res;
};



var barcodes = [1, 1, 1, 1, 2, 2, 3, 3, 2];
barcodes = [2, 1, 1]
print(rearrangeBarcodes(barcodes))