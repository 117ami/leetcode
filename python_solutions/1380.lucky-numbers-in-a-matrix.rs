/*
 * @lc app=leetcode id=1380 lang=rust
 *
 * [1380] Lucky Numbers in a Matrix
 *
 * https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
 *
 * algorithms
 * Easy (76.44%)
 * Total Accepted:    7.2K
 * Total Submissions: 9.4K
 * Testcase Example:  '[[3,7,8],[9,11,13],[15,16,17]]'
 *
 * Given a m * n matrix of distinct numbers, return all lucky numbers in the
 * matrix in any order.
 * 
 * A lucky number is an element of the matrix such that it is the minimum
 * element in its row and maximum in its column.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
 * Output: [15]
 * Explanation: 15 is the only lucky number since it is the minimum in its row
 * and the maximum in its column
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
 * Output: [12]
 * Explanation: 12 is the only lucky number since it is the minimum in its row
 * and the maximum in its column.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: matrix = [[7,8],[1,2]]
 * Output: [7]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == mat.length
 * n == mat[i].length
 * 1 <= n, m <= 50
 * 1 <= matrix[i][j] <= 10^5.
 * All elements in the matrix are distinct.
 * 
 */
impl Solution {
    pub fn lucky_numbers (matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mins: HashSet<i32> = matrix.iter().map(|row| *row.iter().min().unwrap()).collect(); 
        let maxs: HashSet<i32> = (0..matrix[0].len()).map(|i| matrix.iter().map(|row| row[i]).max().unwrap()).collect();
    
        mins.intersection(&maxs).map(|&n| n).collect()
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