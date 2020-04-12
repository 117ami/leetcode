/*
 * @lc app=leetcode id=1409 lang=rust
 *
 * [1409] Queries on a Permutation With Key
 *
 * https://leetcode.com/problems/queries-on-a-permutation-with-key/description/
 *
 * algorithms
 * Medium (82.19%)
 * Total Accepted:    7.1K
 * Total Submissions: 8.6K
 * Testcase Example:  '[3,1,2,1]\n5'
 *
 * Given the array queries of positive integers between 1 and m, you have to
 * process all queries[i] (from i=0 to i=queries.length-1) according to the
 * following rules:
 *
 *
 * In the beginning, you have the permutation P=[1,2,3,...,m].
 * For the current i, find the position of queries[i] in the permutation P
 * (indexing from 0) and then move this at the beginning of the permutation P.
 * Notice that the position of queries[i] in P is the result for queries[i].
 *
 *
 * Return an array containing the result for the given queries.
 *
 *
 * Example 1:
 *
 *
 * Input: queries = [3,1,2,1], m = 5
 * Output: [2,1,2,1]
 * Explanation: The queries are processed as follow:
 * For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move
 * 3 to the beginning of P resulting in P=[3,1,2,4,5].
 * For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move
 * 1 to the beginning of P resulting in P=[1,3,2,4,5].
 * For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move
 * 2 to the beginning of P resulting in P=[2,1,3,4,5].
 * For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move
 * 1 to the beginning of P resulting in P=[1,2,3,4,5].
 * Therefore, the array containing the result is [2,1,2,1].
 *
 *
 * Example 2:
 *
 *
 * Input: queries = [4,1,2,2], m = 4
 * Output: [3,1,2,0]
 *
 *
 * Example 3:
 *
 *
 * Input: queries = [7,5,5,8,3], m = 8
 * Output: [6,5,0,7,5]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= m <= 10^3
 * 1 <= queries.length <= m
 * 1 <= queries[i] <= m
 *
 */


impl Solution {
    pub fn process_queries(queries: Vec<i32>, m: i32) -> Vec<i32> {
        let mut res: Vec<i32> = vec![];
        let mut m = m as usize;
        let mut ft = FenwickTree::new(2*m+1);
        let mut map: Vec<usize> = vec![0; 2*m+1];
        
        for i in 1..m+1 {
            map[i] = i + m; 
            ft.update(i+m, 1);
        }

        for q in queries {
            res.push(ft.get(map[q as usize]) - 1);
            ft.update(map[q as usize], -1);
            ft.update(m, 1);
            map[q as usize] = m; 
            m -= 1; 
        }
        res
    }
}

// pub struct Solution;

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
