/*
 * @lc app=leetcode id=1387 lang=rust
 *
 * [1387] Sort Integers by The Power Value
 *
 * https://leetcode.com/problems/sort-integers-by-the-power-value/description/
 *
 * algorithms
 * Medium (72.43%)
 * Total Accepted:    3.7K
 * Total Submissions: 5.1K
 * Testcase Example:  '12\n15\n2'
 *
 * The power of an integer x is defined as the number of steps needed to
 * transform x into 1 using the following steps:
 * 
 * 
 * if x is even then x = x / 2
 * if x is odd then x = 3 * x + 1
 * 
 * 
 * For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3
 * --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
 * 
 * Given three integers lo, hi and k. The task is to sort all integers in the
 * interval [lo, hi] by the power value in ascending order, if two or more
 * integers have the same power value sort them by ascending order.
 * 
 * Return the k-th integer in the range [lo, hi] sorted by the power value.
 * 
 * Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will
 * transform into 1 using these steps and that the power of x is will fit in 32
 * bit signed integer.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: lo = 12, hi = 15, k = 2
 * Output: 13
 * Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8
 * --> 4 --> 2 --> 1)
 * The power of 13 is 9
 * The power of 14 is 17
 * The power of 15 is 17
 * The interval sorted by the power value [12,13,14,15]. For k = 2 answer is
 * the second element which is 13.
 * Notice that 12 and 13 have the same power value and we sorted them in
 * ascending order. Same for 14 and 15.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: lo = 1, hi = 1, k = 1
 * Output: 1
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: lo = 7, hi = 11, k = 4
 * Output: 7
 * Explanation: The power array corresponding to the interval [7, 8, 9, 10, 11]
 * is [16, 3, 19, 6, 14].
 * The interval sorted by power is [8, 10, 11, 7, 9].
 * The fourth number in the sorted array is 7.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: lo = 10, hi = 20, k = 5
 * Output: 13
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: lo = 1, hi = 1000, k = 777
 * Output: 570
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= lo <= hi <= 1000
 * 1 <= k <= hi - lo + 1
 * 
 */
impl Solution {
    pub fn get_kth(lo: i32, hi: i32, k: i32) -> i32 {
        let mut res: Vec<_> = vec![];
        for i in lo..hi+1{
            let mut n = i; 
            let mut step = 0; 
            while n > 1 {
                step += 1; 
                n = if n % 2 == 0 { n / 2 } else { 3 * n + 1 }
            }
            res.push((step, i));
        }
        res.sort();
        res[(k-1) as usize].1
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