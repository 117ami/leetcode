/*
 * @lc app=leetcode id=287 lang=javascript
 *
 * [287] Find the Duplicate Number
 *
 * https://leetcode.com/problems/find-the-duplicate-number/description/
 *
 * algorithms
 * Medium (49.21%)
 * Total Accepted:    182.2K
 * Total Submissions: 370.2K
 * Testcase Example:  '[1,3,4,2,2]'
 *
 * Given an array nums containing n + 1 integers where each integer is between
 * 1 and n (inclusive), prove that at least one duplicate number must exist.
 * Assume that there is only one duplicate number, find the duplicate one.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,3,4,2,2]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,1,3,4,2]
 * Output: 3
 * 
 * Note:
 * 
 * 
 * You must not modify the array (assume the array is read only).
 * You must use only constant, O(1) extra space.
 * Your runtime complexity should be less than O(n2).
 * There is only one duplicate number in the array, but it could be repeated
 * more than once.
 * 
 * 
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    var slow = nums[0],
        fast = nums[slow];
    cond = 0;
    while (true) {
        if (slow == fast) {
            cond += 1;
            slow = 0;
        }
        if (cond == 2) return fast;
        slow = nums[slow];
        fast = cond == 0 ? nums[nums[fast]] : nums[fast];
    }
    return fast;
};

nums = [1, 3, 2, 1, 4];
nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1];
console.log(findDuplicate(nums));