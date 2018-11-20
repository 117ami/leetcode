#include "aux.cpp"
/**
In a deck of cards, each card has an integer written on it.
Return true if and only if you can chooseX >= 2 such thatit is possible to split
the entire deckinto 1 or more groups of cards, where: Each group has exactly X
cards. All the cards in each group have the same integer.

Example 1:
Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:
Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:
Input: [1]
Output: false
Explanation: No possible partition.
Example 4:
Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:
Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
Note:
        1 <= deck.length <= 10000
        0 <= deck[i] <10000


 https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  bool hasGroupsSizeX(vector<int> &deck) {
    sort(deck.begin(), deck.end());
    vector<int> couters;
    int tmp = deck[0], cn = 0;
    for (int n : deck)
      if (tmp != n) {
        couters.emplace_back(cn);
        tmp = n;
        cn = 1;
      } else
        cn++;
    couters.emplace_back(cn);
    sort(couters.begin(), couters.end());
    bool res = true;

    for (tmp = 2; tmp <= couters[0]; tmp++) {
      res = true;
      for (auto n : couters) {
        if (n % tmp != 0) {
          res = false;
          break;
        }
      }
      if (res)
        return true;
    }
    return false;
  }
};

int main() {
  Solution s;
  std::vector<int> deck = {1, 1, 2, 2, 2, 2};
  say(s.hasGroupsSizeX(deck));
}
