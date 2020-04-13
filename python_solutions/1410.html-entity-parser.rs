/*
 * @lc app=leetcode id=1410 lang=rust
 *
 * [1410] HTML Entity Parser
 *
 * https://leetcode.com/problems/html-entity-parser/description/
 *
 * algorithms
 * Medium (55.64%)
 * Total Accepted:    7.6K
 * Total Submissions: 13.9K
 * Testcase Example:  ""&amp; is an HTML entity but &ambassador; is not.""
 *
 * HTML entity parser is the parser that takes HTML code as input and replace
 * all the entities of the special characters by the characters itself.
 *
 * The special characters and their entities for HTML are:
 *
 *
 * Quotation Mark: the entity is " and symbol character is ".
 * Single Quote Mark: the entity is " and symbol character is ".
 * Ampersand: the entity is & and symbol character is &.
 * Greater Than Sign: the entity is > and symbol character is >.
 * Less Than Sign: the entity is < and symbol character is <.
 * Slash: the entity is ⁄ and symbol character is /.
 *
 *
 * Given the input text string to the HTML parser, you have to implement the
 * entity parser.
 *
 * Return the text after replacing the entities by the special characters.
 *
 *
 * Example 1:
 *
 *
 * Input: text = "& is an HTML entity but &ambassador; is not."
 * Output: "& is an HTML entity but &ambassador; is not."
 * Explanation: The parser will replace the & entity by &
 *
 *
 * Example 2:
 *
 *
 * Input: text = "and I quote: "...""
 * Output: "and I quote: \"...\""
 *
 *
 * Example 3:
 *
 *
 * Input: text = "Stay home! Practice on Leetcode :)"
 * Output: "Stay home! Practice on Leetcode :)"
 *
 *
 * Example 4:
 *
 *
 * Input: text = "x > y && x < y is always false"
 * Output: "x > y && x < y is always false"
 *
 *
 * Example 5:
 *
 *
 * Input: text = "leetcode.com⁄problemset⁄all"
 * Output: "leetcode.com/problemset/all"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= text.length <= 10^5
 * The string may contain any possible characters out of all the 256 ASCII
 * characters.
 *
 *
 */
impl Solution {
    pub fn entity_parser(text: String) -> String {
        text.replace("&gt;", ">")
            .replace("&lt;", "<")
            .replace("&frasl;", "/")
            .replace("&quot;", "\"")
            .replace("&apos;", "\'")
            .replace("&amp;", "&")
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
