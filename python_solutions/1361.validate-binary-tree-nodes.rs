/*
 * @lc app=leetcode id=1361 lang=rust
 *
 * [1361] Validate Binary Tree Nodes
 *
 * https://leetcode.com/problems/validate-binary-tree-nodes/description/
 *
 * algorithms
 * Medium (69.87%)
 * Total Accepted:    6.9K
 * Total Submissions: 9.9K
 * Testcase Example:  '4\n[1,-1,3,-1]\n[2,-1,-1,-1]'
 *
 * You have n binary tree nodes numbered from 0 to n - 1 where node i has two
 * children leftChild[i] and rightChild[i], return true if and only if all the
 * given nodes form exactly one valid binary tree.
 * 
 * If node i has no left child then leftChild[i] will equal -1, similarly for
 * the right child.
 * 
 * Note that the nodes have no values and that we only use the node numbers in
 * this problem.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
 * Output: false
 * 
 * 
 * Example 3:
 * 
 * 
 * 
 * 
 * Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * 
 * 
 * Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 10^4
 * leftChild.length == rightChild.length == n
 * -1 <= leftChild[i], rightChild[i] <= n - 1
 * 
 * 
 */

impl Solution {
    pub fn validate_binary_tree_nodes(n: i32, left_child: Vec<i32>, right_child: Vec<i32>) -> bool {
        let mut nodes_used = vec![0; n as usize];
        for e in left_child { if e >= 0 { nodes_used[e as usize] += 1; }}
        for e in right_child { if e >= 0 { nodes_used[e as usize] += 1; }}
        // println!("{:?}", nodes_used);
        let mut root_number = 0; 
        for e in nodes_used {
            if e > 1 { return false; }
            else if e == 0 { root_number += 1; }
        }
        root_number == 1 
    }
}
// pub structSolution; 
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;
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

