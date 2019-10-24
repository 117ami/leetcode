/*
 * @lc app=leetcode id=18 lang=cpp
 *
 * [18] 4Sum
 *
 * https://leetcode.com/problems/4sum/description/
 *
 * algorithms
 * Medium (31.60%)
 * Total Accepted:    266.5K
 * Total Submissions: 843.2K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * Given an array nums of n integers and an integer target, are there elements
 * a, b, c, and d in nums such that a + b + c + d = target? Find all unique
 * quadruplets in the array which gives the sum of target.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate quadruplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
 * 
 * A solution set is:
 * [
 * ⁠ [-1,  0, 0, 1],
 * ⁠ [-2, -1, 1, 2],
 * ⁠ [-2,  0, 0, 2]
 * ]
 * 
 * 
 */
class Solution {
public:
    vector<vector<int>> res; 
    void nsum(int l, int r, int target, int cter, vector<int> nums, vector<int> curres) {
        if (r - l + 1 < cter || cter < 2 || nums[r] * cter < target || nums[l] * cter > target) return; 
        if (cter == 2) {
            while (l < r) {
                int s = nums[l] + nums[r]; 
                if (s == target) {
                    vector<int> tmp(curres); 
                    tmp.push_back(nums[l]); 
                    tmp.push_back(nums[r]); 
                    res.push_back(tmp);
                    l ++; 
                    while (l < r && nums[l] == nums[l-1]) l ++; 
                } else if (s < target) l ++; 
                else r --; 
            }
        } else {
            for (int i = l; i <= r; i ++){
                if (i == l || nums[i] != nums[i-1]) {
                    vector<int> tmp(curres); 
                    tmp.push_back(nums[i]);
                    nsum(i + 1, r, target - nums[i], cter - 1, nums, tmp);
                }
            }
        }
    }

    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end()); 
        vector<int> tmp; 
        nsum(0, nums.size() - 1, target, 4, nums, tmp);
        return res; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
