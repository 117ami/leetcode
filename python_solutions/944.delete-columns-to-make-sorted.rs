/*
 * @lc app=leetcode id=944 lang=rust
 *
 * [944] Delete Columns to Make Sorted
 *
 * https://leetcode.com/problems/delete-columns-to-make-sorted/description/
 *
 * algorithms
 * Easy (69.88%)
 * Total Accepted:    35.1K
 * Total Submissions: 50.3K
 * Testcase Example:  '["cba","daf","ghi"]'
 *
 * We are given an array A of N lowercase letter strings, all of the same
 * length.
 * 
 * Now, we may choose any set of deletion indices, and for each string, we
 * delete all the characters in those indices.
 * 
 * For example, if we have an array A = ["abcdef","uvwxyz"] and deletion
 * indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"],
 * and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
 * (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)
 * 
 * Suppose we chose a set of deletion indices D such that after deletions, each
 * remaining column in A is in non-decreasing sorted order.
 * 
 * Return the minimum possible value of D.length.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: ["cba","daf","ghi"]
 * Output: 1
 * Explanation: 
 * After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in
 * non-decreasing sorted order.
 * If we chose D = {}, then a column ["b","a","h"] would not be in
 * non-decreasing sorted order.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["a","b"]
 * Output: 0
 * Explanation: D = {}
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: ["zyx","wvu","tsr"]
 * Output: 3
 * Explanation: D = {0, 1, 2}
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 100
 * 1 <= A[i].length <= 1000
 * 
 * 
 * 
 * 
 * 
 */
impl Solution {
    pub fn min_deletion_size(a: Vec<String>) -> i32 {
        let mut d = 0; 
        for i in 0..a[0].len() {
            for j in 0..a.len() - 1 {
                if a[j].as_bytes()[i] > a[j+1].as_bytes()[i] {
                    // println!("{:?}", (a[j].chars().nth(i).unwrap(), a[j+1].chars().nth(i).unwrap()));
                    d += 1; 
                    break 
                }
            }
        }
        d
    }
}
// pub structSolution; 
use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;

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

