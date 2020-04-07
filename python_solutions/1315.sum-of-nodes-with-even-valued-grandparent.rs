/*
 * @lc app=leetcode id=1315 lang=rust
 *
 * [1315] Sum of Nodes with Even-Valued Grandparent
 *
 * https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
 *
 * algorithms
 * Medium (83.22%)
 * Total Accepted:    16K
 * Total Submissions: 19.2K
 * Testcase Example:  '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
 *
 * Given a binary tree, return the sum of values of nodes with even-valued
 * grandparent.  (A grandparent of a node is the parent of its parent, if it
 * exists.)
 * 
 * If there are no nodes with an even-valued grandparent, return 0.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
 * Output: 18
 * Explanation: The red nodes are the nodes with even-value grandparent while
 * the blue nodes are the even-value grandparents.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is between 1 and 10^4.
 * The value of nodes is between 1 and 100.
 * 
 */
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// // pub structTreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }

// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn bfs(root: Option<Rc<RefCell<TreeNode>>>, gp: i32, p: i32)->i32 {
        let mut res = 0_i32; 
        if let Some(root) = root{
            if gp % 2 == 0 { res += root.borrow().val ; }
            res += Solution::bfs(root.borrow().left.clone(), p, root.borrow().val);
            res += Solution::bfs(root.borrow().right.clone(), p, root.borrow().val);
            return res; 
        }
        0 
    }
    pub fn sum_even_grandparent(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Solution::bfs(root, 1, 1)
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
