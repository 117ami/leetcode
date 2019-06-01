/*
 * @lc app=leetcode id=330 lang=javascript
 *
 * [330] Patching Array
 *
 * https://leetcode.com/problems/patching-array/description/
 *
 * algorithms
 * Hard (33.31%)
 * Total Accepted:    31.2K
 * Total Submissions: 93.6K
 * Testcase Example:  '[1,3]\n6'
 *
 * Given a sorted positive integer array nums and an integer n, add/patch
 * elements to the array such that any number in range [1, n] inclusive can be
 * formed by the sum of some elements in the array. Return the minimum number
 * of patches required.
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,3], n = 6
 * Output: 1 
 * Explanation:
 * Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3,
 * 4.
 * Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
 * [2,3], [1,2,3].
 * Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
 * So we only need 1 patch.
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,5,10], n = 20
 * Output: 2
 * Explanation: The two patches can be [2, 4].
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,2,2], n = 5
 * Output: 0
 * 
 */
/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number}
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
    array.forEach(function(e) {
        dict[e] = dict[e] ? dict[e] += 1 : 1;
    });
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

var minPatches = function(nums, n) {
    var res = 0,
        i = 0,
        missed = 1;
    while (missed <= n) {
        if (i < nums.length && nums[i] <= missed) {
            missed += nums[i];
            i += 1;
        } else {
            missed *= 2;
            res += 1;
        }
    }
    return res;
};