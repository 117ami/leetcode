// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to
// Medium (Difficulty)

// There are n people whose IDs go from 0 to n - 1 and each person belongs
// exactly to one group. Given the array groupSizes of length n telling the
// group size each person belongs to, return the groups there are and the
// people's IDs each group includes. You can return any solution in any order
// and the same applies for IDs. Also, it is guaranteed that there exists at
// least one solution.    Example 1: Example 2:   Constraints: Input: groupSizes
// = [3,3,3,3,3,1,3] Output: [[5],[0,1,2],[3,4,6]] Explanation: Other possible
// solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
//
// Input: groupSizes = [2,1,3,3,3,2]
// Output: [[1],[0,5],[2,3,4]]
//
// xxxxxxxxxx
// class Solution {
// public:
//     vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
//         
//     }
// };
class Solution {
public:
  vector<vector<int>> groupThePeople(vector<int> &groupSizes) {
    vector<vector<int>> ans;
    unordered_map<int, vector<int>> um;

    for (size_t i = 0; i < groupSizes.size(); i++) {
      size_t n = groupSizes[i];
      um[n].push_back(i);
      if (um[n].size() == n) {
        ans.push_back(um[n]);
        um[n].clear();
      }
    }
    return ans;
  }
};