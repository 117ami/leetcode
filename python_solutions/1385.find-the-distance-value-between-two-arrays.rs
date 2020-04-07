/*
 * @lc app=leetcode id=1385 lang=rust
 *
 * [1385] Find the Distance Value Between Two Arrays
 *
 * https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
 *
 * algorithms
 * Easy (72.11%)
 * Total Accepted:    5.1K
 * Total Submissions: 7.1K
 * Testcase Example:  '[4,5,8]\n[10,9,1,8]\n2'
 *
 * Given two integer arrays arr1 and arr2, and the integer d, return the
 * distance value between the two arrays.
 * 
 * The distance value is defined as the number of elements arr1[i] such that
 * there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
 * Output: 2
 * Explanation: 
 * For arr1[0]=4 we have: 
 * |4-10|=6 > d=2 
 * |4-9|=5 > d=2 
 * |4-1|=3 > d=2 
 * |4-8|=4 > d=2 
 * For arr1[1]=5 we have: 
 * |5-10|=5 > d=2 
 * |5-9|=4 > d=2 
 * |5-1|=4 > d=2 
 * |5-8|=3 > d=2
 * For arr1[2]=8 we have:
 * |8-10|=2 <= d=2
 * |8-9|=1 <= d=2
 * |8-1|=7 > d=2
 * |8-8|=0 <= d=2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
 * Output: 2
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr1.length, arr2.length <= 500
 * -10^3 <= arr1[i], arr2[j] <= 10^3
 * 0 <= d <= 100
 * 
 */

//  pub fn bisect_left(arr: &Vec<i32>, target: i32) -> usize {
//     let (mut lo, mut hi) = (0, arr.len() - 1);
//     let mut mid = 0; 
//     while lo < hi {
//         mid = (lo + hi) >> 1; 
//         if arr[mid as usize] >= target { hi = mid; }
//         else { lo = mid + 1; }
//     }
//     lo 
//  }

impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, arr2: Vec<i32>, d: i32) -> i32 {
        let mut res = 0; 
        for n in arr1.iter() {
            if !arr2.iter().any(|m| (m - n).abs() <= d) {
                res += 1;
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