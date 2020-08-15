/*
 * @lc app=leetcode id=409 lang=cpp
 *
 * [409] Longest Palindrome
 *
 * https://leetcode.com/problems/longest-palindrome/description/
 *
 * algorithms
 * Easy (50.32%)
 * Total Accepted:    165.3K
 * Total Submissions: 321.4K
 * Testcase Example:  '"abccccdd"'
 *
 * Given a string which consists of lowercase or uppercase letters, find the
 * length of the longest palindromes that can be built with those letters.
 * 
 * This is case sensitive, for example "Aa" is not considered a palindrome
 * here.
 * 
 * Note:
 * Assume the length of given string will not exceed 1,010.
 * 
 * 
 * Example: 
 * 
 * Input:
 * "abccccdd"
 * 
 * Output:
 * 7
 * 
 * Explanation:
 * One longest palindrome that can be built is "dccaccd", whose length is 7.
 * 
 * 
 */
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> cc; 
        for(auto &c: s) cc[c]++; 
        int res = s.size(); 
        int has_odd=0; 
        for(auto &[k, v]: cc) {
            if(v &1 ) has_odd=1, res --; 
        }
        return res + has_odd; 
    }
};



auto speed_up = [] () {
    ios_base::sync_with_stdio(false);
    return 0;
}(); 
