/*
 * @lc app=leetcode id=1356 lang=rust
 *
 * [1356] Sort Integers by The Number of 1 Bits
 *
 * https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/
 *
 * algorithms
 * Easy (69.52%)
 * Total Accepted:    6.1K
 * Total Submissions: 8.7K
 * Testcase Example:  '[0,1,2,3,4,5,6,7,8]'
 *
 * Given an integer array arr. You have to sort the integers in the array in
 * ascending order by the number of 1's in their binary representation and in
 * case of two or more integers have the same number of 1's you have to sort
 * them in ascending order.
 * 
 * Return the sorted array.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [0,1,2,3,4,5,6,7,8]
 * Output: [0,1,2,4,8,3,5,6,7]
 * Explantion: [0] is the only integer with 0 bits.
 * [1,2,4,8] all have 1 bit.
 * [3,5,6] have 2 bits.
 * [7] has 3 bits.
 * The sorted array by bits is [0,1,2,4,8,3,5,6,7]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
 * Output: [1,2,4,8,16,32,64,128,256,512,1024]
 * Explantion: All integers have 1 bit in the binary representation, you should
 * just sort them in ascending order.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [10000,10000]
 * Output: [10000,10000]
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: arr = [2,3,5,7,11,13,17,19]
 * Output: [2,3,5,17,7,11,13,19]
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: arr = [10,100,1000,10000]
 * Output: [10,100,10000,1000]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 500
 * 0 <= arr[i] <= 10^4
 * 
 * 
 */
impl Solution {
    pub fn sort_by_bits(mut arr: Vec<i32>) -> Vec<i32> {
        // arr.sort_unstable();
        arr.sort_by(|a, b| a.count_ones().cmp(&b.count_ones()).then(a.cmp(&b))); 
        arr
    }
}
// pub structSolution; 
use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;
use std::collections::VecDeque; 

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

