/*
 * @lc app=leetcode id=890 lang=rust
 *
 * [890] Find and Replace Pattern
 *
 * https://leetcode.com/problems/find-and-replace-pattern/description/
 *
 * algorithms
 * Medium (72.86%)
 * Total Accepted:    44.7K
 * Total Submissions: 61.3K
 * Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
 *
 * You have a list of words and a pattern, and you want to know which words in
 * words matches the pattern.
 *
 * A word matches the pattern if there exists a permutation of letters p so
 * that after replacing every letter x in the pattern with p(x), we get the
 * desired word.
 *
 * (Recall that a permutation of letters is a bijection from letters to
 * letters: every letter maps to another letter, and no two letters map to the
 * same letter.)
 *
 * Return a list of the words in words that match the given pattern.
 *
 * You may return the answer in any order.
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
 * Output: ["mee","aqq"]
 * Explanation: "mee" matches the pattern because there is a permutation {a ->
 * m, b -> e, ...}.
 * "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
 * permutation,
 * since a and b map to the same letter.
 *
 *
 *
 * Note:
 *
 *
 * 1 <= words.length <= 50
 * 1 <= pattern.length = words[i].length <= 20
 *
 *
 *
 */
pub fn _match(s: &str, t: &str) -> bool {
    let mut m: HashMap<usize, usize> = HashMap::new();
    for (a, b) in s.chars().into_iter().zip(t.chars().into_iter()) {
        let i = a as usize; 
        let j = b as usize + 30_usize; 
        if m.contains_key(&i) && m[&i] != j || m.contains_key(&j) && m[&j] != i {
            return false;
        }
        m.insert(i, j);
        m.insert(j, i);
    }
    true
}

impl Solution {
    pub fn find_and_replace_pattern(words: Vec<String>, pattern: String) -> Vec<String> {
        let mut res: Vec<String> = vec![];
        for w in &words {
            if _match(w, &pattern) {
                res.push(w.clone());
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
