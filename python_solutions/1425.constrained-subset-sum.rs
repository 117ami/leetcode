/*
 * @lc app=leetcode id=1425 lang=rust
 *
 * [1425] Constrained Subset Sum
 *
 * https://leetcode.com/problems/constrained-subset-sum/description/
 *
 * algorithms
 * Hard (30.17%)
 * Total Accepted:    3.2K
 * Total Submissions: 8K
 * Testcase Example:  '[10,2,-10,5,20]\n2'
 *
 * Given an integer array nums and an integer k, return the maximum sum of a
 * non-empty subset of that array such that for every two consecutive integers
 * in the subset, nums[i] and nums[j], where i < j, the condition j - i <= k is
 * satisfied.
 *
 * A subset of an array is obtained by deleting some number of elements (can be
 * zero) from the array, leaving the remaining elements in their original
 * order.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [10,2,-10,5,20], k = 2
 * Output: 37
 * Explanation: The subset is [10, 2, 5, 20].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-1,-2,-3], k = 1
 * Output: -1
 * Explanation: The subset must be non-empty, so we choose the largest
 * number.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [10,-2,-10,-5,20], k = 2
 * Output: 23
 * Explanation: The subset is [10, -2, -5, 20].
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= k <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 *
 *
 */
impl Solution {
    pub fn constrained_subset_sum(A: Vec<i32>, k: i32) -> i32 {
        let k = k as usize; 
        let mut ns = A.to_vec();
        let mut d: VecDeque<i32> = VecDeque::new();
        let mut res = ns[0];

        for i in (0..A.len()) {
            ns[i] += if d.is_empty() { 0 } else { d[0] };
            res = max(res, ns[i]);
            while !d.is_empty() && d.back().unwrap() < &ns[i] {
                d.pop_back();
            }
            if ns[i] > 0 {
                d.push_back(ns[i])
            };
            if i >= k && !d.is_empty() && d[0] == ns[i - k] {
                d.pop_front();
            }
        }
        res
    }
}

// pub struct Solution;
use std::cmp::max;
use std::cmp::min;
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;
// use std::collections::BTreeMap;
use std::any::type_name;
use std::collections::BinaryHeap;

pub struct Helper;
impl Helper {
    pub fn stringify(str_vector: Vec<&str>) -> Vec<String> {
        // Convert a vector of &str to vector or String for coding convenience
        str_vector
            .iter()
            .map(|c| c.to_string())
            .collect::<Vec<String>>()
    }
}

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
    if target > *arr.last().unwrap() {
        return arr.len();
    }
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

#[allow(dead_code)]
fn get_vector_sum(a: &Vec<i32>) -> i32 {
    a.iter().fold(0, |mut sum, &x| {
        sum += x;
        sum
    })
}

#[allow(dead_code)]
fn get_vector_product(a: &Vec<i32>) -> i32 {
    a.iter().fold(1, |mut prod, &x| {
        prod *= x;
        prod
    })
}
