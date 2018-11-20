#include "aux.cpp"
/**
There isa special square room with mirrors on each of the fourwalls. Except for
the southwestcorner, there are receptors on each of the remaining corners,
numbered 0, 1, and 2. The square room has walls of length p, and a laser ray
from the southwest cornerfirst meets the east wall at a distance qfrom the 0th
receptor. Return the number of the receptor that the ray meets first. (It is
guaranteed that the ray will meeta receptor eventually.)

Example 1:
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to
the left wall. Note: 1 <= p <= 1000 0 <= q <= p

 https://leetcode.com/problems/mirror-reflection/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int mirrorReflection(int p, int q) {
    int i = 1;
    while (i * q % p != 0)
      i++;
    if (i * q / p % 2 == 0)
      return 0;
    else if (i % 2 == 0)
      return 2;
    return 1;
  }
};

int main() {
  Solution s;
  say(s.mirrorReflection(2, 1));
}
