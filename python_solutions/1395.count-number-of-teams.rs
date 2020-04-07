/*
 * @lc app=leetcode id=1395 lang=rust
 *
 * [1395] Count Number of Teams
 *
 * https://leetcode.com/problems/count-number-of-teams/description/
 *
 * algorithms
 * Medium (81.24%)
 * Total Accepted:    6.3K
 * Total Submissions: 7.8K
 * Testcase Example:  '[2,5,3,4,1]\r'
 *
 * There are n soldiers standing in a line. Each soldier is assigned a unique
 * rating value.
 * 
 * You have to form a team of 3 soldiers amongst them under the following
 * rules:
 * 
 * 
 * Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
 * rating[k]).
 * A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] >
 * rating[j] > rating[k]) where (0 <= i < j < k < n).
 * 
 * 
 * Return the number of teams you can form given the conditions. (soldiers can
 * be part of multiple teams).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: rating = [2,5,3,4,1]
 * Output: 3
 * Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1),
 * (5,3,1). 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: rating = [2,1,3]
 * Output: 0
 * Explanation: We can't form any team given the conditions.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: rating = [1,2,3,4]
 * Output: 4
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == rating.length
 * 1 <= n <= 200
 * 1 <= rating[i] <= 10^5
 * 
 */
impl Solution {
    pub fn num_teams(rating: Vec<i32>) -> i32 {
        let n = rating.len(); 
        let mut res = 0; 
        for i in 0..n {
            let (mut ls, mut ll, mut rs, mut rl) = (0, 0, 0, 0);
            for j in 0..i {
                if rating[j] < rating[i] { ls += 1; }
                else if rating[j] > rating[i] { ll += 1; }
            }
            for j in i+1..n {
                if rating[j] < rating[i] { rs += 1; }
                else if rating[j] > rating[i] { rl += 1; }
            }
            res += ls * rl + ll * rs; 
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
