/*
 * @lc app=leetcode id=1366 lang=rust
 *
 * [1366] Rank Teams by Votes
 *
 * https://leetcode.com/problems/rank-teams-by-votes/description/
 *
 * algorithms
 * Medium (50.62%)
 * Total Accepted:    7.6K
 * Total Submissions: 15K
 * Testcase Example:  '["ABC","ACB","ABC","ACB","ACB"]'
 *
 * In a special ranking system, each voter gives a rank from highest to lowest
 * to all teams participated in the competition.
 * 
 * The ordering of teams is decided by who received the most position-one
 * votes. If two or more teams tie in the first position, we consider the
 * second position to resolve the conflict, if they tie again, we continue this
 * process until the ties are resolved. If two or more teams are still tied
 * after considering all positions, we rank them alphabetically based on their
 * team letter.
 * 
 * Given an array of strings votes which is the votes of all voters in the
 * ranking systems. Sort all teams according to the ranking system described
 * above.
 * 
 * Return a string of all teams sorted by the ranking system.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
 * Output: "ACB"
 * Explanation: Team A was ranked first place by 5 voters. No other team was
 * voted as first place so team A is the first team.
 * Team B was ranked second by 2 voters and was ranked third by 3 voters.
 * Team C was ranked second by 3 voters and was ranked third by 2 voters.
 * As most of the voters ranked C second, team C is the second team and team B
 * is the third.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: votes = ["WXYZ","XYZW"]
 * Output: "XWYZ"
 * Explanation: X is the winner due to tie-breaking rule. X has same votes as W
 * for the first position but X has one vote as second position while W doesn't
 * have any votes as second position. 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
 * Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
 * Explanation: Only one voter so his votes are used for the ranking.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
 * Output: "ABC"
 * Explanation: 
 * Team A was ranked first by 2 voters, second by 2 voters and third by 2
 * voters.
 * Team B was ranked first by 2 voters, second by 2 voters and third by 2
 * voters.
 * Team C was ranked first by 2 voters, second by 2 voters and third by 2
 * voters.
 * There is a tie and we rank teams ascending by their IDs.
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: votes = ["M","M","M","M"]
 * Output: "M"
 * Explanation: Only team M in the competition so it has the first rank.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= votes.length <= 1000
 * 1 <= votes[i].length <= 26
 * votes[i].length == votes[j].length for 0 <= i, j < votes.length.
 * votes[i][j] is an English upper-case letter.
 * All characters of votes[i] are unique.
 * All the characters that occur in votes[0] also occur in votes[j] where 1 <=
 * j < votes.length.
 * 
 */
impl Solution {
    pub fn rank_teams(votes: Vec<String>) -> String {
        let mut r = vec![vec![0; 26]; 26];
        for v in &votes {
            for (i, c) in v.chars().enumerate() {
                r[c as usize - 'A' as usize][i] += 1;
            }
        }
        let mut teams:Vec<_> = votes[0].clone().chars().collect();
        teams.sort();
        teams.sort_by(|a, b| r[*b as usize - 'A' as usize].cmp(&r[*a as usize - 'A' as usize]));
        // println!("{:?}", teams);

        // println!("{:?}", r);
        teams.iter().collect()
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
pub fn say_vec(nums: Vec<i32>){
	println!("{:?}", nums);
}

#[allow(dead_code)]
pub fn char_frequency(s: String) -> HashMap<char, i32> {
    let mut res:HashMap<char, i32> = HashMap::new(); 
    for c in s.chars(){
        *res.entry(c).or_insert(0) += 1;
    }
    res 
}

#[allow(dead_code)]
pub fn vec_counter(arr: Vec<i32>) -> HashMap<i32, i32> {
    let mut c = HashMap::new(); 
    for n in arr { *c.entry(n).or_insert(0) += 1; }
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
        if arr[mid as usize] >= target { hi = mid; }
        else { lo = mid + 1; }
    }
    lo 
 }

 #[allow(dead_code)]
pub fn bisect_right(arr: &Vec<i32>, target: i32) -> usize {
    let (mut lo, mut hi) = (0, arr.len() - 1);
    let mut mid;
    while lo < hi {
        mid = (lo + hi + 1) >> 1; 
        if arr[mid as usize] > target { hi = mid - 1; }
        else { lo = mid; }
    }
    if arr[hi] > target { hi } else {hi + 1}
}
