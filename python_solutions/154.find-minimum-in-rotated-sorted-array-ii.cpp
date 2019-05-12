/*
 * @lc app=leetcode id=154 lang=cpp
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
class Solution {
public:
    int findMin(vector<int>& nums) {
    	return recursive(nums, 0, nums.size() - 1);
    }

    int recursive(vector<int>& nums, int start, int end) {
		int pivot = nums[end];
        int mid = (start + end) / 2; 
        if (end - start <= 1) return min(nums[start], nums[end]); 
        if (nums[mid] < pivot) 
        	return recursive(nums, start, mid); 
        else if (nums[mid] > pivot) 
        	return recursive(nums, mid, end); 
        else
        	return min(recursive(nums, start, mid), recursive(nums, mid, end));
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
