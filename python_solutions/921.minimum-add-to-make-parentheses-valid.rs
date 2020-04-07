/*
 * @lc app=leetcode id=921 lang=rust
 *
 * [921] Minimum Add to Make Parentheses Valid
 *
 * https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
 *
 * algorithms
 * Medium (71.78%)
 * Total Accepted:    49K
 * Total Submissions: 68.3K
 * Testcase Example:  '"())"'
 *
 * Given a string S of '(' and ')' parentheses, we add the minimum number of
 * parentheses ( '(' or ')', and in any positions ) so that the resulting
 * parentheses string is valid.
 * 
 * Formally, a parentheses string is valid if and only if:
 * 
 * 
 * It is the empty string, or
 * It can be written as AB (A concatenated with B), where A and B are valid
 * strings, or
 * It can be written as (A), where A is a valid string.
 * 
 * 
 * Given a parentheses string, return the minimum number of parentheses we must
 * add to make the resulting string valid.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "())"
 * Output: 1
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "((("
 * Output: 3
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "()"
 * Output: 0
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "()))(("
 * Output: 4
 * 
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * S.length <= 1000
 * S only consists of '(' and ')' characters.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */
impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let (mut res, mut cter) = (0, 0);
        for c in s.chars(){
            if c == '(' { cter += 1; }
            else { cter -= 1; }
            if cter < 0 { 
                res -= cter; 
                cter = 0; 
            }
        }
        res += cter; 
        res 
    }
}
// pub structSolution; 
use std::collections::HashMap;
use std::fmt::Debug;
use std::hash::Hash;

#[allow(dead_code)]
pub fn print_map<K: Debug + Eq + Hash, V: Debug>(map: &HashMap<K, V>) {
    for (k, v) in map.iter() {
        println!("{:?}: {:?}", k, v);
    }
}

#[allow(dead_code)]
pub fn say_vec(nums: Vec<i32>){
	println!("{:?}", nums);
}

#[allow(dead_code)]
pub fn char_frequency(s: String) -> HashMap<char, i32> {
    let mut res:HashMap<char, i32> = HashMap::new(); 
    for c in s.chars(){
        *res.entry(c).or_insert(0) += 1;
    }
    res 
}

