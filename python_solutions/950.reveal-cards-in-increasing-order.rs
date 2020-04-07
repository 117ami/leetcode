/*
 * @lc app=leetcode id=950 lang=rust
 *
 * [950] Reveal Cards In Increasing Order
 *
 * https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
 *
 * algorithms
 * Medium (73.31%)
 * Total Accepted:    29K
 * Total Submissions: 39.5K
 * Testcase Example:  '[17,13,11,2,3,5,7]'
 *
 * In a deck of cards, every card has a unique integer.  You can order the deck
 * in any order you want.
 * 
 * Initially, all the cards start face down (unrevealed) in one deck.
 * 
 * Now, you do the following steps repeatedly, until all cards are
 * revealed:
 * 
 * 
 * Take the top card of the deck, reveal it, and take it out of the deck.
 * If there are still cards in the deck, put the next top card of the deck at
 * the bottom of the deck.
 * If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
 * 
 * 
 * Return an ordering of the deck that would reveal the cards in increasing
 * order.
 * 
 * The first entry in the answer is considered to be the top of the deck.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [17,13,11,2,3,5,7]
 * Output: [2,13,3,11,5,17,7]
 * Explanation: 
 * We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter),
 * and reorder it.
 * After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top
 * of the deck.
 * We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
 * We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
 * We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
 * We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
 * We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
 * We reveal 13, and move 17 to the bottom.  The deck is now [17].
 * We reveal 17.
 * Since all the cards revealed are in increasing order, the answer is
 * correct.
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 1000
 * 1 <= A[i] <= 10^6
 * A[i] != A[j] for all i != j
 * 
 * 
 * 
 * 
 */
impl Solution {
    pub fn deck_revealed_increasing(mut deck: Vec<i32>) -> Vec<i32> {
        deck.sort_unstable(); 
        deck.reverse(); 
        let mut vd: VecDeque<i32> = VecDeque::new(); 
        vd.push_back(deck[0]); 
        for i in 1..deck.len() {
            vd.push_front(*vd.back().unwrap());
            vd.pop_back(); 
            vd.push_front(deck[i]);
        }
        println!("{:?}", vd);
        Vec::from(vd)
        // deck
    }
}
// pub structSolution; 
use std::collections::HashMap;
use std::collections::HashSet;
use std::fmt::Debug;
use std::hash::Hash;
use std::iter::FromIterator;
use std::collections::VecDeque; 

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

