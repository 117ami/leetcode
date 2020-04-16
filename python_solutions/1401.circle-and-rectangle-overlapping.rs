/*
 * @lc app=leetcode id=1401 lang=rust
 *
 * [1401] Circle and Rectangle Overlapping
 *
 * https://leetcode.com/problems/circle-and-rectangle-overlapping/description/
 *
 * algorithms
 * Medium (39.59%)
 * Total Accepted:    3.7K
 * Total Submissions: 9.3K
 * Testcase Example:  '1\n0\n0\n1\n-1\n3\n1'
 *
 * Given a circle represented as (radius, x_center, y_center) and an
 * axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are
 * the coordinates of the bottom-left corner, and (x2, y2) are the coordinates
 * of the top-right corner of the rectangle.
 * 
 * Return True if the circle and rectangle are overlapped otherwise return
 * False.
 * 
 * In other words, check if there are any point (xi, yi) such that belongs to
 * the circle and the rectangle at the same time.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 =
 * 1
 * Output: true
 * Explanation: Circle and rectangle share the point (1,0) 
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 =
 * 1
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * 
 * 
 * Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2
 * = 3
 * Output: true
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 =
 * -1
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= radius <= 2000
 * -10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
 * x1 < x2
 * y1 < y2
 * 
 * 
 */
impl Solution {
    pub fn check_overlap(r: i32, rx: i32, ry: i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
        (rx - min(max(x1, rx), x2)).pow(2) + (ry - min(max(y1, ry), y2)).pow(2) <= r.pow(2)
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
