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
var counter = function(array_or_string) {
    var dict = {};
    for (let i = 0; i < array_or_string.length; i++) {
        let e = array_or_string[i];
        dict[e] = dict[e] ? dict[e] += 1 : 1;
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


var len = function(str_or_array) {
    return str_or_array.length;
}

var sorted = function(arr) {
    return arr.sort((a, b) => (a - b));
}

// print out a Map 
function printMap(m) {
    m.forEach(function(v, k) {
        console.log(k + " " + v);
    })
}

var gcd = function(a, b) {
    return b == 0 ? a : gcd(b, a % b);
}

var say = function(a) {
    console.log(a)
};


var two_d_array = function(m, n, v) {
    return [...Array(m)].map(x => Array(n).fill(v));
}

function floor(float_number) {
    return Math.floor(float_number)
}

function ceil(float_number) {
    return Math.ceil(float_number)
}


var max = function(arr) {
    return Math.max(...arr);
}

var min = function(arr) {
    return Math.min(...arr)
};

var pairmax = function(a, b) {
    return Math.max(a, b)
}

var pairmin = function(a, b) {
    return Math.min(a, b)
}

// create an array with elements from 0 to n
var nlist = function(n) {
    return [...Array(n + 1).keys()];
}

function last(arr) {
    return arr[len(arr) - 1];
}


/*
 * @lc app=leetcode id=5086 lang=javascript
 *
 * [5086] Smallest Subsequence of Distinct Characters
 *
 * https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
 *
 * algorithms
 * Medium (33.27%)
 * Total Accepted:    1.4K
 * Total Submissions: 3.8K
 * Testcase Example:  '"cdadabcc"'
 *
 * Return the lexicographically smallest subsequence of text that contains all
 * the distinct characters of text exactly once.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "cdadabcc"
 * Output: "adbc"
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "abcd"
 * Output: "abcd"
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "ecbacba"
 * Output: "eacb"
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "leetcode"
 * Output: "letcod"
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= text.length <= 1000
 * text consists of lowercase English letters.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */
/**
 * @param {string} text
 * @return {string}
 */
var smallestSubsequence = function(text) {
    var cnt = counter(text),
        seen = {},
        i = 0,
        res = [];
    for (var c of text) {
        cnt[c] -= 1;
        if ((c in seen) && (seen[c]) > 0) continue;
        while (len(res) > 0 && last(res) > c && cnt[last(res)] > 0) {
            seen[res.pop()] = 0;
        }
        res.push(c);
        seen[c] = 1;
    }
    return res.join('');
};

var text = "leetcode";
print(smallestSubsequence(text));