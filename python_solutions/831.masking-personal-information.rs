/*
 * @lc app=leetcode id=831 lang=rust
 *
 * [831] Masking Personal Information
 *
 * https://leetcode.com/problems/masking-personal-information/description/
 *
 * algorithms
 * Medium (43.41%)
 * Total Accepted:    9.2K
 * Total Submissions: 21.2K
 * Testcase Example:  '"LeetCode@LeetCode.com"'
 *
 * We are given a personal information string S, which may represent either an
 * email address or a phone number.
 * 
 * We would like to mask this personal information according to the following
 * rules:
 * 
 * 
 * 1. Email address:
 * 
 * We define a name to be a string of length ≥ 2 consisting of only lowercase
 * letters a-z or uppercase letters A-Z.
 * 
 * An email address starts with a name, followed by the symbol '@', followed by
 * a name, followed by the dot '.' and followed by a name. 
 * 
 * All email addresses are guaranteed to be valid and in the format of
 * "name1@name2.name3".
 * 
 * To mask an email, all names must be converted to lowercase and all letters
 * between the first and last letter of the first name must be replaced by 5
 * asterisks '*'.
 * 
 * 
 * 2. Phone number:
 * 
 * A phone number is a string consisting of only the digits 0-9 or the
 * characters from the set {'+', '-', '(', ')', ' '}. You may assume a phone
 * number contains 10 to 13 digits.
 * 
 * The last 10 digits make up the local number, while the digits before those
 * make up the country code. Note that the country code is optional. We want to
 * expose only the last 4 digits and mask all other digits.
 * 
 * The local number should be formatted and masked as "***-***-1111", where 1
 * represents the exposed digits.
 * 
 * To mask a phone number with country code like "+111 111 111 1111", we write
 * it in the form "+***-***-***-1111".  The '+' sign and the first '-' sign
 * before the local number should only exist if there is a country code.  For
 * example, a 12 digit phone number mask should start with "+**-".
 * 
 * Note that extraneous characters like "(", ")", " ", as well as extra dashes
 * or plus signs not part of the above formatting scheme should be removed.
 * 
 * 
 * 
 * Return the correct "mask" of the information provided.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "LeetCode@LeetCode.com"
 * Output: "l*****e@leetcode.com"
 * Explanation: All names are converted to lowercase, and the letters between
 * the
 * first and last letter of the first name is replaced by 5
 * asterisks.
 * Therefore, "leetcode" -> "l*****e".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "AB@qq.com"
 * Output: "a*****b@qq.com"
 * Explanation: There must be 5 asterisks between the first and last
 * letter 
 * of the first name "ab". Therefore, "ab" -> "a*****b".
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "1(234)567-890"
 * Output: "***-***-7890"
 * Explanation: 10 digits in the phone number, which means all digits make up
 * the local number.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "86-(10)12345678"
 * Output: "+**-***-***-5678"
 * Explanation: 12 digits, 2 digits for country code and 10 digits for local
 * number. 
 * 
 * 
 * Notes:
 * 
 * 
 * S.length <= 40.
 * Emails have length at least 8.
 * Phone numbers have length at least 10.
 * 
 * 
 */
impl Solution {
    pub fn mask_pii(s: String) -> String {
        if s.contains("@") {
            let mut res = "".to_string();
            let mut flag = false; 
            let mut pre:char = '#';
            for (i, c) in s.chars().enumerate() {
                if i == 0 { res.push(c);}
                else if c == '@' { res += "*****"; res.push(pre); res.push(c); flag = true; }
                else if flag { res.push(c);}
                pre = c; 
            }
            return res.to_lowercase() ;
        } else {
            let ds = s.chars().into_iter().filter(|c| c.is_numeric()).collect::<Vec<_>>(); 
            let suffix = "***-***-".to_string() + &(ds[(ds.len()-4)..].iter().collect::<String>());
            if ds.len() == 10 { 
                return suffix;
            }
            let mut res = "+".to_string(); 
            for i in 0..ds.len() - 10 {
                res.push('*');
            }
            res.push('-');
            return res + &suffix;
        }
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
