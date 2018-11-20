#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
A password is considered strong if below conditions are all met:
 It has at least 6 characters and at most 20 characters.
 It must contain at least one lowercase letter, at least one uppercase letter,
and at least one digit. It must NOT contain three repeating characters in a row
("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions
are met). Write a function strongPasswordChecker(s), that takes a string s as
input, and return the MINIMUM change required to make s a strong password. If s
is already strong, return 0. Insertion, deletion or replace of any one character
are all considered as one change.
 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int strongPasswordChecker(string s) {
    int res = 0;
    if (is_strong(s))
      return res;

    return res;
  }

  // assume the length of s is less than 6, we consider how many steps are
  // required to make it a strong password

  int insert_letters_2b_strong(string s) {
    if (s.size() <= 3) // has no more than 3 characters
      return 6 - s.size();
    else{     	// check the number of digit, uppercase and lowercase letters {
		int cter = 0;
		      for (char c : s)
        if (c >= '0' && c <= '9' || c >= 'a' && c <= 'z' || 
            c >= 'A' && c <= 'Z')
		cter ++; 
    }
    if (cter == 0 ) return 3; 
    else if (cter == 1 ) return 2; 
    else if (cter == 2 ) return s.size() == 4 ? 2 : 1; 

  }

  bool is_strong(string s) {
    if (s.size() < 6 || s.size() > 20)
      return false;
    bool lowercase = false, uppercase = false, digit = false;
    for (int i = 0; i < s.size(); i++) {
      int asc = int(s[i]);
      digit = digit || asc <= 57 && asc >= 48;
      lowercase = lowercase || asc <= 90 && asc >= 65;
      uppercase = uppercase || asc <= 122 && asc >= 97;
      if (i >= 2 && s[i] == s[i - 1] && s[i - 1] == s[i - 2])
        return false;
    }
    return lowercase && uppercase && digit;
  }
};

int main() {
  Solution s;
  cout << int('0') << endl;
  string password = "123aAldsajk";
  cout << s.is_strong(password) << endl;
}
