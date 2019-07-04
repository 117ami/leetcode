#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

/**

Given a list of sorted characters letters containing only lowercase letters, and
given a target letter target, find the smallest element in the list that is
larger than the given target. Letters also wrap around.  For example, if the
target is target = 'z' and letters = ['a', 'b'], the answer is 'a'. Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"
Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"
Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"
Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"
Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"
Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
**/

// void say(string s) { cout << s << endl; }
// void say(char i) { cout << i << endl; }
// void say(vector<char> ivec) {
//   cout << "The char vector is: " << endl;
//   for (auto &c: ivec)
//     cout << c << " ";
//   cout << endl;
// }

template <class T, class ...Args>
void say(T head, Args... rest)
{
  cout << "parameter " << head << endl;
  say(rest...);
}


class Solution {
public:
  char nextGreatestLetter(vector<char> &letters, char target) {
    say(letters);
    for (auto &c : letters)
      if (c > target)
        return c;
    return letters[0];
  }
};

int main() {
  cout << "Leetcode 744" << endl;
  Solution s;
  string str = "cfj";
  char target = 'd';
  vector<char> letters(str.begin(), str.end());
  cout << s.nextGreatestLetter(letters, target) << endl;
  say(letters.front());
  say(letters.back()); 
}
