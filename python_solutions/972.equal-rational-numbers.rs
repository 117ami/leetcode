/*
 * @lc app=leetcode id=972 lang=rust
 *
 * [972] Equal Rational Numbers
 *
 * https://leetcode.com/problems/equal-rational-numbers/description/
 *
 * algorithms
 * Hard (41.49%)
 * Total Accepted:    3.8K
 * Total Submissions: 9.2K
 * Testcase Example:  '"0.(52)"\n"0.5(25)"'
 *
 * Given two strings S and T, each of which represents a non-negative rational
 * number, return True if and only if they represent the same number. The
 * strings may use parentheses to denote the repeating part of the rational
 * number.
 *
 * In general a rational number can be represented using up to three parts: an
 * integer part, a non-repeating part, and a repeating part. The number will be
 * represented in one of the following three ways:
 *
 *
 * <IntegerPart> (e.g. 0, 12, 123)
 * <IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
 * <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6),
 * 0.9(9), 0.00(1212))
 *
 *
 * The repeating portion of a decimal expansion is conventionally denoted
 * within a pair of round brackets.  For example:
 *
 * 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)
 *
 * Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 /
 * 6.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: S = "0.(52)", T = "0.5(25)"
 * Output: true
 * Explanation:
 * Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents
 * 0.52525252525..... , the strings represent the same number.
 *
 *
 *
 * Example 2:
 *
 *
 * Input: S = "0.1666(6)", T = "0.166(66)"
 * Output: true
 *
 *
 *
 * Example 3:
 *
 *
 * Input: S = "0.9(9)", T = "1."
 * Output: true
 * Explanation:
 * "0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See
 * this link for an explanation.]
 * "1." represents the number 1, which is formed correctly: (IntegerPart) = "1"
 * and (NonRepeatingPart) = "".
 *
 *
 *
 *
 *
 * Note:
 *
 *
 * Each part consists only of digits.
 * The <IntegerPart> will not begin with 2 or more zeros.  (There is no other
 * restriction on the digits of each part.)
 * 1 <= <IntegerPart>.length <= 4
 * 0 <= <NonRepeatingPart>.length <= 4
 * 1 <= <RepeatingPart>.length <= 4
 *
 *
 */
impl Solution {
    pub fn unfold(s: String) -> f64 {
        if !s.contains("(") {
            return s.parse::<f64>().unwrap();
        }
        let i = s.find('(').unwrap();
        let rep = &s[i + 1..s.len() - 1];
        let mut base = (&s[..i]).to_string();
        for i in 1..20 {
            base += rep;
        }
        base.parse::<f64>().unwrap()
    }

    pub fn is_rational_equal(s: String, t: String) -> bool {
        Self::unfold(s) == Self::unfold(t)
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
