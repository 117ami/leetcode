#include "aux.cpp"
/**
Given a set of candidate numbers (candidates) (without duplicates) and a target
number (target), find all unique combinations in candidateswhere the candidate
numbers sums to target. The same repeated number may be chosen from
candidatesunlimited number of times. Note: All numbers (including target) will
be positive integers. The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
 [2,2,2,2],
 [2,3,3],
 [3,5]
]

 https://leetcode.com/problems/combination-sum/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    vector<std::vector<int>> res;
    if (candidates.size() == 0)
      return res;
    sort(candidates.begin(), candidates.end());
    vector<int> stack;
    backtracking(res, candidates, stack, target, 0);
    return res;
  }

  void backtracking(vector<vector<int>> &res, const vector<int> candidates,
                    vector<int> &stack, int target, int idx) {
    if (target < 0)
      return;
    if (target == 0) {
    	// just push back to the tail without deep or shallow copy of stack
      res.emplace_back(stack);
      return;
    }

    while (idx < candidates.size() && target - candidates[idx] >= 0) {
      stack.emplace_back(candidates[idx]);
      backtracking(res, candidates, stack, target - candidates[idx], idx);
      idx += 1;
      stack.resize(stack.size() - 1);
    }
  }
};

int main() {
  Solution s;
  vector<int> candidates = {2, 3, 5};
  int target = 8;
  for (auto sol : s.combinationSum(candidates, target)) {
    say(sol);
  }
}
