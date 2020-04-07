/*
 * @lc app=leetcode id=1375 lang=rust
 *
 * [1375] Bulb Switcher III
 *
 * https://leetcode.com/problems/bulb-switcher-iii/description/
 *
 * algorithms
 * Medium (58.83%)
 * Total Accepted:    7.3K
 * Total Submissions: 12.4K
 * Testcase Example:  '[2,1,3,5,4]'
 *
 * There is a room with n bulbs, numbered from 1 to n, arranged in a row from
 * left to right. Initially, all the bulbs are turned off.
 * 
 * At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb
 * change color to blue only if it is on and all the previous bulbs (to the
 * left) are turned on too.
 * 
 * Return the number of moments in which all turned on bulbs are blue.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: light = [2,1,3,5,4]
 * Output: 3
 * Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: light = [3,2,4,1,5]
 * Output: 2
 * Explanation: All bulbs turned on, are blue at the moment 3, and 4
 * (index-0).
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: light = [4,1,2,3]
 * Output: 1
 * Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
 * Bulb 4th changes to blue at the moment 3.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: light = [2,1,4,3,6,5]
 * Output: 3
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: light = [1,2,3,4,5,6]
 * Output: 6
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == light.length
 * 1 <= n <= 5 * 10^4
 * light is a permutation of  [1, 2, ..., n]
 * 
 * 
 */
impl Solution {
    pub fn num_times_all_blue(light: Vec<i32>) -> i32 {
        let mut res = 0; 
        let mut t = 0; 
        for (i, n) in light.iter().enumerate(){
            t += (i + 1) as i32 - n;
            if t == 0 { res += 1; }
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

