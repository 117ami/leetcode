#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**
Given a non-empty string containing an out-of-order English representation of
digits 0-9, output the digits in ascending order.
Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits.
That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"
Output: "012"
Example 2:
Input: "fviefuro"
Output: "45"

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
  int letters[26] = {0};
  vector<int> res;

public:
  string originalDigits(string s) {
    for (char c : s)
      letters[c - 'a']++;
    decode('z', 0, "zero");
    decode('w', 2, "two");
    decode('x', 6, "six");
    decode('u', 4, "four");
    decode('g', 8, "eight");
    decode('h', 3, "three");
    decode('f', 5, "five");
    decode('s', 7, "seven");
    decode('o', 1, "one");
    decode('i', 9, "nine");
    string sss = "";
    sort(res.begin(), res.end());
    for (int i : res)
      sss.append(1, '0' + i);
    return sss;
  }

  void decode(char c, int n, string s) {
    while (letters[c - 'a'] > 0) {
      res.push_back(n);
      for (char w : s)
        letters[w - 'a']--;
    }
  }
};

int main() {
  Solution s;
  cout << s.originalDigits("onetwothfninezenineeightroifoeigxishturveree")
       << endl;
}
