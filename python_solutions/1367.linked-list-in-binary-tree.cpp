#include <vector>
/*
 * @lc app=leetcode id=1367 lang=cpp
 *
 * [1367] Linked List in Binary Tree
 *
 * https://leetcode.com/problems/linked-list-in-binary-tree/description/
 *
 * algorithms
 * Medium (40.10%)
 * Total Accepted:    18.8K
 * Total Submissions: 45.9K
 * Testcase Example:
 * '[4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'
 *
 * Given a binary tree root and a linked list with head as the first node. 
 *
 * Return True if all the elements in the linked list starting from the head
 * correspond to some downward path connected in the binary tree otherwise
 * return False.
 *
 * In this context downward path means a path that starts at some node and goes
 * downwards.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: head = [4,2,8], root =
 * [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
 * Output: true
 * Explanation: Nodes in blue form a subpath in the binary Tree.
 *
 *
 * Example 2:
 *
 *
 *
 *
 * Input: head = [1,4,2,6], root =
 * [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
 * Output: true
 *
 *
 * Example 3:
 *
 *
 * Input: head = [1,4,2,6,8], root =
 * [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
 * Output: false
 * Explanation: There is no path in the binary tree that contains all the
 * elements of the linked list from head.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= node.val <= 100 for each node in the linked list and binary tree.
 * The given linked list will contain between 1 and 100 nodes.
 * The given binary tree will contain between 1 and 2500 nodes.
 *
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
  bool dfs(ListNode *h, TreeNode *r) {
    if (!h)
      return true;
    if (!r)
      return false;
    return h->val == r->val &&
           (dfs(h->next, r->left) || dfs(h->next, r->right));
  }
  
  vector<int> get_values(ListNode *head) {
    vector<int> ns;
    while (head)
      ns.push_back(head->val), head = head->next;
    return ns;
  }
  
  vector<int> get_lhp(vector<int> &ns) {
    int j = 0;
    vector<int> lhp(ns.size(), 0);
    for (int i = 1; i < ns.size(); i++) {
      while (j > 0 && ns[j] != ns[i])
        j = lhp[j - 1];
      if (ns[i] == ns[j])
        lhp[i] = ++j;
    }
    return lhp;
  }

  bool kmp(vector<int> &ns, vector<int> &lhp, int j, TreeNode *root) {
    if (j == lhp.size())
      return true;
    if (!root)
      return false;
    while (j > 0 && ns[j] != root->val)
      j = lhp[j - 1];
    if (root->val == ns[j])
      j++;
    return kmp(ns, lhp, j, root->left) || kmp(ns, lhp, j, root->right);
  }

  bool isSubPath(ListNode *head, TreeNode *root) {
    vector<int> ns = get_values(head);
    vector<int> lhp = get_lhp(ns);
    return kmp(ns, lhp, 0, root);

    // if (!head) return true;
    // if (!root) return false;
    // return dfs(head, root) || isSubPath(head, root->left) || isSubPath(head,
    // root->right);
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
