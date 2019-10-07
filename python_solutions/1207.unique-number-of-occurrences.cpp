/*
 * @lc app=leetcode id=1207 lang=cpp
 *
 * [1207] Unique Number of Occurrences
 *
 * https://leetcode.com/problems/unique-number-of-occurrences/description/
 *
 * algorithms
 * Easy (74.36%)
 * Total Accepted:    12.1K
 * Total Submissions: 16.3K
 * Testcase Example:  '[1,2,2,1,1,3]'
 *
 * Given an array of integers arr, write a function that returns true if and
 * only if the number of occurrences of each value in the array is unique.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [1,2,2,1,1,3]
 * Output: true
 * Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
 * values have the same number of occurrences.
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [1,2]
 * Output: false
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
 * Output: true
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 1000
 * -1000 <= arr[i] <= 1000
 * 
 * 
 */
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        int ox[2001] = {0}; 
        for (auto &i : arr) ox[i + 1000] ++; 
        
        unordered_set<int> us; 
        for (int i = 0; i < 2001; i ++) {
            if (ox[i] > 0 && us.count(ox[i])) return false; 
            us.insert(ox[i]);
        }
        return true; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
