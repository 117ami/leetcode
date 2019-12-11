// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
// Medium (Difficulty)

// Given an array of strings arr. String s is a concatenation of a sub-sequence
// of arr which have unique characters. Return the maximum possible length of s.
//  
// Example 1:
// Example 2:
// Example 3:
//  
// Constraints:
// Input: arr = ["un","iq","ue"]
// Output: 4
// Explanation: All possible concatenations are "","un","iq","ue","uniq" and
// "ique". Maximum length is 4.
//
// Input: arr = ["cha","r","act","ers"]
// Output: 6
// Explanation: Possible solutions are "chaers" and "acters".
//
// Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
// Output: 26
//
// xxxxxxxxxx
// class Solution {
// public:
//     int maxLength(vector<string>& arr) {
//         
//     }
// };
class Solution {
public:
  int maxLength(vector<string> &arr) {
      ios_base::sync_with_stdio(false);
    vector<bitset<26>> dp = {bitset<26>()};
    int res = 0;
    for (auto &s : arr) {
      bitset<26> tmp;
      for (char c : s)
        tmp.set(c - 'a');

      if (tmp.count() < s.size())
        continue;

      for (int i = dp.size() - 1; i >= 0; --i) {
        bitset c = dp[i];
        if ((c & tmp).any())
          continue;
        dp.push_back(c | tmp);
        res = max(res, (int)dp[dp.size() - 1].count());
      }
    }
    return res;
  }
};