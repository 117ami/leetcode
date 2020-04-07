/*
 * @lc app=leetcode id=896 lang=rust
 *
 * [896] Monotonic Array
 *
 * https://leetcode.com/problems/monotonic-array/description/
 *
 * algorithms
 * Easy (56.80%)
 * Total Accepted:    82.2K
 * Total Submissions: 144.6K
 * Testcase Example:  '[1,2,2,3]'
 *
 * An array is monotonic if it is either monotone increasing or monotone
 * decreasing.
 * 
 * An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array
 * A is monotone decreasing if for all i <= j, A[i] >= A[j].
 * 
 * Return true if and only if the given array A is monotonic.
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
 * Input: [1,2,2,3]
 * Output: true
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [6,5,4,4]
 * Output: true
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [1,3,2]
 * Output: false
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: [1,2,4,5]
 * Output: true
 * 
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: [1,1,1]
 * Output: true
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 50000
 * -100000 <= A[i] <= 100000
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */
impl Solution {
    pub fn is_monotonic(a: Vec<i32>) -> bool {
        let (mut inc, mut dec) = (true, true);
        for i in 0..a.len()-1{
            inc &= a[i] <= a[i+1];
            dec &= a[i] >= a[i+1];
        }
        inc || dec
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