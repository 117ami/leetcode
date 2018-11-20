#include "aux.cpp"
/**
Given a list of non negative integers, arrange them such that they form the
largest number.
Example 1:
Input: [10,2]
Output: "210"
Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an
integer.

 https://leetcode.com/problems/largest-number/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  string largestNumber(vector<int> &nums) {
    if (nums.empty())
      return "";
    sort(nums.begin(), nums.end(), [](const int &a, const int &b) {
      return to_string(b) + to_string(a) < to_string(a) + to_string(b);
    });
    string res = "";
    for (int i = 0; i < nums.size(); i++)
      res.append(to_string(nums[i]));
    return res[0] == '0' ? "0" : res;
  }
};
int main() {
  Solution s;
  vector<int> nums = {31, 309, 47, 5, 9};
  nums = {0, 0, 1};
  say(s.largestNumber(nums));
}
