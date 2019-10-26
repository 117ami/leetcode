/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms
 * Medium (24.88%)
 * Total Accepted:    678.3K
 * Total Submissions: 2.7M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the
 * sum of zero.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate triplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [-1, 0, 1, 2, -1, -4],
 * 
 * A solution set is:
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 */
class Solution {
public:
    vector<vector<int>> res; 
    void nsum(int l, int r, int target, int c, vector<int>& nums, vector<int> & cur) {
        if (r - l + 1 < c || c < 2 || nums[l] * c > target || nums[r] * c < target) return; 
        if (c == 2) {
            while (l < r) {
                int s = nums[l] + nums[r]; 
                if (s == target) {
                    vector<int>tmp(cur); 
                    tmp.emplace_back(nums[l]); 
                    tmp.emplace_back(nums[r]); 
                    res.emplace_back(tmp);
                    l ++; 
                    while (l < r && nums[l] == nums[l-1]) l ++; 
                } else if (s < target) l ++; 
                else r --; 
            }
        } else {
            for (int i = l; i <= r; i ++)
                if (i == l || nums[i] != nums[i-1]) {
                    vector<int> tmp(cur); 
                    tmp.emplace_back(nums[i]); 
                    nsum(i + 1, r, target - nums[i], c - 1, nums, tmp); 
                }
        }
    }
    
    // Method 1: nsum for any n >= 2
    vector<vector<int>> threeSum2(vector<int>& nums) {
        sort(nums.begin(), nums.end())    ;
        vector<int> cur; 
        nsum(0, nums.size() - 1, 0, 3, nums, cur);
        return res; 
    }

    // Method 2: fix one and calculate 
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        size_t n = nums.size(); 
        
        for (size_t i = 0; i < n; i ++) {
            int v = -nums[i], lo = i + 1, hi = n - 1; 
            while (lo < hi) {
                int sum = nums[lo] + nums[hi]; 
                if (v < sum) hi --; 
                else if (v > sum) lo ++; 
                else {
                    int vlo = nums[lo], vhi = nums[hi]; 
                    res.emplace_back(vector<int>{-v, vlo, vhi});
                    while (lo < hi && nums[++lo] == vlo) ; 
                    while (lo < hi && nums[--hi] == vhi) ;
                }
            }
            while (i < n - 1 && nums[i] == nums[i+1]) i ++; 
        }
        return res; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
