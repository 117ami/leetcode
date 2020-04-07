/*
 * @lc app=leetcode id=941 lang=rust
 *
 * [941] Valid Mountain Array
 *
 * https://leetcode.com/problems/valid-mountain-array/description/
 *
 * algorithms
 * Easy (35.50%)
 * Total Accepted:    37.8K
 * Total Submissions: 106.4K
 * Testcase Example:  '[2,1]'
 *
 * Given an array A of integers, return true if and only if it is a valid
 * mountain array.
 * 
 * Recall that A is a mountain array if and only if:
 * 
 * 
 * A.length >= 3
 * There exists some i with 0 < i < A.length - 1 such that:
 * 
 * A[0] < A[1] < ... A[i-1] < A[i] 
 * A[i] > A[i+1] > ... > A[A.length - 1]
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [2,1]
 * Output: false
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,5,5]
 * Output: false
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [0,3,2,1]
 * Output: true
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 0 <= A.length <= 10000
 * 0 <= A[i] <= 10000 
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
    pub fn valid_mountain_array(a: Vec<i32>) -> bool {
        if a.len() < 3 { return false ;}
        let mut up:bool = true; 
        let mut pivot = i32::max_value();
        for i in 1..a.len() {
            if a[i] == a[i-1] { return false; }
            if a[i] > a[i-1] && !up { return false; }
            if a[i] < a[i-1] { up = false; pivot = std::cmp::min(pivot, (i-1) as i32); }
        }
        up == false && pivot > 0
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