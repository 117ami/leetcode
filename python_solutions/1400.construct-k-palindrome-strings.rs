/*
 * @lc app=leetcode id=1400 lang=rust
 *
 * [1400] Construct K Palindrome Strings
 *
 * https://leetcode.com/problems/construct-k-palindrome-strings/description/
 *
 * algorithms
 * Medium (55.56%)
 * Total Accepted:    4.5K
 * Total Submissions: 7.9K
 * Testcase Example:  '"annabelle"\n2'
 *
 * Given a string s and an integer k. You should construct k non-empty
 * palindrome strings using all the characters in s.
 *
 * Return True if you can use all the characters in s to construct k palindrome
 * strings or False otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "annabelle", k = 2
 * Output: true
 * Explanation: You can construct two palindromes using all characters in s.
 * Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" +
 * "b"
 *
 *
 * Example 2:
 *
 *
 * Input: s = "leetcode", k = 3
 * Output: false
 * Explanation: It is impossible to construct 3 palindromes using all the
 * characters of s.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "true", k = 4
 * Output: true
 * Explanation: The only possible solution is to put each character in a
 * separate string.
 *
 *
 * Example 4:
 *
 *
 * Input: s = "yzyzyzyzyzyzyzy", k = 2
 * Output: true
 * Explanation: Simply you can put all z's in one string and all y's in the
 * other string. Both strings will be palindrome.
 *
 *
 * Example 5:
 *
 *
 * Input: s = "cr", k = 7
 * Output: false
 * Explanation: We don't have enough characters in s to construct 7
 * palindromes.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * All characters in s are lower-case English letters.
 * 1 <= k <= 10^5
 *
 */
impl Solution {
    pub fn can_construct(s: String, k: i32) -> bool {
        if k > s.len() as i32 {
            return false;
        }
        let mut cache = vec![0; 26];
        for c in s.chars() {
            cache[c as usize - 'a' as usize] += 1;
        }

        let cnt = cache.into_iter().filter(|v| v % 2 == 1).count();
        cnt as i32 <= k
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
