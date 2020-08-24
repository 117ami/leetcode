// C libraries
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

// Containers
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// Input/Output
#include <fstream>
#include <iomanip>
#include <ios>
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>

// Other
#include <algorithm>
#include <bitset>
#include <chrono>
#include <iterator>
#include <limits>
#include <random>
#include <stdexcept>
#include <string>
#include <tuple>
#include <type_traits>
#include <utility>

// ==================================================

using namespace std;

// constants
const double EPS = 1e-9;
const int MOD = 1000000007;

// type alias
using pii = pair<int, int>;
using ll = long long;
using ull = unsigned long long;
using vi = vector<int>;
using vb = vector<bool>;
using vc = vector<char>;
using vs = vector<string>;
using vvb = vector<vector<bool>>;
using vvc = vector<vector<char>>;
using vvi = vector<vector<int>>;
using vvs = vector<vector<string>>;
using mii = map<int, int>;
using mci = map<char, int>;
using si = set<int>;
using spii = set<pair<int, int>>;
using umii = unordered_map<int, int>;
using umci = unordered_map<char, int>;
using umsi = unordered_map<string, int>;
using usi = unordered_set<int>;
using usc = unordered_set<char>;
using uss = unordered_set<string>;
using vpii = vector<pair<int, int>>;

typedef struct TreeNode TreeNode;
using ptn = TreeNode *;
using tn = TreeNode;

// ==================================================

// fast IO
static auto __speedup__ = []() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  return 0;
}();

// ==================================================

// some macro for less typing
#define forloop(i, n) for (int i = 0; i < n; i++)             //[0, n)
#define forloopr(i, n) for (int i = n - 1; i >= 0; --i)       // reverse [0, n)
#define forloopup(i, a, b) for (int i = a; i < b; ++i)        // [a, b)
#define forloopdown(i, a, b) for (int i = b - 1; i >= a; --i) // reverse [a, b)
#define forunfold(i, arr) for (auto &i : arr)

#define INF 0x3f3f3f3f
#define MAX(a, b) a = max(a, b)
#define MIN(a, b) a = min(a, b)

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define ef emplace_front
#define eb emplace_back
#define qall(v) v.begin(), v.end()
#define qsize(v) (int)v.size()
#define qsort(v) sort(v.begin(), v.end())
#define rqsort(v) sort(v.rbegin(), v.rend())
#define qreverse(v) reverse(v.begin(), v.end())

// int to string
string itos(int n) { return to_string(n); }
// char to string
string ctos(char c) { return string(1, c); };

inline string upper(string s) {
  string t(s);
  transform(t.begin(), t.end(), t.begin(), ::toupper);
  return t;
}
inline string lower(string s) {
  string t(s);
  transform(t.begin(), t.end(), t.begin(), ::tolower);
  return t;
}

int dirs[5] = {-1, 0, 1, 0, -1};

// ==================================================
/*
 * @lc app=leetcode id=1032 lang=cpp
 *
 * [1032] Stream of Characters
 *
 * https://leetcode.com/problems/stream-of-characters/description/
 *
 * algorithms
 * Hard (48.28%)
 * Total Accepted:    33.2K
 * Total Submissions: 68.9K
 * Testcase Example:
 '["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"]\n'
 +
  '[[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]'
 *
 * Implement the StreamChecker class as follows:
 *
 *
 * StreamChecker(words): Constructor, init the data structure with the given
 * words.
 * query(letter): returns true if and only if for some k >= 1, the last k
 * characters queried (in order from oldest to newest, including this letter
 * just queried) spell one of the words in the given list.
 *
 *
 *
 *
 * Example:
 *
 *
 * StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init
 * the dictionary.
 * streamChecker.query('a');          // return false
 * streamChecker.query('b');          // return false
 * streamChecker.query('c');          // return false
 * streamChecker.query('d');          // return true, because 'cd' is in the
 * wordlist
 * streamChecker.query('e');          // return false
 * streamChecker.query('f');          // return true, because 'f' is in the
 * wordlist
 * streamChecker.query('g');          // return false
 * streamChecker.query('h');          // return false
 * streamChecker.query('i');          // return false
 * streamChecker.query('j');          // return false
 * streamChecker.query('k');          // return false
 * streamChecker.query('l');          // return true, because 'kl' is in the
 * wordlist
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= words.length <= 2000
 * 1 <= words[i].length <= 2000
 * Words will only consist of lowercase English letters.
 * Queries will only consist of lowercase English letters.
 * The number of queries is at most 40000.
 *
 *
 */

// For shared_ptr class
const int ALPHABET_SIZE = 26;

// trie node
struct TrieNode {
  struct TrieNode *children[ALPHABET_SIZE];

  // True if the node represents end of a word
  bool is_leaf;
};

// Returns new trie node (initialized to NULLs)
struct TrieNode *create_node(void) {
  struct TrieNode *root = new TrieNode;
  root->is_leaf = false;

  for (int i = 0; i < ALPHABET_SIZE; i++)
    root->children[i] = nullptr;

  return root;
}

// If not present, inserts key into trie
// If the key is prefix of trie node, just
// marks leaf node
void insert(struct TrieNode *root, string key) {
  struct TrieNode *pCrawl = root;

  for (int i = 0; i < key.length(); i++) {
    int index = key[i] - 'a';
    if (!pCrawl->children[index])
      pCrawl->children[index] = create_node();

    pCrawl = pCrawl->children[index];
  }

  // mark last node as leaf
  pCrawl->is_leaf = true;
}

// Returns true if key presents in trie, else false
bool search(struct TrieNode *root, string key) {
  struct TrieNode *pCrawl = root;

  for (int i = 0; i < key.length(); i++) {
    int index = key[i] - 'a';
    if (!pCrawl->children[index])
      return false;

    pCrawl = pCrawl->children[index];
  }

  return (pCrawl != NULL && pCrawl->is_leaf);
}

class StreamChecker {
  struct TrieNode *root = create_node();
  vector<char> stack;

public:
  StreamChecker(vector<string> &words) {
    for (auto &w : words) {
      reverse(w.begin(), w.end());
      insert(root, w);
    }
  }

  bool query(char letter) {
    stack.push_back(letter);
    struct TrieNode *cur = root;
    for (auto it = stack.rbegin(); it < stack.rend(); it++) {
      // say(*it);
      int c = *it - 'a';
      if (cur->children[c]) {
        if (cur->children[c]->is_leaf)
          return true;
        else
          cur = cur->children[c];
      } else {
        if (cur == nullptr)
          return true;
        else
          return false;
      }
    }
    return nullptr == cur;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
