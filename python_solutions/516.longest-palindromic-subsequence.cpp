/*
 * @lc app=leetcode id=516 lang=cpp
 *
 * [516] Longest Palindromic Subsequence
 *
 * https://leetcode.com/problems/longest-palindromic-subsequence/description/
 *
 * algorithms
 * Medium (46.30%)
 * Total Accepted:    58.1K
 * Total Submissions: 125.5K
 * Testcase Example:  '"bbbab"'
 *
 * 
 * Given a string s, find the longest palindromic subsequence's length in s.
 * You may assume that the maximum length of s is 1000.
 * 
 * 
 * Example 1:
 * Input: 
 * 
 * "bbbab"
 * 
 * Output: 
 * 
 * 4
 * 
 * One possible longest palindromic subsequence is "bbbb".
 * 
 * 
 * Example 2:
 * Input:
 * 
 * "cbbd"
 * 
 * Output:
 * 
 * 2
 * 
 * One possible longest palindromic subsequence is "bb".
 * 
 */
class Solution {
public:
    int longestPalindromeSubseq(string s) {
		vector<int> cur (s.size(), 0); 
		for (int i = s.size() - 1; i >= 0; i--)  {
			vector<int> pre(cur); 
			cur[i] = 1;
			for (int j = i+1; j < s.size(); j ++) {
				cur[j] = s[i] == s[j] ? 2 + pre[j-1] : max(cur[j-1], pre[j]);
			}
		}
		// say(cur);
		return cur.back();
    }
};


static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
