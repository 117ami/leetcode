/*
 * @lc app=leetcode id=1347 lang=rust
 *
 * [1347] Minimum Number of Steps to Make Two Strings Anagram
 *
 * https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
 *
 * algorithms
 * Medium (76.24%)
 * Total Accepted:    11.3K
 * Total Submissions: 14.8K
 * Testcase Example:  '"bab"\n"aba"'
 *
 * Given two equal-size strings s and t. In one step you can choose any
 * character of t and replace it with another character.
 * 
 * Return the minimum number of steps to make t an anagram of s.
 * 
 * An Anagram of a string is a string that contains the same characters with a
 * different (or the same) ordering.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "bab", t = "aba"
 * Output: 1
 * Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram
 * of s.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "leetcode", t = "practice"
 * Output: 5
 * Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper
 * characters to make t anagram of s.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "anagram", t = "mangaar"
 * Output: 0
 * Explanation: "anagram" and "mangaar" are anagrams. 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: s = "xxyyzz", t = "xxyyzz"
 * Output: 0
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: s = "friend", t = "family"
 * Output: 4
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 50000
 * s.length == t.length
 * s and t contain lower-case English letters only.
 * 
 * 
 */

impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut v = vec![0; 26];
        for c in s.chars() {
            v[(c as usize) - ('a' as usize)] += 1;
        }
        for c in t.chars() {
            v[(c as usize) - ('a' as usize)] -= 1;
        }
        let mut res = 0 ; 
        for i in v {
            if i > 0 { res += i;}
        }
        res 
    }
}
// pub structSolution; 
