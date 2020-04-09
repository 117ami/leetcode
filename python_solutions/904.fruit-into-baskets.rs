/*
 * @lc app=leetcode id=904 lang=rust
 *
 * [904] Fruit Into Baskets
 *
 * https://leetcode.com/problems/fruit-into-baskets/description/
 *
 * algorithms
 * Medium (42.17%)
 * Total Accepted:    83.8K
 * Total Submissions: 198.9K
 * Testcase Example:  '[1,2,1]'
 *
 * In a row of trees, the i-th tree produces fruit with type tree[i].
 * 
 * You start at any tree of your choice, then repeatedly perform the following
 * steps:
 * 
 * 
 * Add one piece of fruit from this tree to your baskets.  If you cannot,
 * stop.
 * Move to the next tree to the right of the current tree.  If there is no tree
 * to the right, stop.
 * 
 * 
 * Note that you do not have any choice after the initial choice of starting
 * tree: you must perform step 1, then step 2, then back to step 1, then step
 * 2, and so on until you stop.
 * 
 * You have two baskets, and each basket can carry any quantity of fruit, but
 * you want each basket to only carry one type of fruit each.
 * 
 * What is the total amount of fruit you can collect with this procedure?
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,1]
 * Output: 3
 * Explanation: We can collect [1,2,1].
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [0,1,2,2]
 * Output: 3
 * Explanation: We can collect [1,2,2].
 * If we started at the first tree, we would only collect [0, 1].
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [1,2,3,2,2]
 * Output: 4
 * Explanation: We can collect [2,3,2,2].
 * If we started at the first tree, we would only collect [1, 2].
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: [3,3,3,1,2,1,1,2,3,3,4]
 * Output: 5
 * Explanation: We can collect [1,2,1,1,2].
 * If we started at the first tree or the eighth tree, we would only collect 4
 * fruits.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= tree.length <= 40000
 * 0 <= tree[i] < tree.length
 * 
 * 
 */
impl Solution {
    pub fn total_fruit(tree: Vec<i32>) -> i32 {
        let (mut cnt, mut i, mut res) = (0, 0, 0);
        let mut arr = vec![0; tree.len()];
        for j in 0..tree.len() {
            let t = tree[j] as usize;
            if arr[t] == 0 { cnt += 1; }
            arr[t] += 1; 
            
            while cnt > 2 {
                arr[tree[i] as usize] -= 1;
                if arr[tree[i] as usize] == 0 { cnt -= 1;}
                i += 1;
            }
            res = std::cmp::max(res, j - i + 1);
        }
        res as i32 
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
