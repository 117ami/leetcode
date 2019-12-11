/**
   This file includes auxiliary functions such as print..
 **/
#include <algorithm>
#include <climits>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <regex>
#include <set>
#include <stack>
#include <stdio.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

/* return vector of int with every item is a random number no bigger than bound,
the size of vector is determined by arg: xsize, when xsize is set to be smaller
than 1
then the size is 10.
**/

vector<int> randvector(int bound, int xsize) {
  cout << "A random vector of size " << xsize << " with bound " << bound << ":" << endl; 
  if (xsize <= 0) xsize = 10;
  vector<int> res;
  srand(time(NULL));
  for (int i = 0; i < xsize; i++)
    res.push_back(rand() % (bound + 1));
  return res;
}

// print a singe item out
template <class T> void say(const T n) {
  cout << fixed << boolalpha << n << endl;
};

// print a pair

template <class T> void say(const pair<T, T> &p) {
  cout << p.first << " " << p.second << endl;
}

// print a vector of items out
template <class T> void say(const vector<T> &vect) {
  // cout << "...printing vector<T>: \n";
  for (auto t : vect)
    cout << t << " ";
  cout << endl;
}

template <class K, class V> void say(const map<K, V> &m) {
  // cout << "...printing map: \n";
  for (auto t = m.begin(); t != m.end(); t++)
    cout << t->first << " " << t->second << endl;
}

// print out a vector of vectors
template <class T> void say(vector<vector<T>> &vv) {
  // cout << "...printing vector<vector<T>>: \n";
  for (auto &v : vv){
    for (auto i: v) 
      cout << i << " "; 
    cout << " " << endl; 
  }
}

// print out a vector of pairs
template <class T> void say(vector<pair<T, T>> &vv) {
  // cout << "...printing vector<vector<T>>: \n";
  for (auto v : vv)
    cout << v.first << " " << v.second << endl;
}


#ifndef NDEBUG
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};
#endif



// Given a vector of integers, construct a tree
TreeNode *arr2tree(vector<int> arr) {
  TreeNode *root = new TreeNode(arr[0]);
  vector<TreeNode *> todo = {root};
  int idx = 1, tid = 0;
  while (idx < arr.size()) {
    if (todo[tid] == nullptr) {
      tid++;
      continue;
    }
    TreeNode *cur = todo[tid];
    TreeNode *left_node =
        arr[idx] == INT_MIN ? nullptr : new TreeNode(arr[idx]);
    TreeNode *right_node = idx >= arr.size() - 1 || arr[++idx] == INT_MIN
                               ? nullptr
                               : new TreeNode(arr[idx]);

    cur->left = left_node;
    cur->right = right_node;
    todo.emplace_back(left_node);
    todo.emplace_back(right_node);
    tid++;
    idx++;
  }
  return root;
}

// Given a root node of a tree, return its traversal of nodes with depth
vector<pair<int, int>> traversalWithDepth(TreeNode *root, int depth = 0) {
  vector<pair<int, int>> res;
  if (root == NULL)
    return res;
  res.emplace_back(make_pair(root->val, depth));
  for (auto pair : traversalWithDepth(root->left, depth + 1))
    res.emplace_back(pair);

  if (root->left == NULL && root->right != NULL)
    res.emplace_back(make_pair(INT_MIN, depth + 1));

  for (auto pair : traversalWithDepth(root->right, depth + 1))
    res.emplace_back(pair);

  return res;
}

void printTree(TreeNode *root) {
  vector<pair<int, int>> vpi = traversalWithDepth(root, 0);
  sort(vpi.begin(), vpi.end(),
       [](const pair<int, int> &a, const pair<int, int> &b) {
         return a.second < b.second;
       });
  for (auto pair : vpi)
    if (pair.first == INT_MIN)
      cout << "NULL ";
    else
      cout << pair.first << " ";
  cout << endl;
}

// int main(int argc, char const *argv[]) {
//   vector<int> arr = {1, 2, 3, 4, -1231, -1231, 6};
//   TreeNode *r = arr2tree(arr);
//   say(r->left->right == nullptr);
//   return 0;
// }

// ********************************************************
// ON Integers
// ********************************************************
vector<int> integerToArray(int x) {
  vector<int> resultArray;
  while (true) {
    resultArray.insert(resultArray.begin(), x % 10);
    x /= 10;
    if (x == 0)
      return resultArray;
  }
}

// ********************************************************
// Strings
// ********************************************************


// int main(int argc, char const *argv[]) {
//   say("Hello");
//   say(string(1, ')'));
//   return 0;
// }


