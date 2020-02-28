/*
 * @lc app=leetcode id=771 lang=rust
 *
 * [771] Jewels and Stones
 *
 * https://leetcode.com/problems/jewels-and-stones/description/
 *
 * algorithms
 * Easy (84.53%)
 * Total Accepted:    387.3K
 * Total Submissions: 458.1K
 * Testcase Example:  '"aA"\n"aAAbbbb"'
 *
 * You're given strings J representing the types of stones that are jewels, and
 * S representing the stones you have.  Each character in S is a type of stone
 * you have.  You want to know how many of the stones you have are also
 * jewels.
 * 
 * The letters in J are guaranteed distinct, and all characters in J and S are
 * letters. Letters are case sensitive, so "a" is considered a different type
 * of stone from "A".
 * 
 * Example 1:
 * 
 * 
 * Input: J = "aA", S = "aAAbbbb"
 * Output: 3
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: J = "z", S = "ZZ"
 * Output: 0
 * 
 * 
 * Note:
 * 
 * 
 * S and J will consist of letters and have length at most 50.
 * The characters in J are distinct.
 * 
 * 
 */
use std::collections::HashSet; 
impl Solution {
    pub fn num_jewels_in_stones(j: String, s: String) -> i32 {
        let hs: HashSet<char> = j.chars().collect();
        if hs.is_empty() { return 0 ; }
        s.chars().filter(|c| hs.contains(c)).count() as i32 
    }
}
// pub structSolution; 
