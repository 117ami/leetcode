/*
 * @lc app=leetcode id=1436 lang=rust
 *
 * [1436] Destination City
 *
 * https://leetcode.com/problems/destination-city/description/
 *
 * algorithms
 * Easy (80.55%)
 * Total Accepted:    9.4K
 * Total Submissions: 11.6K
 * Testcase Example:  '[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]'
 *
 * You are given the array paths, where paths[i] = [cityAi, cityBi] means there
 * exists a direct path going from cityAi to cityBi. Return the destination
 * city, that is, the city without any path outgoing to another city.
 * 
 * It is guaranteed that the graph of paths forms a line without any loop,
 * therefore, there will be exactly one destination city.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao
 * Paulo"]]
 * Output: "Sao Paulo" 
 * Explanation: Starting at "London" city you will reach "Sao Paulo" city which
 * is the destination city. Your trip consist of: "London" -> "New York" ->
 * "Lima" -> "Sao Paulo".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: paths = [["B","C"],["D","B"],["C","A"]]
 * Output: "A"
 * Explanation: All possible trips are: 
 * "D" -> "B" -> "C" -> "A". 
 * "B" -> "C" -> "A". 
 * "C" -> "A". 
 * "A". 
 * Clearly the destination city is "A".
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: paths = [["A","Z"]]
 * Output: "Z"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= paths.length <= 100
 * paths[i].length == 2
 * 1 <= cityAi.length, cityBi.length <= 10
 * cityAi != cityBi
 * All strings consist of lowercase and uppercase English letters and the space
 * character.
 * 
 * 
 */
impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        let s: HashSet<String> = paths.iter().map(|v| v[0].clone()).collect();
        let t: HashSet<String> = paths.iter().map(|v| v[1].clone()).collect();
        t.difference(&s).collect::<Vec<&String>>()[0].to_string()
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
pub fn string_counter(s: String) -> HashMap<char, i32> {
    let mut res = HashMap::new();
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

// There is NO gcd in standard lib for Rust, surprise.  
#[allow(dead_code)]
fn gcd(a: i32, b: i32) -> i32 {
    if b == 0 { a } else { gcd(b, a % b)}
}
