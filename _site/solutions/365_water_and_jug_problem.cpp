#include "aux.cpp"
/**
You are given two jugs with capacities x and y litres. There is an infinite
amount of water supply available. You need to determine whether it is possible
to measure exactly z litres using these two jugs. If z liters of water is
measurable, you must have z liters of water contained within one or both buckets
by the end. Operations allowed: Fill any of the jugs completely with water.
        Empty any of the jugs.
        Pour water from one jug into another till the other jug is completely
full or the first jug itself is empty. Example 1: (From the famous "Die Hard"
example) Input: x = 3, y = 5, z = 4 Output: True Example 2: Input: x = 2, y = 6,
z = 5 Output: False

 https://leetcode.com/problems/water-and-jug-problem/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  bool canMeasureWater(int x, int y, int z) {
    int a = min(x, y), b = max(x, y);
    if (z > a + b || a == 0 && z != b)
      return false;
    if (z == 0 || z == a || z == b || z == a + b || z == b - a)
      return true;

    while (b != 0) {
      int tmp = a;
      a = b;
      b = tmp % b;
    }

    return z % a == 0;
  }
};
int main() {
  Solution s;

  say(s.canMeasureWater(3, 5, 2));
}
