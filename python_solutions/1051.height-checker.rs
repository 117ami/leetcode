/*
 * @lc app=leetcode id=1051 lang=rust
 *
 * [1051] Height Checker
 *
 * https://leetcode.com/problems/height-checker/description/
 *
 * algorithms
 * Easy (68.54%)
 * Total Accepted:    39.1K
 * Total Submissions: 57K
 * Testcase Example:  '[1,1,4,2,1,3]'
 *
 * Students are asked to stand in non-decreasing order of heights for an annual
 * photo.
 * 
 * Return the minimum number of students that must move in order for all
 * students to be standing in non-decreasing order of height.
 * 
 * 
 * Example 1:
 * Input: heights = [1,1,4,2,1,3]
 * Output: 3
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= heights.length <= 100
 * 1 <= heights[i] <= 100
 * 
 * 
 */
impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut copy = heights.clone(); 
        copy.sort(); 
        copy.iter().zip(&heights).map(|(i, j)| if i == j {0} else {1} ).sum()
        // println!("{:?}", a);
        // println!("{}", a.sum());
        // 1
    }
}



// pub structSolution; 
use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;
use std::collections::VecDeque; 

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

