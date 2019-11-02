/*
 * @lc app=leetcode id=1221 lang=cpp
 *
 * [1221] Split a String in Balanced Strings
 *
 * https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
 *
 * algorithms
 * Easy (78.31%)
 * Total Accepted:    16.7K
 * Total Submissions: 21.3K
 * Testcase Example:  '"RLRRLLRLRL"'
 *
 * Balanced strings are those who have equal quantity of 'L' and 'R'
 * characters.
 * 
 * Given a balanced string s split it in the maximum amount of balanced
 * strings.
 * 
 * Return the maximum amount of splitted balanced strings.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "RLRRLLRLRL"
 * Output: 4
 * Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring
 * contains same number of 'L' and 'R'.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "RLLLLRRRLR"
 * Output: 3
 * Explanation: s can be split into "RL", "LLLRRR", "LR", each substring
 * contains same number of 'L' and 'R'.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "LLLLRRRR"
 * Output: 1
 * Explanation: s can be split into "LLLLRRRR".
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 1000
 * s[i] = 'L' or 'R'
 * 
 * 
 */
class Solution {
public:
    int balancedStringSplit(string s) {
        int balance = 0, res = 0; 
        for(auto &c: s) {
            balance += c == 'L' ? 1 : -1; 
            if (balance == 0) res ++; 
        }
        return res; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
