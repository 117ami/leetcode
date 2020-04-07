/*
 * @lc app=leetcode id=1399 lang=rust
 *
 * [1399] Count Largest Group
 *
 * https://leetcode.com/problems/count-largest-group/description/
 *
 * algorithms
 * Easy (59.01%)
 * Total Accepted:    4.3K
 * Total Submissions: 7.2K
 * Testcase Example:  '13\r'
 *
 * Given an integer n. Each number from 1 to n is grouped according to the sum
 * of its digits. 
 * 
 * Return how many groups have the largest size.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 13
 * Output: 4
 * Explanation: There are 9 groups in total, they are grouped according sum of
 * its digits of numbers from 1 to 13:
 * [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups
 * with largest size.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 2
 * Output: 2
 * Explanation: There are 2 groups [1], [2] of size 1.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: n = 15
 * Output: 6
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: n = 24
 * Output: 5
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 10^4
 * 
 * 
 */
impl Solution {
    pub fn count_largest_group(n: i32) -> i32 {
        let mut res = 0; 
        let mut cnt = vec![0; 37];
        let mut cmax = 0; 
        for i in 1.. n + 1 {
            let mut t = 0; 
            let mut k = i; 
            while k > 0 {
                t += k % 10; 
                k = k / 10; 
            }
            cnt[t as usize] += 1; 
            cmax = std::cmp::max(cmax, cnt[t as usize]);
        }
        for v in cnt {
            if v == cmax { res += 1 ;}
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
