/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (45.09%)
 * Total Accepted:    2.6M
 * Total Submissions: 5.8M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * Example:
 * 
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * 
 */
mod aux; 
use std::collections::HashMap; 

struct Solution(); 
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            if seen.contains_key(num) {
                return vec![seen[num] as i32, i as i32];
            } else {
                seen.insert(target - num, i);
            }
        }
        vec![]
    }
}


fn main(){
    println!("Hello", );
    let vec = vec![2,3,5,7,9];
    let target = 9; 
    let res = Solution::two_sum(vec, target);
    println!("{:?}", res);

    // println!("{:?}", sol::two_sum());
    let mut m = HashMap::new(); 
    m.insert(0, "book".to_string());
    m.insert(0, "computer".to_string());
    m.insert(1, "phone".to_string());
    m.entry(1).or_insert("fake".to_string());
    
    aux::print_map(&m);
    println!("{} {}", 0, m[&0]);

    println!("The length of map {}", m.len());
    
    let x: i8 = 10; 
    println!("{}", x);

    let arr: [i32; 5] = [1,2,3,4,5];
    let y = &arr[1..3];
    println!("{:?}", y);

}