/*
 * @lc app=leetcode id=1499 lang=rust
 *
 * [1499] Max Value of Equation
 *
 * https://leetcode.com/problems/max-value-of-equation/description/
 *
 * algorithms
 * Hard (31.72%)
 * Total Accepted:    1.7K
 * Total Submissions: 3.9K
 * Testcase Example:  '[[1,3],[2,0],[5,10],[6,-10]]\n1'
 *
 * Given an array points containing the coordinates of points on a 2D plane,
 * sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all
 * 1 <= i < j <= points.length. You are also given an integer k.
 *
 * Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj|
 * <= k and 1 <= i < j <= points.length. It is guaranteed that there exists at
 * least one pair of points that satisfy the constraint |xi - xj| <= k.
 *
 *
 * Example 1:
 *
 *
 * Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
 * Output: 4
 * Explanation: The first two points satisfy the condition |xi - xj| <= 1 and
 * if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth
 * points also satisfy the condition and give a value of 10 + -10 + |5 - 6| =
 * 1.
 * No other pairs satisfy the condition, so we return the max of 4 and 1.
 *
 * Example 2:
 *
 *
 * Input: points = [[0,0],[3,0],[9,2]], k = 3
 * Output: 3
 * Explanation: Only the first two points have an absolute difference of 3 or
 * less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= points.length <= 10^5
 * points[i].length == 2
 * -10^8 <= points[i][0], points[i][1] <= 10^8
 * 0 <= k <= 2 * 10^8
 * points[i][0] < points[j][0] for all 1 <= i < j <= points.length
 * xi form a strictly increasing sequence.
 *
 *
 */
impl Solution {
    pub fn find_max_value_of_equation(points: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut d: VecDeque<(i32, i32)> = VecDeque::new();
        let mut ans = i32::min_value();
        for p in points {
            let x = p[0];
            let y = p[1];
            while !d.is_empty() && d[0].0 + k < x {
                d.pop_front();
            }
            if !d.is_empty() {
                ans = max(ans, y + x + d[0].1);
            }
            while !d.is_empty() && d.back().unwrap().1 <= y - x {
                d.pop_back();
            }
            d.push_back((x, y - x));
        }
        ans
    }
}

// pub struct Solution;
static CHARHASH: [i32; 26] = [
    -9536, -6688, 2006, -2069, 7302, -8825, -8832, 7678, 4540, 7567, 5286, 7027, -8601, -7555,
    -4541, 6134, 9023, 7805, -3888, 8309, -5265, 7487, -2988, 292, -5646, 7002,
];

pub fn hash_string(s: String) -> i32 {
    s.chars().map(|c| CHARHASH[char2usize(c)]).sum()
}

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
    pub fn is_palindrome(s: String) -> bool {
        let cs: Vec<char> = s.chars().collect();
        for i in 0..s.len() / 2 {
            if cs[i] != cs[s.len() - i - 1] {
                return false;
            }
        }
        true
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
pub fn string_counter(s: &str) -> HashMap<char, i32> {
    let mut res = HashMap::new();
    for c in s.chars() {
        *res.entry(c).or_insert(0) += 1;
    }
    res
}

#[allow(dead_code)]
pub fn vec_counter(arr: &Vec<i32>) -> HashMap<i32, i32> {
    let mut c = HashMap::new();
    for n in arr {
        *c.entry(*n).or_insert(0) += 1;
    }
    c
}

#[allow(dead_code)]
pub fn vec_to_hashset(arr: &Vec<i32>) -> HashSet<i32> {
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

#[allow(dead_code)]
fn accumulate_sum(nums: Vec<i32>) -> Vec<i32> {
    nums.iter()
        .scan(0, |sum, &v| {
            *sum += v;
            Some(*sum)
        })
        .collect::<Vec<i32>>()
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

#[allow(dead_code)]
fn capitalize(word: String) -> String {
    let mut res = word;
    res.chars()
        .take(1)
        .flat_map(char::to_uppercase)
        .chain(res.chars().skip(1))
        .collect()
}
