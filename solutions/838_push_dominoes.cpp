#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
There areN dominoes in a line, and we place each domino vertically upright.
In the beginning, we simultaneously pushsome of the dominoes either to the left
or to the right.
After each second, each domino that is falling to the left pushes the adjacent
domino on the left.
Similarly, the dominoes falling to the right push their adjacent dominoes
standing on the right.
When a vertical domino has dominoes falling on it from both sides, it stays
still due to the balance of the forces.
For the purposes of this question, we will consider that a falling dominoexpends
no additional force to a falling or already fallen domino.
Given a string "S" representing the initial state.S[i] = 'L', if the i-th domino
has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to
the right; S[i] = '.',if the i-th domino has not been pushed.
Return a string representing the final state.
Example 1:
Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:
Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:
        0 <= N<= 10^5
        Stringdominoes contains only'L', 'R' and '.'

 https://leetcode.com/problems/push-dominoes/description/
 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  string pushDominoes(string dominoes) {
    dominoes = "L" + dominoes + "R";
    int start = 0;
    for (int i = 0; i < dominoes.size(); i++) {
      if ('.' == dominoes[i] || start == i)
        continue;
      if (dominoes[start] == dominoes[i])
        for (int j = start; j < i; j++)
          dominoes[j] = dominoes[start];

      if ('R' == dominoes[start] && 'L' == dominoes[i]) {
        int j = start, k = i;
        while (j < k) {
          dominoes[j++] = 'R';
          dominoes[k--] = 'L';
        }
      }
      start = i;
    }
    return dominoes.substr(1, dominoes.size() - 2);
  }
};

int main() {
  Solution s;

  string dominoes = ".L.R...LR..L..";
  dominoes = "RR.L";
  say(s.pushDominoes(dominoes));
}
