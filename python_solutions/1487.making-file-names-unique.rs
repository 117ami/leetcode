/*
 * @lc app=leetcode id=1487 lang=rust
 *
 * [1487] Making File Names Unique
 *
 * https://leetcode.com/problems/making-file-names-unique/description/
 *
 * algorithms
 * Medium (26.32%)
 * Total Accepted:    6.4K
 * Total Submissions: 24.5K
 * Testcase Example:  '["pes","fifa","gta","pes(2019)"]\r'
 *
 * Given an array of strings names of size n. You will create n folders in your
 * file system such that, at the ith minute, you will create a folder with the
 * name names[i].
 * 
 * Since two files cannot have the same name, if you enter a folder name which
 * is previously used, the system will have a suffix addition to its name in
 * the form of (k), where, k is the smallest positive integer such that the
 * obtained name remains unique.
 * 
 * Return an array of strings of length n where ans[i] is the actual name the
 * system will assign to the ith folder when you create it.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: names = ["pes","fifa","gta","pes(2019)"]
 * Output: ["pes","fifa","gta","pes(2019)"]
 * Explanation: Let's see how the file system creates folder names:
 * "pes" --> not assigned before, remains "pes"
 * "fifa" --> not assigned before, remains "fifa"
 * "gta" --> not assigned before, remains "gta"
 * "pes(2019)" --> not assigned before, remains "pes(2019)"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: names = ["gta","gta(1)","gta","avalon"]
 * Output: ["gta","gta(1)","gta(2)","avalon"]
 * Explanation: Let's see how the file system creates folder names:
 * "gta" --> not assigned before, remains "gta"
 * "gta(1)" --> not assigned before, remains "gta(1)"
 * "gta" --> the name is reserved, system adds (k), since "gta(1)" is also
 * reserved, systems put k = 2. it becomes "gta(2)"
 * "avalon" --> not assigned before, remains "avalon"
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: names =
 * ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
 * Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
 * Explanation: When the last folder is created, the smallest positive valid k
 * is 4, and it becomes "onepiece(4)".
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: names = ["wano","wano","wano","wano"]
 * Output: ["wano","wano(1)","wano(2)","wano(3)"]
 * Explanation: Just increase the value of k each time you create folder
 * "wano".
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: names = ["kaido","kaido(1)","kaido","kaido(1)"]
 * Output: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
 * Explanation: Please note that system adds the suffix (k) to current name
 * even it contained the same suffix before.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= names.length <= 5 * 10^4
 * 1 <= names[i].length <= 20
 * names[i] consists of lower case English letters, digits and/or round
 * brackets.
 * 
 */
impl Solution {
    pub fn get_folder_names(names: Vec<String>) -> Vec<String> {
        let mut memo:HashMap<String, i32>=HashMap::new(); 
        let mut ans = vec![];
        for n in names {
            if !memo.contains_key(&n) {
                ans.push(n.to_string()); 
                memo.insert(n, 1);
            } else {
                let mut uid = memo[&n];
                let mut x = n.to_string() + "(" + &uid.to_string() + ")";
                while memo.contains_key(&x) {
                    uid += 1; 
                    x = n.to_string() + "(" + &uid.to_string() + ")";
                }
                ans.push(x.to_string());
                memo.insert(n, uid + 1);
                memo.insert(x, 1);
            }
        }
        ans 
    }
}


// pub struct Solution; 
static CHARHASH: [i32; 26] = [-9536, -6688, 2006, -2069, 7302, -8825, -8832, 7678, 4540, 7567, 5286, 7027, -8601, -7555, -4541, 6134, 9023, 7805, -3888, 8309, -5265, 7487, -2988, 292, -5646, 7002];

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

pub fn char2usize(c:char) -> usize {
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
    if target > *arr.last().unwrap() { return arr.len() }
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
fn accumulate_sum(nums: Vec<i32>) -> Vec<i32>{
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
    if b == 0 { a } else { gcd(b, a % b)}
}

#[allow(dead_code)]
fn capitalize(word: String) -> String { 
	let mut res = word;
	res.chars().take(1).flat_map(char::to_uppercase).chain(res.chars().skip(1)).collect()
}

