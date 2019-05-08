/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (43.82%)
 * Total Accepted:    1.7M
 * Total Submissions: 4M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * Example:
 * 
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * 
 * 
 * 
 */
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	unordered_map<int, int> idx; 
		for (int i = 0; i < nums.size(); ++i) {
			if (idx.find(target - nums[i]) != idx.end()) 
				return {idx[target - nums[i]], i}; 
			idx[nums[i]] = i;
		}
		return {};
	}
};


static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
