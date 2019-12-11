// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference
// Medium (Difficulty)

// Given an integer array arr and an integer difference, return the length of
// the longest subsequence in arr which is an arithmetic sequence such that the
// difference between adjacent elements in the subsequence equals difference.  
// Example 1:
// Example 2:
// Example 3:
//  
// Constraints:
// Input: arr = [1,2,3,4], difference = 1
// Output: 4
// Explanation: The longest arithmetic subsequence is [1,2,3,4].
// Input: arr = [1,3,5,7], difference = 1
// Output: 1
// Explanation: The longest arithmetic subsequence is any single element.
//
// Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
// Output: 4
// Explanation: The longest arithmetic subsequence is [7,5,3,1].
//
// xxxxxxxxxx
// class Solution {
// public:
//     int longestSubsequence(vector<int>& arr, int difference) {
//         
//     }
// };

class Solution {
public:
  int longestSubsequence(vector<int> &arr, int difference) {
    ios_base::sync_with_stdio(false);
    unordered_map<int, int> memo;

    int ans = 0; 
    for (auto n : arr){
      memo[n] = memo[n - difference] + 1;
      ans = max(ans, memo[n]);
    }
    // auto x = max_element(memo.begin(), memo.end(),
    //                      [](const pair<int, int> &a, const pair<int, int> &b) {
    //                        return a.second < b.second;
    //                      });
    // return x->second;
    return ans; 
  }
};