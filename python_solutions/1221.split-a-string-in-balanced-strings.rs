/*
 * @lc app=leetcode id=1221 lang=rust
 *
 * [1221] Split a String in Balanced Strings
 *
 * https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
 *
 * algorithms
 * Easy (81.26%)
 * Total Accepted:    47.1K
 * Total Submissions: 57.9K
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
 * Example 4:
 * 
 * 
 * Input: s = "RLRRRLLRLL"
 * Output: 2
 * Explanation: s can be split into "RL", "RRRLLRLL", since each substring
 * contains an equal number of 'L' and 'R'
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
impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let (mut res, mut flag) = (0, 0); 
        for c in s.chars() {
            flag += if c == 'L' { 1 } else { -1 };
            if flag == 0 { res += 1;}
        }
        res 
    }
}
// pub structSolution; 
