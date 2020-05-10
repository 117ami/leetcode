/*
 * @lc app=leetcode id=1441 lang=rust
 *
 * [1441] Build an Array With Stack Operations
 *
 * https://leetcode.com/problems/build-an-array-with-stack-operations/description/
 *
 * algorithms
 * Easy (68.07%)
 * Total Accepted:    6.6K
 * Total Submissions: 9.7K
 * Testcase Example:  '[1,3]\r\n3\r'
 *
 * Given an array target and an integer n. In each iteration, you will read a
 * number from  list = {1,2,3..., n}.
 *
 * Build the target array using the following operations:
 *
 *
 * Push: Read a new element from the beginning list, and push it in the
 * array.
 * Pop: delete the last element of the array.
 * If the target array is already built, stop reading more elements.
 *
 *
 * You are guaranteed that the target array is strictly increasing, only
 * containing numbers between 1 to n inclusive.
 *
 * Return the operations to build the target array.
 *
 * You are guaranteed that the answer is unique.
 *
 *
 * Example 1:
 *
 *
 * Input: target = [1,3], n = 3
 * Output: ["Push","Push","Pop","Push"]
 * Explanation:
 * Read number 1 and automatically push in the array -> [1]
 * Read number 2 and automatically push in the array then Pop it -> [1]
 * Read number 3 and automatically push in the array -> [1,3]
 *
 *
 * Example 2:
 *
 *
 * Input: target = [1,2,3], n = 3
 * Output: ["Push","Push","Push"]
 *
 *
 * Example 3:
 *
 *
 * Input: target = [1,2], n = 4
 * Output: ["Push","Push"]
 * Explanation: You only need to read the first 2 numbers and stop.
 *
 *
 * Example 4:
 *
 *
 * Input: target = [2,3,4], n = 4
 * Output: ["Push","Pop","Push","Push","Push"]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= target.length <= 100
 * 1 <= target[i] <= 100
 * 1 <= n <= 100
 * target is strictly increasing.
 *
 *
 */
impl Solution {
    pub fn build_array(target: Vec<i32>, n: i32) -> Vec<String> {
        let cc: HashSet<i32> = HashSet::from_iter(target);
        let m = min(n, *cc.iter().max().unwrap());
        let mut res: Vec<String> = vec![];
        for i in 1..1 + m {
            res.push("Push".to_string());
            if !cc.contains(&i) {
                res.push("Pop".to_string())
            };
        }
        res
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
use std::any::type_name;
use std::collections::BinaryHeap;

pub fn char2usize(c: char) -> usize {
    c as usize - 97
}

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
pub fn string_counter(s: String) -> HashMap<char, i32> {
    let mut res = HashMap::new();
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

// There is NO gcd in standard lib for Rust, surprise.
#[allow(dead_code)]
fn gcd(a: i32, b: i32) -> i32 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}
