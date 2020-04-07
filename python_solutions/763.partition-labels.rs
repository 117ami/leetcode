/*
 * @lc app=leetcode id=763 lang=rust
 *
 * [763] Partition Labels
 *
 * https://leetcode.com/problems/partition-labels/description/
 *
 * algorithms
 * Medium (73.56%)
 * Total Accepted:    90K
 * Total Submissions: 122.4K
 * Testcase Example:  '"ababcbacadefegdehijhklij"'
 *
 * 
 * A string S of lowercase letters is given.  We want to partition this string
 * into as many parts as possible so that each letter appears in at most one
 * part, and return a list of integers representing the size of these parts.
 * 
 * 
 * Example 1:
 * 
 * Input: S = "ababcbacadefegdehijhklij"
 * Output: [9,7,8]
 * Explanation:
 * The partition is "ababcbaca", "defegde", "hijhklij".
 * This is a partition so that each letter appears in at most one part.
 * A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
 * splits S into less parts.
 * 
 * 
 * 
 * Note:
 * S will have length in range [1, 500].
 * S will consist of lowercase letters ('a' to 'z') only.
 * 
 */
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut last:HashMap<char, usize> = HashMap::new(); 
        for (i, c) in s.chars().enumerate() {
            last.insert(c, i);
        }

        let (mut start, mut end) = (0_usize, 0_usize); 
        let mut res:Vec<i32> = vec![];
        for (i, c) in s.chars().enumerate() {
            end = std::cmp::max(end, last[&c]);
            if i == end {
                res.push((end - start) as i32 + 1);
                start = i + 1;
            }
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

