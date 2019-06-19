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

var ispalindrome = function(s) {
    var i = 0,
        j = len(s) - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i += 1;
        j -= 1;
    }
    return true;
}

function permutations(inputArr) {
    var results = [];

    function permute(arr, memo) {
        var cur, memo = memo || [];

        for (var i = 0; i < arr.length; i++) {
            cur = arr.splice(i, 1);
            if (arr.length === 0) {
                results.push(memo.concat(cur));
            }
            permute(arr.slice(), memo.concat(cur));
            arr.splice(i, 0, cur[0]);
        }

        return results;
    }

    return permute(inputArr);
}


function last(arr) {
    return arr[len(arr) - 1];
}

function exist(key, hash) {
    return (key in hash);
}
/*
 * @lc app=leetcode id=1089 lang=javascript
 *
 * [1089] Duplicate Zeros
 *
 * https://leetcode.com/problems/duplicate-zeros/description/
 *
 * algorithms
 * Easy (58.86%)
 * Total Accepted:    3.8K
 * Total Submissions: 6.4K
 * Testcase Example:  '[1,0,2,3,0,4,5,0]'
 *
 * Given a fixed length array arr of integers, duplicate each occurrence of
 * zero, shifting the remaining elements to the right.
 * 
 * Note that elements beyond the length of the original array are not written.
 * 
 * Do the above modifications to the input array in place, do not return
 * anything from your function.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,0,2,3,0,4,5,0]
 * Output: null
 * Explanation: After calling your function, the input array is modified to:
 * [1,0,0,2,3,0,0,4]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [1,2,3]
 * Output: null
 * Explanation: After calling your function, the input array is modified to:
 * [1,2,3]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= arr.length <= 10000
 * 0 <= arr[i] <= 9
 * 
 */
/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */

var duplicateZeros = function(arr) {
    for (let i = 0; i < len(arr); i++) {
        if (arr[i] == 0) {
            arr.splice(i, 0, 0);
            arr.pop();
            i += 1;
        }
    }
}

var duplicateZeros2 = function(arr) {
    var i = -1,
        j = -1;
    while (true) {
        j += 1;
        i += arr[j] == 0 ? 2 : 1;
        if (i >= len(arr) - 1) break;
    }
    if (i >= len(arr)) {
        arr[i - 1] = 0;
        i -= 2;
        j -= 1;
    }
    while (i >= 0) {
        if (arr[j] == 0) {
            arr[i] = arr[i - 1] = 0;
            i -= 2;
        } else {
            arr[i] = arr[j];
            i -= 1;
        }
        j -= 1;
    }
    // print(arr)
};

arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr)