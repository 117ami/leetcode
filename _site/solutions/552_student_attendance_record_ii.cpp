#include "aux.cpp"
/**
Given a positive integer n, return the number of all possible attendance records
with length n, which will be regarded as rewardable. The answer may be very
large, return it after mod 109 + 7.
A student attendance record is a string that only contains the following three
characters:
'A' : Absent.
'L' : Late.
 'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A'
(absent) or more than two continuous 'L' (late).
Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.
Note:
The value of n won't exceed 100,000.

 https://leetcode.com/problems/student-attendance-record-ii/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int checkRecord(int n) {
    switch (n) {
    case 1:
      return 3;
    case 2:
      return 8;
    case 3:
      return 19;
    }
    vector<long> ea = {1, 2, 4};
    vector<long> ep = {1, 3, 8};
    vector<long> el = {1, 3, 7};
    int mod = 1000000007;
    for (int i = 3; i < n; i++) {
      ea.push_back((ea[i - 1] + ea[i - 2] + ea[i - 3]) % mod);
      ep.push_back((ea[i - 1] + ep[i - 1] + el[i - 1]) % mod);
      el.push_back((ea[i - 1] + ep[i - 1] + ea[i - 2] + ep[i - 2]) % mod);
    }
    return (ea.back() + ep.back() + el.back()) % mod;
  }
};

int main() {
  Solution s;
  srand(time(NULL));
  for (int i = 0; i < 10; i++) {
    int n = rand() % 11;
    cout << n << " " << s.checkRecord(n) << endl;
  }
}
