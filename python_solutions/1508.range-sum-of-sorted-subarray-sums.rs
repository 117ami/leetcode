/*
 * @lc app=leetcode id=1508 lang=rust
 *
 * [1508] Range Sum of Sorted Subarray Sums
 *
 * https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/
 *
 * algorithms
 * Medium (75.12%)
 * Total Accepted:    5K
 * Total Submissions: 6.7K
 * Testcase Example:  '[1,2,3,4]\n4\n1\n5'
 *
 * Given the array nums consisting of n positive integers. You computed the sum
 * of all non-empty continous subarrays from the array and then sort them in
 * non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
 *
 * Return the sum of the numbers from index left to index right (indexed from
 * 1), inclusive, in the new array. Since the answer can be a huge number
 * return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
 * Output: 13
 * Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After
 * sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4,
 * 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2
 * + 3 + 3 + 4 = 13.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
 * Output: 6
 * Explanation: The given array is the same as example 1. We have the new array
 * [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to
 * ri = 4 is 3 + 3 = 6.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
 * Output: 50
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^3
 * nums.length == n
 * 1 <= nums[i] <= 100
 * 1 <= left <= right <= n * (n + 1) / 2
 *
 *
 */
impl Solution {
    pub fn range_sum(nums: Vec<i32>, n: i32, left: i32, right: i32) -> i32 {
        let mut pq: BinaryHeap<(i32, usize)> = BinaryHeap::new();
        let left = left as usize;
        let right = right as usize;
        let n = n as usize;

        for i in 0..n {
            pq.push((-1 * nums[i], i));
        }
        let mut ans = 0;
        let MOD = 1000000007;
        for i in 1..right + 1 {
            let p = pq.pop().unwrap();
            if i >= left {
                ans = (ans + (-1 * p.0)) % MOD;
            }
            if p.1 + 1 < n {
                pq.push((p.0 - nums[p.1 + 1], p.1 + 1));
            }
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
