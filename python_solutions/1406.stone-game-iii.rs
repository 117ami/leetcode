/*
 * @lc app=leetcode id=1406 lang=rust
 *
 * [1406] Stone Game III
 *
 * https://leetcode.com/problems/stone-game-iii/description/
 *
 * algorithms
 * Hard (52.01%)
 * Total Accepted:    3.9K
 * Total Submissions: 7.3K
 * Testcase Example:  '[1,2,3,7]'
 *
 * Alice and Bob continue their games with piles of stones. There are several
 * stones arranged in a row, and each stone has an associated value which is an
 * integer given in the array stoneValue.
 * 
 * Alice and Bob take turns, with Alice starting first. On each player's turn,
 * that player can take 1, 2 or 3 stones from the first remaining stones in the
 * row.
 * 
 * The score of each player is the sum of values of the stones taken. The score
 * of each player is 0 initially.
 * 
 * The objective of the game is to end with the highest score, and the winner
 * is the player with the highest score and there could be a tie. The game
 * continues until all the stones have been taken.
 * 
 * Assume Alice and Bob play optimally.
 * 
 * Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end
 * the game with the same score.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: values = [1,2,3,7]
 * Output: "Bob"
 * Explanation: Alice will always lose. Her best move will be to take three
 * piles and the score become 6. Now the score of Bob is 7 and Bob wins.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: values = [1,2,3,-9]
 * Output: "Alice"
 * Explanation: Alice must choose all the three piles at the first move to win
 * and leave Bob with negative score.
 * If Alice chooses one pile her score will be 1 and the next move Bob's score
 * becomes 5. The next move Alice will take the pile with value = -9 and lose.
 * If Alice chooses two piles her score will be 3 and the next move Bob's score
 * becomes 3. The next move Alice will take the pile with value = -9 and also
 * lose.
 * Remember that both play optimally so here Alice will choose the scenario
 * that makes her win.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: values = [1,2,3,6]
 * Output: "Tie"
 * Explanation: Alice cannot win this game. She can end the game in a draw if
 * she decided to choose all the first three piles, otherwise she will lose.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: values = [1,2,3,-1,-2,-3,7]
 * Output: "Alice"
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: values = [-1,-2,-3]
 * Output: "Tie"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= values.length <= 50000
 * -1000 <= values[i] <= 1000
 * 
 */
impl Solution {
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        let n = stone_value.len(); 
        let mut dp = vec![0; n+3];
        let mut s = 0; 
        for j in 0..n {
            let i = n - 1 - j; 
            s += stone_value[i]; 
            dp[i] = s - min(dp[i+1], min(dp[i+2], dp[i+3]));
        }
        // println!("{} {:?}", s, dp);
        if dp[0] * 2 == s { return "Tie".to_string() ; }
        if dp[0] * 2 > s { "Alice".to_string() } else { "Bob".to_string() }
    }
}


// pub structSolution; 

use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;
use std::cmp::min;
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
