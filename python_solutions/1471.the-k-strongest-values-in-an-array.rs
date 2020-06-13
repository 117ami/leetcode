/*
 * @lc app=leetcode id=1471 lang=rust
 *
 * [1471] The k Strongest Values in an Array
 *
 * https://leetcode.com/problems/the-k-strongest-values-in-an-array/description/
 *
 * algorithms
 * Medium (55.30%)
 * Total Accepted:    11.6K
 * Total Submissions: 20.3K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given an array of integers arr and an integer k.
 *
 * A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| >
 * |arr[j] - m| where m is the median of the array.
 * If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than
 * arr[j] if arr[i] > arr[j].
 *
 * Return a list of the strongest k values in the array. return the answer in
 * any arbitrary order.
 *
 * Median is the middle value in an ordered integer list. More formally, if the
 * length of the list is n, the median is the element in position ((n - 1) / 2)
 * in the sorted list (0-indexed).
 *
 *
 * For arr = [6, -3, 7, 2, 11], n = 5 and the median is obtained by sorting the
 * array arr = [-3, 2, 6, 7, 11] and the median is arr[m] where m = ((5 - 1) /
 * 2) = 2. The median is 6.
 * For arr = [-7, 22, 17, 3], n = 4 and the median is obtained by sorting the
 * array arr = [-7, 3, 17, 22] and the median is arr[m] where m = ((4 - 1) / 2)
 * = 1. The median is 3.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [1,2,3,4,5], k = 2
 * Output: [5,1]
 * Explanation: Median is 3, the elements of the array sorted by the strongest
 * are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also
 * accepted answer.
 * Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1
 * because 5 > 1.
 *
 *
 * Example 2:
 *
 *
 * Input: arr = [1,1,3,5,5], k = 2
 * Output: [5,5]
 * Explanation: Median is 3, the elements of the array sorted by the strongest
 * are [5,5,1,1,3]. The strongest 2 elements are [5, 5].
 *
 *
 * Example 3:
 *
 *
 * Input: arr = [6,7,11,7,6,8], k = 5
 * Output: [11,8,6,6,7]
 * Explanation: Median is 7, the elements of the array sorted by the strongest
 * are [11,8,6,6,7,7].
 * Any permutation of [11,8,6,6,7] is accepted.
 *
 *
 * Example 4:
 *
 *
 * Input: arr = [6,-3,7,2,11], k = 3
 * Output: [-3,11,2]
 *
 *
 * Example 5:
 *
 *
 * Input: arr = [-7,22,17,3], k = 2
 * Output: [22,17]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= arr.length <= 10^5
 * -10^5 <= arr[i] <= 10^5
 * 1 <= k <= arr.length
 *
 */
impl Solution {
    pub fn get_strongest(ref mut arr: Vec<i32>, k: i32) -> Vec<i32> {
        arr.sort_unstable();
        let m = arr[(arr.len() - 1) >> 1];
        // arr.sort_by(|a, b| (b - m).abs().cmp(&(a-m).abs()).then(b.cmp(&a)));
        // arr[..k as usize].to_vec()
        let mut res = vec![];
        let (mut l, mut r) = (0, arr.len() - 1);
        let k = k as usize;
        while res.len() < k {
            if arr[r] - m >= m - arr[l] {
                res.push(arr[r]);
                r -= 1;
            } else {
                res.push(arr[l]);
                l += 1;
            }
        }
        res
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
