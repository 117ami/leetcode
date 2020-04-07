/*
 * @lc app=leetcode id=942 lang=rust
 *
 * [942] DI String Match
 *
 * https://leetcode.com/problems/di-string-match/description/
 *
 * algorithms
 * Easy (71.05%)
 * Total Accepted:    53.6K
 * Total Submissions: 75.4K
 * Testcase Example:  '"IDID"'
 *
 * Given a string S that only contains "I" (increase) or "D" (decrease), let N
 * = S.length.
 * 
 * Return any permutation A of [0, 1, ..., N] such that for all i = 0, ...,
 * N-1:
 * 
 * 
 * If S[i] == "I", then A[i] < A[i+1]
 * If S[i] == "D", then A[i] > A[i+1]
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "IDID"
 * Output: [0,4,1,3,2]
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "III"
 * Output: [0,1,2,3]
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "DDI"
 * Output: [3,2,0,1]
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= S.length <= 10000
 * S only contains characters "I" or "D".
 * 
 */
impl Solution {
    pub fn di_string_match(s: String) -> Vec<i32> {
        let (mut i, mut j) = (0, s.len());
        let mut res = vec![];
        for c in s.chars() {
            if c == 'I' {
                res.push(i as i32);
                i += 1; 
            } else {
                res.push(j as i32);
                j -= 1;
            }
        }
        res.push(i as i32);
        res 
    }
}
// pub structSolution; 
use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;

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

