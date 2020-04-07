/*
 * @lc app=leetcode id=1282 lang=rust
 *
 * [1282] Group the People Given the Group Size They Belong To
 *
 * https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
 *
 * algorithms
 * Medium (83.50%)
 * Total Accepted:    16.4K
 * Total Submissions: 19.6K
 * Testcase Example:  '[3,3,3,3,3,1,3]'
 *
 * There are n people whose IDs go from 0 to n - 1 and each person belongs
 * exactly to one group. Given the array groupSizes of length n telling the
 * group size each person belongs to, return the groups there are and the
 * people's IDs each group includes.
 * 
 * You can return any solution in any order and the same applies for IDs. Also,
 * it is guaranteed that there exists at least one solution. 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: groupSizes = [3,3,3,3,3,1,3]
 * Output: [[5],[0,1,2],[3,4,6]]
 * Explanation: 
 * Other possible solutions are [[2,1,6],[5],[0,4,3]] and
 * [[5],[0,6,2],[4,3,1]].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: groupSizes = [2,1,3,3,3,2]
 * Output: [[1],[0,5],[2,3,4]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * groupSizes.length == n
 * 1 <= n <= 500
 * 1 <= groupSizes[i] <= n
 * 
 * 
 */
use std::collections::HashMap;

impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res:Vec<Vec<i32>> = vec![]; 
        let mut hm:HashMap<i32, Vec<i32>> = HashMap::new();

        for (i, n) in group_sizes.iter().enumerate(){
            if !hm.contains_key(n) {
                hm.insert(*n, Vec::new());
            }
            hm.get_mut(&n).unwrap().push(i as i32);
            if hm[n].len() as i32 == *n {
                res.push(hm[&n].clone());
                hm.get_mut(&n).unwrap().clear();
            }
        
        }
        res 
    }
}
// pub structSolution; 
