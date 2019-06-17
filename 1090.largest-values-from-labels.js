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


function last(arr){
    return arr[len(arr)-1];
}

function exist(key, hash) {
    return (key in hash);
}/*
 * @lc app=leetcode id=1090 lang=javascript
 *
 * [1090] Largest Values From Labels
 *
 * https://leetcode.com/problems/largest-values-from-labels/description/
 *
 * algorithms
 * Medium (53.75%)
 * Total Accepted:    2.6K
 * Total Submissions: 4.8K
 * Testcase Example:  '[5,4,3,2,1]\n[1,1,2,2,3]\n3\n1'
 *
 * We have a set of items: the i-th item has value values[i] and label
 * labels[i].
 * 
 * Then, we choose a subset S of these items, such that:
 * 
 * 
 * |S| <= num_wanted
 * For every label L, the number of items in S with label L is <= use_limit.
 * 
 * 
 * Return the largest possible sum of the subset S.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit
 * = 1
 * Output: 9
 * Explanation: The subset chosen is the first, third, and fifth item.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit
 * = 2
 * Output: 12
 * Explanation: The subset chosen is the first, second, and third item.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit
 * = 1
 * Output: 16
 * Explanation: The subset chosen is the first and fourth item.
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit
 * = 2
 * Output: 24
 * Explanation: The subset chosen is the first, second, and fourth item.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= values.length == labels.length <= 20000
 * 0 <= values[i], labels[i] <= 20000
 * 1 <= num_wanted, use_limit <= values.length
 * 
 * 
 * 
 * 
 * 
 */
/**
 * @param {number[]} values
 * @param {number[]} labels
 * @param {number} num_wanted
 * @param {number} use_limit
 * @return {number}
 */
var largestValsFromLabels = function(values, labels, num_wanted, use_limit) {
    
};
