/*
 * @lc app=leetcode id=1402 lang=rust
 *
 * [1402] Reducing Dishes
 *
 * https://leetcode.com/problems/reducing-dishes/description/
 *
 * algorithms
 * Hard (74.25%)
 * Total Accepted:    3.7K
 * Total Submissions: 5K
 * Testcase Example:  '[-1,-8,0,5,-7]'
 *
 * A chef has collected data on the satisfaction level of his n dishes. Chef
 * can cook any dish in 1 unit of time.
 * 
 * Like-time coefficient of a dish is defined as the time taken to cook that
 * dish including previous dishes multiplied by its satisfaction level  i.e.
 * time[i]*satisfaction[i]
 * 
 * Return the maximum sum of Like-time coefficient that the chef can obtain
 * after dishes preparation.
 * 
 * Dishes can be prepared in any order and the chef can discard some dishes to
 * get this maximum value.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: satisfaction = [-1,-8,0,5,-9]
 * Output: 14
 * Explanation: After Removing the second and last dish, the maximum total
 * Like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is
 * prepared in one unit of time.
 * 
 * Example 2:
 * 
 * 
 * Input: satisfaction = [4,3,2]
 * Output: 20
 * Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: satisfaction = [-1,-4,-5]
 * Output: 0
 * Explanation: People don't like the dishes. No dish is prepared.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: satisfaction = [-2,5,-1,0,3,-3]
 * Output: 35
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == satisfaction.length
 * 1 <= n <= 500
 * -10^3 <= satisfaction[i] <= 10^3
 * 
 */
impl Solution {
    pub fn max_satisfaction(sa: Vec<i32>) -> i32 {
        let mut sa = sa;
        sa.sort(); 
        sa.reverse(); 
        let (mut res, mut part, mut i) = (0, 0, 0_usize) ;
        while i < sa.len() && part + sa[i] > 0 {
            part += sa[i];
            res += part; 
            i += 1; 
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
