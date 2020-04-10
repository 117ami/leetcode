/*
 * @lc app=leetcode id=828 lang=rust
 *
 * [828] Count Unique Characters of All Substrings of a Given String
 *
 * https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/
 *
 * algorithms
 * Hard (43.71%)
 * Total Accepted:    8.5K
 * Total Submissions: 19.5K
 * Testcase Example:  '"ABC"'
 *
 * Let's define a function countUniqueChars(s) that returns the number of
 * unique characters on s, for example if s = "LEETCODE" then "L",
 * "T","C","O","D" are the unique characters since they appear only once in s,
 * therefore countUniqueChars(s) = 5.
 *
 * On this problem given a string s we need to return the sum of
 * countUniqueChars(t) where t is a substring of s. Notice that some substrings
 * can be repeated so on this case you have to count the repeated ones too.
 *
 * Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "ABC"
 * Output: 10
 * Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
 * Evey substring is composed with only unique letters.
 * Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
 *
 *
 * Example 2:
 *
 *
 * Input: s = "ABA"
 * Output: 8
 * Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "LEETCODE"
 * Output: 92
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= s.length <= 10^4
 * s contain upper-case English letters only.
 *
 *
 */
impl Solution {
    pub fn unique_letter_string(s: String) -> i32 {
        let m: i32 = 10_i32.pow(9) + 7;
        let mut idx = vec![vec![-1; 2]; 26];
        let mut res = 0;
        let mut cnt = vec![0; 1 + s.len()];

        for (j, c) in s.chars().enumerate() {
            let ic = (c as usize - 'A' as usize);

            if idx[ic].last() == Some(&-1) {
                let v = if j == 0 { 0 } else { cnt[j - 1] };
                cnt[j] = j as i32 + 1 + v ;
            } else {
                cnt[j] = j as i32 - idx[ic][1] * 2 + idx[ic][0] + cnt[j - 1]; 
            }

            idx[ic][0] = j as i32; 
            idx[ic].swap(0, 1);
            res = (res + cnt[j]) % m;
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
pub fn say_vec(nums: Vec<i32>) {
    println!("{:?}", nums);
}

#[allow(dead_code)]
pub fn char_frequency(s: String) -> HashMap<char, i32> {
    let mut res: HashMap<char, i32> = HashMap::new();
    for c in s.chars() {
        *res.entry(c).or_insert(0) += 1;
    }
    res
}

#[allow(dead_code)]
pub fn vec_counter(arr: Vec<i32>) -> HashMap<i32, i32> {
    let mut c = HashMap::new();
    for n in arr {
        *c.entry(n).or_insert(0) += 1;
    }
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
        if arr[mid as usize] >= target {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    lo
}

#[allow(dead_code)]
pub fn bisect_right(arr: &Vec<i32>, target: i32) -> usize {
    let (mut lo, mut hi) = (0, arr.len() - 1);
    let mut mid;
    while lo < hi {
        mid = (lo + hi + 1) >> 1;
        if arr[mid as usize] > target {
            hi = mid - 1;
        } else {
            lo = mid;
        }
    }
    if arr[hi] > target {
        hi
    } else {
        hi + 1
    }
}
