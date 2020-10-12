// Containers
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "conf.d/say.h"

using namespace std;
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
/**
 * Definition for a binary tree node.
 * struct Node {
 *     char val;
 *     Node *left;
 *     Node *right;
 *     Node() : val(' '), left(nullptr), right(nullptr) {}
 *     Node(char x) : val(x), left(nullptr), right(nullptr) {}
 *     Node(char x, Node *left, Node *right) : val(x), left(left), right(right)
 * {}
 * };
 */
class Solution {
public:
  int cnt[26];
  void querySum(Node *root, int n) {
    if (root->val == '+') {
      querySum(root->left, n);
      querySum(root->right, n);
    } else {
      cnt[root->val - 'a'] += n;
    }
  }
  bool checkEquivalence(Node *root1, Node *root2) {
    memset(cnt, 0, sizeof(cnt));
    querySum(root1, 1), querySum(root2, -1);
    for (int i = 0; i < 26; i++)
      if (cnt[i] != 0)
        return false;
    return true;
  }
};

int main() {
  Solution s;
  size_t char_h = std::hash<char>{}('a');
  say(char_h);
}