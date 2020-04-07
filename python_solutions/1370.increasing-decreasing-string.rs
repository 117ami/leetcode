/*
 * @lc app=leetcode id=1370 lang=rust
 *
 * [1370] Increasing Decreasing String
 *
 * https://leetcode.com/problems/increasing-decreasing-string/description/
 *
 * algorithms
 * Easy (78.64%)
 * Total Accepted:    4.6K
 * Total Submissions: 5.8K
 * Testcase Example:  '"aaaabbbbcccc"'
 *
 * Given a string s. You should re-order the string using the following
 * algorithm:
 * 
 * 
 * Pick the smallest character from s and append it to the result.
 * Pick the smallest character from s which is greater than the last appended
 * character to the result and append it.
 * Repeat step 2 until you cannot pick more characters.
 * Pick the largest character from s and append it to the result.
 * Pick the largest character from s which is smaller than the last appended
 * character to the result and append it.
 * Repeat step 5 until you cannot pick more characters.
 * Repeat the steps from 1 to 6 until you pick all characters from s.
 * 
 * 
 * In each step, If the smallest or the largest character appears more than
 * once you can choose any occurrence and append it to the result.
 * 
 * Return the result string after sorting s with this algorithm.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "aaaabbbbcccc"
 * Output: "abccbaabccba"
 * Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
 * After steps 4, 5 and 6 of the first iteration, result = "abccba"
 * First iteration is done. Now s = "aabbcc" and we go back to step 1
 * After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
 * After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "rat"
 * Output: "art"
 * Explanation: The word "rat" becomes "art" after re-ordering it with the
 * mentioned algorithm.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "leetcode"
 * Output: "cdelotee"
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: s = "ggggggg"
 * Output: "ggggggg"
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: s = "spo"
 * Output: "ops"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 500
 * s contains only lower-case English letters.
 * 
 * 
 */
impl Solution {
    pub fn sort_string(s: String) -> String {
        let mut arr = vec![0; 26];
        for c in s.chars() { arr[c as usize - 'a' as usize] += 1; }
        let mut res = String::from(""); 
        let mut cter = s.len();
        let mut pivot = 0; 

        while cter > 0 {
            for i in 0..26 {
                let j = if pivot == 0 { i as usize } else {(25 - i) as usize};
                if arr [j] > 0 {
                    arr [j] -= 1; 
                    res.push((j as u8+97) as char);
                    cter -= 1; 
                }
            }
            pivot = 1 - pivot;
        }
        res 
    }
}


// pub structSolution; 

use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;
// use std::collections::VecDeque; 
// use std::collections::BTreeMap; 

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

#[allow(dead_code)]
pub fn vec_counter(arr: Vec<i32>) -> HashMap<i32, i32> {
    let mut c = HashMap::new(); 
    for n in arr { *c.entry(n).or_insert(0) += 1; }
    c 
}

#[allow(dead_code)]
pub fn vec_to_hashset(arr: Vec<i32>) -> HashSet<i32> {
   HashSet::from_iter(arr.iter().cloned())
}

#[allow(dead_code)]
pub fn int_to_char(n: i32) -> char {
    // Convert number 0 to a, 1 to b, ...
    assert!(n >= 0 && n <= 25);
    (n as u8 + 'a' as u8) as char
}