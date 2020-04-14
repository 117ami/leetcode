/*
 * @lc app=leetcode id=1411 lang=rust
 *
 * [1411] Number of Ways to Paint N × 3 Grid
 *
 * https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/
 *
 * algorithms
 * Hard (59.43%)
 * Total Accepted:    5K
 * Total Submissions: 8.2K
 * Testcase Example:  '1'
 *
 * You have a grid of size n x 3 and you want to paint each cell of the grid
 * with exactly one of the three colours: Red, Yellow or Green while making
 * sure that no two adjacent cells have the same colour (i.e no two cells that
 * share vertical or horizontal sides have the same colour).
 * 
 * You are given n the number of rows of the grid.
 * 
 * Return the number of ways you can paint this grid. As the answer may grow
 * large, the answer must be computed modulo 10^9 + 7.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 1
 * Output: 12
 * Explanation: There are 12 possible way to paint the grid as shown:
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 2
 * Output: 54
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: n = 3
 * Output: 246
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: n = 7
 * Output: 106494
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: n = 5000
 * Output: 30228214
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == grid.length
 * grid[i].length == 3
 * 1 <= n <= 5000
 * 
 */
impl Solution {
    pub fn num_of_ways(n: i32) -> i32 {
        let (mut r, mut s) = (6_i64, 6_i64) ; 
        let x = 10_i64.pow(9) + 7; 
        for i in 1..n {
            let _r = r * 3 + s * 2; 
            let _s = r * 2 + s * 2; 
            r = _r % x; 
            s = _s % x; 
        }
        ((r + s) % x) as i32 
    }
}


// pub struct Solution; 
use std::cmp::max;
use std::cmp::min;
use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;
// use std::collections::VecDeque;
// use std::collections::BTreeMap;
use std::collections::BinaryHeap; 


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
pub fn say_vec(nums: Vec<i32>) {
    println!("{:?}", nums);
}

#[allow(dead_code)]
pub fn char_frequency(s: String) -> HashMap<char, i32> {
    let mut res: HashMap<char, i32> = HashMap::new();
    for c in s.chars() {
        *res.entry(c).or_insert(0) += 1;
    }
    res
}

#[allow(dead_code)]
pub fn vec_counter(arr: Vec<i32>) -> HashMap<i32, i32> {
    let mut c = HashMap::new();
    for n in arr {
        *c.entry(n).or_insert(0) += 1;
    }
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
        if arr[mid as usize] >= target {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    lo
}

#[allow(dead_code)]
pub fn bisect_right(arr: &Vec<i32>, target: i32) -> usize {
    let (mut lo, mut hi) = (0, arr.len() - 1);
    let mut mid;
    while lo < hi {
        mid = (lo + hi + 1) >> 1;
        if arr[mid as usize] > target {
            hi = mid - 1;
        } else {
            lo = mid;
        }
    }
    if arr[hi] > target {
        hi
    } else {
        hi + 1
    }
}

pub struct FenwickTree {
    vals: Vec<i32>,
}

impl FenwickTree {
    pub fn new(size: usize) -> FenwickTree {
        FenwickTree {
            vals: Vec::from_iter(std::iter::repeat(0).take(size + 1)),
        }
    }

    pub fn update(&mut self, mut i: usize, val: i32) {
        let size = self.vals.len();
        while i < size {
            self.vals[i] += val;
            i += i & (!i + 1);
        }
    }

    pub fn get(&mut self, mut i: usize) -> i32 {
        let mut res = 0;
        while i > 0 {
            res += self.vals[i];
            i -= i & (!i + 1);
        }
        res
    }
}
