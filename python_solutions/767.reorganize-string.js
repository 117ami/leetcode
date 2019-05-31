/*
 * @lc app=leetcode id=767 lang=javascript
 *
 * [767] Reorganize String
 *
 * https://leetcode.com/problems/reorganize-string/description/
 *
 * algorithms
 * Medium (42.02%)
 * Total Accepted:    26.5K
 * Total Submissions: 62.8K
 * Testcase Example:  '"aab"'
 *
 * Given a string S, check if the letters can be rearranged so that two
 * characters that are adjacent to each other are not the same.
 * 
 * If possible, output any possible result.  If not possible, return the empty
 * string.
 * 
 * Example 1:
 * 
 * 
 * Input: S = "aab"
 * Output: "aba"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: S = "aaab"
 * Output: ""
 * 
 * 
 * Note:
 * 
 * 
 * S will consist of lowercase letters and have length in range [1, 500].
 * 
 * 
 * 
 * 
 */
/**
 * @param {string} S
 * @return {string}
 */

var bisect_left = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    while (i < j) {
        mid = ~~((i + j) / 2);
        if (nums[mid] < target)
            i = mid + 1;
        else
            j = mid;
    }
    return i;
}

var bisect_right = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    while (i < j) {
        mid = Math.ceil((i + j) / 2);
        if (nums[mid] > target)
            j = mid - 1;
        else
            i = mid;
    }
    return j;
}

var two_d_array = function(m, n) {
    return new Array(m).fill(0).map(() => new Array(n).fill(0));
}

var reverse = function(s) {
    return [...str].reverse().join('');
}


// simple print
var print = function(a) {
    console.log(a);
}

// For counting elements in a list 
var counter = function(array) {
    var dict = {};
    for (var i = 0; i < array.length; i++) {
        dict[array[i]] = dict[array[i]] ? dict[array[i]] += 1 : 1;
    }
    return dict;
}

var sum = function(array) {
    return array.reduce(function(a, b) {
        return a + b;
    }, 0);
}

var isodd = function(n) {
    return n % 2 == 1;
}

var iseven = function(n) {
    return n % 2 == 0;
}

var list = function(size, value) {
    return Array(size).fill(value);
}

var reorganizeString = function(S) {
    c = counter(S);
    chars = Object.keys(c);
    chars.sort(function(a, b) {
        return c[b] - c[a]
    });
    var res = list(S.length, '*'),
        i = 0, 
        b = true;
    chars.forEach(function(k) {
        for (var j = 0; j < c[k]; j ++) {
            res[i] = k;
            if (i > 0 && i < S.length - 1 && (res[i] == res[i - 1] || res[i] == res[i + 1])){
                b = false;
                return "";
            }
            i += 2;
            if (i >= S.length) i = 1;
        }
    });
    if (!b) return "";
    return res.join('');
};

print(reorganizeString("aaab"));