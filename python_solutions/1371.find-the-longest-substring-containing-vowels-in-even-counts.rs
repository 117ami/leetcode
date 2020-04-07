/*
 * @lc app=leetcode id=1371 lang=rust
 *
 * [1371] Find the Longest Substring Containing Vowels in Even Counts
 *
 * https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
 *
 * algorithms
 * Medium (52.32%)
 * Total Accepted:    2.7K
 * Total Submissions: 5.1K
 * Testcase Example:  '"eleetminicoworoep"'
 *
 * Given the string s, return the size of the longest substring containing each
 * vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must
 * appear an even number of times.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "eleetminicoworoep"
 * Output: 13
 * Explanation: The longest substring is "leetminicowor" which contains two
 * each of the vowels: e, i and o and zero of the vowels: a and u.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "leetcodeisgreat"
 * Output: 5
 * Explanation: The longest substring is "leetc" which contains two e's.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "bcbcbc"
 * Output: 6
 * Explanation: In this case, the given string "bcbcbc" is the longest because
 * all vowels: a, e, i, o and u appear zero times.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 5 x 10^5
 * s contains only lowercase English letters.
 *
 */
impl Solution {
    pub fn find_the_longest_substring(s: String) -> i32 {
        let m: HashMap<char, i32> = [('a', 1), ('e', 2), ('i', 4), ('o', 8), ('u', 16)]
            .iter()
            .cloned()
            .collect();
        let (mut res, mut mask) = (0, 0);
        let mut last = vec![-1; 32];

        for (i, c) in s.chars().enumerate() {
            if m.contains_key(&c) {
                mask ^= m[&c];
            }

            if mask == 0 {
                res = i as i32 + 1;
            } else if last[mask as usize] == -1 {
                last[mask as usize] = i as i32;
            } else {
                res = std::cmp::max(res, i as i32 - last[mask as usize]);
            }
        }
        res
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
