/*
 * @lc app=leetcode id=154 lang=javascript
 *
 * [154] Find Minimum in Rotated Sorted Array II
 *
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
 *
 * algorithms
 * Hard (39.25%)
 * Total Accepted:    128.4K
 * Total Submissions: 327K
 * Testcase Example:  '[1,3,5]'
 *
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 * 
 * (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
 * 
 * Find the minimum element.
 * 
 * The array may contain duplicates.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,3,5]
 * Output: 1
 * 
 * Example 2:
 * 
 * 
 * Input: [2,2,2,0,1]
 * Output: 0
 * 
 * Note:
 * 
 * 
 * This is a follow up problem to Find Minimum in Rotated Sorted Array.
 * Would allow duplicates affect the run-time complexity? How and why?
 * 
 * 
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    var rec = function(start, end) {
        // console.log(start, end);		
        if (end - start <= 1) return Math.min(...nums.slice(start, end + 1));
        var mid = Math.floor((start + end) / 2),
            pivot = nums[end];
        if (nums[mid] < pivot)
            return rec(start, mid);
        else if (nums[mid] > pivot)
            return rec(mid + 1, end);
        else
            return Math.min(rec(start, mid), rec(mid + 1, end));
    };
    return rec(0, nums.length - 1);
};

var nums = [3, 3, 3, 1, 3];
// nums = [1, 3]
console.log(findMin(nums));