// Containers
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <iostream>
#include <numeric>


#include "conf.d/say.h"

using namespace std; 
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    std::vector<int> res;
    void dfs(TreeNode* r) {
      if (r == nullptr)return ;
      else if (r->left == nullptr && r->right == nullptr) return ;
      else if (r->left == nullptr) { res.push_back(r->right->val); dfs(r->right); }
      else if (r->right == nullptr) { res.push_back(r->left->val); dfs(r->left); }
      else {dfs(r->left); dfs(r->right);}
    }
    vector<int> getLonelyNodes(TreeNode* root) {
      dfs(root);
        return res;
    }
};


int main() {
  Solution s;
  
}