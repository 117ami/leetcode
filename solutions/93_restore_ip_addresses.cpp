#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.
Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<string> restoreIpAddresses(string s) {
    vector<string> ans;
    int xsize = s.size();
    string a, b, c, d;
    for (int i = 1; i < 4; i++) {
      for (int j = 1; j < 4; j++) {
        for (int m = 1; m < 4; m++) {
          for (int n = 1; n < 4; n++) {
            if (i + j + m + n != xsize)
              continue;
            a = s.substr(0, i), b = s.substr(i, j), c = s.substr(i + j, m),
            d = s.substr(i + j + m, n);
	    if (validIP(a) && validIP(b) && validIP(c) && validIP(d))
	      ans.push_back(a + "." + b + "." + c + "." + d);
          }
        }
      }
    }
    return ans;
  }

  bool validIP(string s) {
    if (s.size() > 1 && s[0] == '0' || stoi(s) > 255)
      return false;
    return true; 
  }
};

int main() {
  Solution s;
  string strr = "25525511135";
  string strr2 = "010010";
  for (auto &st : s.restoreIpAddresses(strr2))
    cout << st << endl;

  for(string ps : {strr, strr2})
    cout << ps << endl;
}
