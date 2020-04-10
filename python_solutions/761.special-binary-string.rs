/*
 * @lc app=leetcode id=761 lang=rust
 *
 * [761] Special Binary String
 *
 * https://leetcode.com/problems/special-binary-string/description/
 *
 * algorithms
 * Hard (54.28%)
 * Total Accepted:    7.1K
 * Total Submissions: 13.1K
 * Testcase Example:  '"11011000"'
 *
 * 
 * Special binary strings are binary strings with the following two
 * properties:
 * 
 * The number of 0's is equal to the number of 1's.
 * Every prefix of the binary string has at least as many 1's as 0's.
 * 
 * Given a special string S, a move consists of choosing two consecutive,
 * non-empty, special substrings of S, and swapping them.  (Two strings are
 * consecutive if the last character of the first string is exactly one index
 * before the first character of the second string.)
 * 
 * At the end of any number of moves, what is the lexicographically largest
 * resulting string possible?
 * 
 * 
 * Example 1:
 * 
 * Input: S = "11011000"
 * Output: "11100100"
 * Explanation:
 * The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
 * This is the lexicographically largest string possible after some number of
 * swaps.
 * 
 * 
 * 
 * Note:
 * S has length at most 50.
 * S is guaranteed to be a special binary string as defined above.
 * 
 */
impl Solution {
    pub fn make_largest_special(s: String) -> String {
        let mut res = vec![];
        let (mut i, mut cnt) = (0_usize, 0_i32);
        for (j, c) in s.chars().enumerate(){
            cnt += if c == '1' { 1 } else { - 1 }; 
            if cnt == 0 {
                res.push("1".to_string() + &Solution::make_largest_special(s[i+1..j].to_string()) + &"0");
                i = j + 1;
            }
        }
        res.sort_unstable_by(|a, b| b.cmp(&a));
        // res.reverse();
        res.join("")
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

use std::any::type_name;

// To get the type of a variable 
pub fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

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
