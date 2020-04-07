/*
 * @lc app=leetcode id=1394 lang=rust
 *
 * [1394] Find Lucky Integer in an Array
 *
 * https://leetcode.com/problems/find-lucky-integer-in-an-array/description/
 *
 * algorithms
 * Easy (74.24%)
 * Total Accepted:    9.1K
 * Total Submissions: 12.5K
 * Testcase Example:  '[2,2,3,4]'
 *
 * Given an array of integers arr, a lucky integer is an integer which has a
 * frequency in the array equal to its value.
 * 
 * Return a lucky integer in the array. If there are multiple lucky integers
 * return the largest of them. If there is no lucky integer return -1.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [2,2,3,4]
 * Output: 2
 * Explanation: The only lucky number in the array is 2 because frequency[2] ==
 * 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [1,2,2,3,3,3]
 * Output: 3
 * Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [2,2,2,3,3]
 * Output: -1
 * Explanation: There are no lucky numbers in the array.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: arr = [5]
 * Output: -1
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: arr = [7,7,7,7,7,7,7]
 * Output: 7
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 500
 * 1 <= arr[i] <= 500
 * 
 */
impl Solution {
    pub fn find_lucky(arr: Vec<i32>) -> i32 {
        let mut cnt = vec![0; 501];
        for n in arr { cnt[n as usize] += 1; }
        let mut res = -1; 
        for i in 1..cnt.len() {
            if i as i32 == cnt[i] { res = std::cmp::max(res, cnt[i]); }
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

#[allow(dead_code)]
fn sayi32(i: i32) {
	println!("{}", i);
}

#[allow(dead_code)]
fn sayi32_arr(arr: &Vec<i32>) {
	println!("{:?}", arr);
}

#[allow(dead_code)]
pub fn bisect_left(arr: &Vec<i32>, target: i32) -> usize {
    let (mut lo, mut hi) = (0, arr.len() - 1);
    let mut mid;
    while lo < hi {
        mid = (lo + hi) >> 1; 
        if arr[mid as usize] >= target { hi = mid; }
        else { lo = mid + 1; }
    }
    lo 
 }

 #[allow(dead_code)]
pub fn bisect_right(arr: &Vec<i32>, target: i32) -> usize {
    let (mut lo, mut hi) = (0, arr.len() - 1);
    let mut mid;
    while lo < hi {
        mid = (lo + hi + 1) >> 1; 
        if arr[mid as usize] > target { hi = mid - 1; }
        else { lo = mid; }
    }
    if arr[hi] > target { hi } else {hi + 1}
}
