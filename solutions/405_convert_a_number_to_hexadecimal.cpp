#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**

Given an integer, write an algorithm to convert it to hexadecimal. For negative
integer, two’s complement method is used.
Note:
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero,
it is represented by a single zero character '0'; otherwise, the first character
in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed
integer.
You must not use any method provided by the library which converts/formats the
number to hex directly.
Example 1:
Input:
26
Output:
"1a"
Example 2:
Input:
-1
Output:
"ffffffff"

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  string toHex(int num) {
    string res = "";
    const string HEX = "0123456789abcdef";
    int cter = 0;
    if (num == 0)
      return "0";

    while (num && cter++ < 8) {
      res = HEX[num & 0xf] + res;
      num >>= 4;
    }
    return res;
  }
};

int main() {
  Solution s;
  int n = 2147483645;
  int m = n & 0xf;
  cout << "The answer is: " << s.toHex(n) << ">>>>>>>>> " << m << endl;
  for (n = 0; n >= -20; n--) {
    int i = n;
    m = i & 0xf;
    i >>= 4;
    cout << "The >>>>>>>>> " << m << ">>>>>>>>>>> " << i << endl;
  }
}
