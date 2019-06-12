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
var nlist=function(n) { return [...Array(n+1).keys()] ; }

var ispalindrome = function(s) {
    var i = 0, j = len(s) - 1; 
    while (i < j) {
        if (s[i] != s[j]) return false; 
        i += 1; 
        j -= 1;
    }
    return true; 
}
/*
 * @lc app=leetcode id=264 lang=javascript
 *
 * [264] Ugly Number II
 *
 * https://leetcode.com/problems/ugly-number-ii/description/
 *
 * algorithms
 * Medium (36.45%)
 * Total Accepted:    105.3K
 * Total Submissions: 288.7K
 * Testcase Example:  '10'
 *
 * Write a program to find the n-th ugly number.
 * 
 * Ugly numbers are positive numbers whose prime factors only include 2, 3,
 * 5. 
 * 
 * Example:
 * 
 * 
 * Input: n = 10
 * Output: 12
 * Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
 * ugly numbers.
 * 
 * Note:  
 * 
 * 
 * 1 is typically treated as an ugly number.
 * n does not exceed 1690.
 * 
 */
/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    
};
